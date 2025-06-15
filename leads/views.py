# Views for lead capture APIs
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LeadSerializer
from .tasks import send_lead_notification

class LeadCreateAPIView(APIView):
    # API view for creating leads from forms
    def post(self, request):
        # Set source to website_form
        data = request.data.copy()
        data['source'] = 'website_form'

        # Validate and save lead
        serializer = LeadSerializer(data=data)
        if serializer.is_valid():
            lead = serializer.save()
            # Trigger async notification task
            send_lead_notification.delay(lead.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailLeadCreateAPIView(APIView):
    # API view for creating leads from emails
    def post(self, request):
        # Set source to email
        data = request.data.copy()
        data['source'] = 'email'

        # Validate and save lead
        serializer = LeadSerializer(data=data)
        if serializer.is_valid():
            lead = serializer.save()
            # Trigger async notification task
            send_lead_notification.delay(lead.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)