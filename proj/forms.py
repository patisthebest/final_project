from django import forms
from .models import Business, JobVacancy

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'contact_person', 'phone', 'email', 'location', 'business_type', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class JobVacancyForm(forms.ModelForm):
    class Meta:
        model = JobVacancy
        fields = ['title', 'company', 'description', 'requirements', 'location', 'salary_range', 'contact_email', 'contact_phone', 'application_deadline', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'requirements': forms.Textarea(attrs={'rows': 4}),
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
        }