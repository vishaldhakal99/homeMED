from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="users")
    is_patient = models.BooleanField('patient status', default=False)
    is_doctor = models.BooleanField('doctor status', default=False)
    info = models.TextField(blank=True,null=True)
    profile_photo = models.ImageField(blank=True,null=True)
    cover_photo = models.ImageField(blank=True,null=True)
    appontment_availablity_from = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    appontment_availablity_to = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    rate_per_hour = models.IntegerField(blank=True,null=True)

class appoint(models.Model):
    doctor = models.ForeignKey(userProfile,on_delete=models.CASCADE,related_name="doct")
    pate = models.ForeignKey(userProfile,on_delete=models.CASCADE,related_name="pate")
    time_from = models.DateTimeField(auto_now=False,auto_now_add=False)
    time_to = models.DateTimeField(auto_now=False,auto_now_add=False)
    


