from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = [
            'full_name', 'dob', 'gender', 'phone', 'email', 'address', 'emergency_contact_name',
            'relationship', 'emergency_contact_phone', 'medical_conditions', 'allergies',
            'current_medications', 'previous_injuries', 'fitness_goals', 'fitness_level',
            'trainer_required', 'trainer_duration', 'trainer_fee', 'pay_now', 'admission_fee',
            'membership_type', 'start_date', 'payment_method', 'profile_image'
        ]
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_conditions': forms.Textarea(attrs={'class': 'form-control', 'style': ' height: 60px'}),
            'allergies': forms.TextInput(attrs={'class': 'form-control', 'style': ' height: 60px'}),
            'current_medications': forms.TextInput(attrs={'class': 'form-control', 'style': ' height: 60px'}),
            'previous_injuries': forms.TextInput(attrs={'class': 'form-control', 'style': ' height: 60px'}),
            'fitness_goals': forms.TextInput(attrs={'class': 'form-control', 'style': ''}),
            'fitness_level': forms.TextInput(attrs={'class': 'form-control', 'style': ''}),
            'membership_type': forms.TextInput(attrs={'class': 'form-control', 'style': ''}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': ''}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control', 'style': ''}),

            'trainer_required': forms.TextInput(attrs={'class': 'form-control'}),
            'trainer_duration': forms.TextInput(attrs={'class': 'form-control'}),
            'trainer_fee': forms.TextInput(attrs={'class': 'form-control'}),
            'pay_now': forms.TextInput(attrs={'class': 'form-control'}),
            'admission_fee': forms.TextInput(attrs={'class': 'form-control'}),
            
        }