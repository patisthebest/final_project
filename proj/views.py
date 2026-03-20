from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import requests
import base64
import json
from datetime import datetime

from .credentials import (
    MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET, MPESA_SHORTCODE,
    MPESA_PASSKEY, MPESA_ACCESS_TOKEN_URL, MPESA_STK_PUSH_URL
)

from .forms import BusinessForm, JobVacancyForm
from .models import Business, JobVacancy


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def employers(request):
    return render(request, 'employers.html')


def jobs(request):
    return render(request, 'jobs.html')


# ---------------- M-PESA FUNCTIONS ---------------- #

def get_access_token():
    """Get M-Pesa access token"""
    try:
        response = requests.get(
            MPESA_ACCESS_TOKEN_URL,
            auth=(MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET)
        )
        response.raise_for_status()
        data = response.json()
        return data.get('access_token')
    except requests.RequestException as e:
        print("Access Token Error:", e)
        return None


def initiate_stk_push(phone_number, amount):
    """Initiate STK Push"""
    access_token = get_access_token()

    if not access_token:
        return {"error": "Could not get access token"}

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    password_string = f"{MPESA_SHORTCODE}{MPESA_PASSKEY}{timestamp}"
    password = base64.b64encode(password_string.encode()).decode()

    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),
        "PartyA": phone_number,
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://your-domain.com/mpesa-callback",  # Replace with real callback
        "AccountReference": "WebsiteService",
        "TransactionDesc": "Payment for website service"
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    print("STK PUSH PAYLOAD:", payload)

    try:
        response = requests.post(
            MPESA_STK_PUSH_URL,
            json=payload,
            headers=headers
        )

        print("MPESA RESPONSE:", response.text)

        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print("STK PUSH ERROR:", e)
        return {"error": str(e)}


# ---------------- PAYMENT VIEW ---------------- #

def payment_view(request):
    """Payment page"""
    if request.method == "POST":

        phone_number = request.POST.get("phone_number")
        amount = 50

        if not phone_number:
            return JsonResponse({"error": "Phone number required"})

        # Convert phone number to 254 format
        if phone_number.startswith("0"):
            phone_number = "254" + phone_number[1:]

        elif phone_number.startswith("+254"):
            phone_number = phone_number[1:]

        elif not phone_number.startswith("254"):
            return JsonResponse({"error": "Invalid phone number format"})

        result = initiate_stk_push(phone_number, amount)

        return JsonResponse(result)

    return render(request, "payment.html")


# ---------------- M-PESA CALLBACK ---------------- #

@csrf_exempt
def mpesa_callback(request):
    """Handle M-Pesa callback"""
    if request.method == "POST":
        try:
            callback_data = json.loads(request.body)

            print("M-PESA CALLBACK DATA:")
            print(json.dumps(callback_data, indent=4))

            return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})

        except Exception as e:
            print("Callback Error:", e)
            return JsonResponse({"error": "Invalid callback"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=405)


# ---------------- BUSINESS FUNCTIONS ---------------- #

def register_business(request):

    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Business registered successfully!")
            return redirect("business_list")

    else:
        form = BusinessForm()

    return render(request, "register_business.html", {"form": form})


def business_list(request):

    businesses = Business.objects.filter(is_active=True).order_by("-created_at")

    return render(request, "business_list.html", {"businesses": businesses})


# ---------------- JOB FUNCTIONS ---------------- #

def post_job(request):

    if request.method == "POST":
        form = JobVacancyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Job vacancy posted successfully!")
            return redirect("job_list")

    else:
        form = JobVacancyForm()

    return render(request, "post_job.html", {"form": form})


def job_list(request):

    jobs = JobVacancy.objects.filter(is_active=True).order_by("-created_at")

    return render(request, "job_list.html", {"jobs": jobs})