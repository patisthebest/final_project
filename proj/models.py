from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    business_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='business_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Businesses"

class JobVacancy(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=200)
    salary_range = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15, blank=True)
    application_deadline = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='job_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        verbose_name_plural = "Job Vacancies"
