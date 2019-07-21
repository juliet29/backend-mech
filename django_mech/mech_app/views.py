from django.shortcuts import render
from rest_framework import generics, routers, viewsets
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer, UserSerializer
from django.contrib.auth.models import User
from django.conf.urls import url, include

# Create your views here.
class ServiceRequestAPIView(generics.ListCreateAPIView):
    # queryset = ServiceRequest.objects.all()
    # order by time sent in from most recent to least recent
    queryset = ServiceRequest.objects.order_by('-time_sent')
    serializer_class = ServiceRequestSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (AllowAny,)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def index(request):
    complaints = ServiceRequest.objects.values_list('complaint', flat=True)
    context = {'complaints': complaints}
    return render(request, 'mech_app/index.html', context)




