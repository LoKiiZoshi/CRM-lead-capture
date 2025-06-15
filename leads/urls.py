# URL patterns for leads app
from django.urls import path
from . import views
from .forms import LeadFormView

app_name = 'leads'

urlpatterns = [
    path('api/leads/', views.LeadCreateAPIView.as_view(), name='lead-create'),  # API for form leads
    path('api/leads/email/', views.EmailLeadCreateAPIView.as_view(), name='email-lead-create'),  # API for email leads
    path('form/', LeadFormView.as_view(), name='lead-form'),  # Server-rendered form
]