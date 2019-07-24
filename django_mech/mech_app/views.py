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

    def get_queryset(self):
        """
        Optionally restricts the returned users to a username given by the front end 
        """
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username__iexact=username)
        return queryset



# order service requests by time sent in from most recent to least recent
class ServiceRequestAPIView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.order_by('-time_sent')
    serializer_class = ServiceRequestSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned service request to an id passed by the front end 
        """
        queryset = ServiceRequest.objects.order_by('-time_sent')
        author = self.request.query_params.get('author', None)
        request_id = self.request.query_params.get('request_id', None)

        if author is not None:
            queryset = queryset.filter(author=author)
        
        if request_id is not None:
            queryset = queryset.filter(request_id=request_id)

        return queryset

class EditServiceRequestAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    lookup_url_kwarg = 'request_id'
    serializer_class = ServiceRequestSerializer
    

    def get_queryset(self):
        """
        Optionally restricts the returned service request to an id passed by the front end 
        """
        queryset = ServiceRequest.objects.order_by('-time_sent')
        request_id = self.request.query_params.get('request_id', None)
        
        if request_id is not None:
            queryset = queryset.filter(request_id=request_id)

        return queryset


# just a landing page for us to come back to
def index(request):
    complaints = ServiceRequest.objects.values_list('complaint', flat=True)
    context = {'complaints': complaints}
    return render(request, 'mech_app/index.html', context)




