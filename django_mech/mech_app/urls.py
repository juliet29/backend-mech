from rest_framework import routers
from .views import UserViewSet
from django.conf.urls import url, include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    #url(r'mech-app/', include('rest_framework.urls', namespace='rest_framework'))
]