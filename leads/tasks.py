# Celery tasks for lead processing
from celery import shared_task
from django.core.mail import send_mail
from .models import Lead

@shared_task
def send_lead_notification(lead_id):
    # Send notification to sales team for new lead
    try:
        lead = Lead.objects.get(id=lead_id)
        subject = f"New Lead: {lead.email}"
        message = f"A new lead was created:\n\nEmail: {lead.email}\nSource: {lead.source}\nMessage: {lead.message}"
        send_mail(
            subject,
            message,
            'from@yourcrm.com',
            ['sales@yourcrm.com'],
            fail_silently=False,
        )
    except Lead.DoesNotExist:
        # Log error if lead not found
        print(f"Lead with ID {lead_id} not found")