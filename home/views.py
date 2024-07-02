from django.shortcuts import render, redirect
from .models import Admission
from .forms import AdmissionForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

def index(request):
    all_admissions = Admission.objects.filter(user=request.user)
    context = {
        "admissions": all_admissions
    }
    return render(request, "home.html", context)

def member(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        emergency_contact_name = request.POST.get("emergency_contact_name")
        relationship = request.POST.get("relationship")
        emergency_contact_phone = request.POST.get("emergency_contact_phone")
        medical_conditions = request.POST.get("medical_conditions")
        allergies = request.POST.get("allergies")
        current_medications = request.POST.get("current_medications")
        previous_injuries = request.POST.get("previous_injuries")
        fitness_goals = request.POST.get("fitness_goals")
        fitness_level = request.POST.get("fitness_level")
        membership_type = request.POST.get("membership_type")
        start_date = request.POST.get("start_date")
        payment_method = request.POST.get("payment_method")
        liability_waiver = request.POST.get("liability_waiver") == 'on'
        terms_conditions = request.POST.get("terms_conditions") == 'on'
        privacy_policy = request.POST.get("privacy_policy") == 'on'
        marketing_consent = request.POST.get("marketing_consent") == 'on'
        preferred_workout_times = request.POST.get("preferred_workout_times")
        referred_by = request.POST.get("referred_by")
        notes = request.POST.get("notes")

        admission = Admission(
            user=request.user,
            full_name=full_name,
            dob=dob,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            emergency_contact_name=emergency_contact_name,
            relationship=relationship,
            emergency_contact_phone=emergency_contact_phone,
            medical_conditions=medical_conditions,
            allergies=allergies,
            current_medications=current_medications,
            previous_injuries=previous_injuries,
            fitness_goals=fitness_goals,
            fitness_level=fitness_level,
            membership_type=membership_type,
            start_date=start_date,
            payment_method=payment_method,
            liability_waiver=liability_waiver,
            terms_conditions=terms_conditions,
            privacy_policy=privacy_policy,
            marketing_consent=marketing_consent,
            preferred_workout_times=preferred_workout_times,
            referred_by=referred_by,
            notes=notes
        )
        admission.save()
        messages.success(request, "Your Message has been sent")
        return redirect("home")

    return render(request, "add_member.html")


def search(request):
    search=request.GET["search"]
    if len(search)>80:
        all_admissions = Admission.objects.none()
    else:
        all_admissions_Name = Admission.objects.filter(full_name__icontains=search)
        all_admissions_PhoneNo = Admission.objects.filter(phone__icontains=search)
        all_admissions_Email = Admission.objects.filter(email__icontains=search)
        all_admissions = all_admissions_Name.union(all_admissions_PhoneNo,all_admissions_Email)
    context = {"admissions": all_admissions, "search":search}
    return render(request, "search.html", context)
    

def profile(request, admission_id):
    admission = get_object_or_404(Admission, id=admission_id, user=request.user)
    context = {
        'admission': admission
    }
    return render(request, 'profile.html', context)

def profile2(request):
    return render(request, 'profile2.html')


# def authentication(request):
#     return render(request, 'authentication.html')

@login_required
def edit_profile(request, pk):
    admission = get_object_or_404(Admission, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = AdmissionForm(request.POST, instance=admission)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated successfully.')
            return redirect('profile', admission_id=pk)  # Redirect to the profile detail page or another appropriate page
    else:
        form = AdmissionForm(instance=admission)
    
    return render(request, 'edit_profile.html', {'form': form, 'admission': admission})



@login_required
def delete_profile(request, pk):
    admission = get_object_or_404(Admission, pk=pk)
    if request.method == 'POST':
        admission.delete()
        messages.success(request, 'Profile has been deleted successfully.')
        return redirect('home')  # Redirect to the home page or another appropriate page
    return render(request, 'confirm_delete.html', {'admission': admission})