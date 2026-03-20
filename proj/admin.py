from django.contrib import admin
from .models import Business, JobVacancy

# Register your models here.

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_type', 'location', 'contact_person', 'email', 'is_active', 'created_at')
    list_filter = ('business_type', 'location', 'is_active', 'created_at')
    search_fields = ('name', 'business_type', 'contact_person', 'email', 'location')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(JobVacancy)
class JobVacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'contact_email', 'is_active', 'created_at', 'application_deadline')
    list_filter = ('location', 'is_active', 'created_at', 'application_deadline')
    search_fields = ('title', 'company', 'location', 'contact_email', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
