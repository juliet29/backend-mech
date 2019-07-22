from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending Service"), 
            (1, "Serviced")
        )

class ServiceRequest(models.Model):
    request_id = models.PositiveIntegerField("Request ID", primary_key=True)
    time_sent = models.DateTimeField(auto_now=False, auto_now_add=True) 
    location = models.CharField(max_length=64) 
    title = models.CharField(max_length=30)
    complaint = models.TextField("Complaint")
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)





