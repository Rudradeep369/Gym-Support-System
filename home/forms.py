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
            'referred_by', 'notes'
        ]
