from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

def get_default_user():
    return User.objects.get(pk=1)  # Replace 1 with the ID of your default user

class Admission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)

    # profile_image=models.ImageField(null=True,blank=True,upload_to="images/")

    full_name = models.CharField(max_length=80)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    emergency_contact_name = models.CharField(max_length=80)
    relationship = models.CharField(max_length=20)
    emergency_contact_phone = models.CharField(max_length=15)

    medical_conditions = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    current_medications = models.TextField(blank=True, null=True)
    previous_injuries = models.TextField(blank=True, null=True)
    fitness_goals = models.TextField(blank=True, null=True)
    fitness_level = models.CharField(max_length=50)

    membership_type = models.CharField(max_length=50)
    start_date = models.DateField()
    payment_method = models.CharField(max_length=50)

    liability_waiver = models.BooleanField(default=False)
    terms_conditions = models.BooleanField(default=False)
    privacy_policy = models.BooleanField(default=False)
    marketing_consent = models.BooleanField(default=False)

    preferred_workout_times = models.CharField(blank=True, null=True,max_length=80)
    referred_by = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    

    def __str__(self):
        return self.full_name