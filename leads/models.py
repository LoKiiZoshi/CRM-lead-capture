# Models for lead capture
from django.db import models

class Lead(models.Model):
    # Choices for lead source
    SOURCE_CHOICES = (
        ('website_form', 'Website Form'),
        ('email', 'Email'),
    )

    # Lead fields
    first_name = models.CharField(max_length=100, blank=True)  # First name from form or email
    last_name = models.CharField(max_length=100, blank=True)  # Last name from form or email
    email = models.EmailField(unique=True)  # Email address, unique to prevent duplicates
    phone = models.CharField(max_length=20, blank=True)  # Phone number, optional
    company = models.CharField(max_length=200, blank=True)  # Company name, optional
    message = models.TextField(blank=True)  # Additional message or email body
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)  # Source of the lead
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of last update

    def __str__(self):
        return f"{self.email} ({self.source})"  # String representation for admin

    class Meta:
        ordering = ['-created_at']  # Order leads by creation date, newest first