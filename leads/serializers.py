# Serializers for lead capture APIs
from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    # Serializer for creating and validating leads
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'message', 'source']
        read_only_fields = ['source']  # Source is set programmatically

    def validate_email(self, value):
        # Custom validation to ensure email is not already in use
        if Lead.objects.filter(email=value).exists():
            raise serializers.ValidationError("A lead with this email already exists.")
        return value

    def validate(self, data):
        # Ensure at least one of first_name, last_name, or company is provided
        if not (data.get('first_name') or data.get('last_name') or data.get('company')):
            raise serializers.ValidationError("At least one of first_name, last_name, or company is required.")
        return data