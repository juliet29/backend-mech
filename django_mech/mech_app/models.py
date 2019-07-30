from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS = ((0, "Pending"), 
            (1, "Ongoing"),
            (2, "Completed")
        )

class ServiceRequest(models.Model):
    request_id = models.PositiveIntegerField("Request ID", primary_key=True)
    time_sent = models.DateTimeField(auto_now=False, auto_now_add=True) 
    location = models.CharField(max_length=64) 
    title = models.CharField(max_length=30)
    complaint = models.TextField("Complaint")
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    departments = models.TextField("Department", default="[Mechanical, Process]")
    plant = models.CharField(max_length=20, default="Mudor")
    status = models.PositiveSmallIntegerField(choices=STATUS, default=0)

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()

@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, **kwargs):
    if created:
        UserDetails.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.UserDetails.save()






