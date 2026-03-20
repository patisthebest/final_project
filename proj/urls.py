from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('employers/', views.employers, name='employers'),
    path('jobs/', views.jobs, name='jobs'),
    path('payment/', views.payment_view, name='payment'),
    path('callback/', views.mpesa_callback, name='mpesa_callback'),
    path('register-business/', views.register_business, name='register_business'),
    path('post-job/', views.post_job, name='post_job'),
    path('businesses/', views.business_list, name='business_list'),
    path('job-vacancies/', views.job_list, name='job_list'),
]