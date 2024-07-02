from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = [
            'full_name', 'dob', 'gender', 'phone', 'email', 'address', 'emergency_contact_name',
            'relationship', 'emergency_contact_phone', 'medical_conditions', 'allergies',
            'current_medications', 'previous_injuries', 'fitness_goals', 'fitness_level',
            'membership_type', 'start_date', 'payment_method', 'liability_waiver',
            'terms_conditions', 'privacy_policy', 'marketing_consent', 'preferred_workout_times',
            'referred_by', 'notes', 'profile_image'
        ]
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 50%;'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 50%;'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_conditions': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 70%; height: 60px'}),
            'allergies': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 70%; height: 60px'}),
            'current_medications': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 70%; height: 60px'}),
            'previous_injuries': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 70%; height: 60px'}),
            'fitness_goals': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 70%;'}),
            'fitness_level': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 70%;'}),
            'membership_type': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 70%;'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 70%;'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 70%;'}),
            'liability_waiver': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'terms_conditions': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'privacy_policy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'marketing_consent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'preferred_workout_times': forms.TextInput(attrs={'class': 'form-control'}),
            'referred_by': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            
        }