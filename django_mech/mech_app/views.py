from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import ServiceRequest
from django.contrib.auth.models import User
from .serializers import ServiceRequestSerializer, UserSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import AllowAny


# views for the users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_permission(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.ation == 'update' or self.action == 'partial_update':
    #         permission_classes = IsLoggedInUserOrAdmin
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]




# order service requests by time sent in from most recent to least recent
class ServiceRequestAPIView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.order_by('-time_sent')
    serializer_class = ServiceRequestSerializer

# just a landing page for us to come back to
def index(request):
    complaints = ServiceRequest.objects.values_list('complaint', flat=True)
    context = {'complaints': complaints}
    return render(request, 'mech_app/index.html', context)




