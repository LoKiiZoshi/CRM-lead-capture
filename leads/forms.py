# Django forms for lead capture
from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    # Form for capturing lead data from website
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),  # Textarea for message field
        }

    def clean_email(self):
        # Validate email uniqueness
        email = self.cleaned_data['email']
        if Lead.objects.filter(email=email).exists():
            raise forms.ValidationError("A lead with this email already exists.")
        return email