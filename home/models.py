from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

def get_default_user():
    return User.objects.get(pk=1)  # Replace 1 with the ID of your default user

class Admission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)

    profile_image=models.ImageField(null=True,blank=True,upload_to="images/")

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

    trainer_required = models.CharField(max_length=80, blank=True, null=True)
    trainer_duration = models.CharField(max_length=50, blank=True, null=True)
    trainer_fee = models.CharField(max_length=50,blank=True, null=True)
    pay_now = models.CharField(max_length=50, blank=True, null=True)
    admission_fee = models.CharField(max_length=50,blank=True, null=True)

    

    def __str__(self):
        return self.full_name


class Receipt(models.Model):
    date = models.DateField()
    slno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    admission_fee = models.ImageField()
    personal_trainer_fee = models.ImageField()
    multi_gym = models.BooleanField(default=False)
    zumba = models.BooleanField(default=False)
    yoga = models.BooleanField(default=False)
    gym_type_fee = models.ImageField()
    total_amount = models.ImageField()
    in_words = models.CharField(max_length=255)
    next_payment_date = models.DateField()

    def __str__(self):
        return f"Receipt {self.slno} - {self.name}"