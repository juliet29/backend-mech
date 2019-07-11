from django.shortcuts import render
from rest_framework import generics
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

# Create your views here.
class ServiceRequestAPIView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

def index(request):
    complaints = ServiceRequest.objects.order_by('complaint')
    context = {'complaints': complaints}
    return render(request, 'mech_app/index.html', context)
