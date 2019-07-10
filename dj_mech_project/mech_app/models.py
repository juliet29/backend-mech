from django.db import models

# Create your models here.
class ServiceRequest(models.Model):
    request_id = models.PositiveIntegerField("Request ID", primary_key=True)
    sender = models.CharField(max_length=128)
    time_sent = models.DateTimeField(auto_now=False, auto_now_add=True) # timestamp of time the service request was created
    location = models.CharField(max_length=64) # will need to update to make one of few options ...
    complaint = models.TextField("Complaint")

