from django.db import models
from django.urls import reverse
from stream_django.activity import Activity
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    """docstring for Member."""

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250, blank=True)
    email_address = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self): # new
        return reverse('members:members_detail', args=[str(self.id)])

class Address(models.Model):
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL)

    
    def get_absolute_url(self): # new
        return reverse('members:address_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.street
    
class Membership(models.Model):
    is_active = models.BooleanField(default=True)
    is_donor = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    date_joined = date_created = models.DateField(auto_now_add=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL)
