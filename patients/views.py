from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Patient
from .forms import PatientForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PatientSerializer

def welcome(request):
    return render(request, 'patients/welcome.html')

def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            subject=f'Contact Us message from {name}',
            message=message + f"\n\nFrom: {name} <{email}>",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )
        success = True

    return render(request, 'patients/contact.html', {'success': success})

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        patient_form = PatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserCreationForm()
        patient_form = PatientForm()
    return render(request, 'patients/register.html', {'user_form': user_form, 'patient_form': patient_form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'patients/login.html', {'form': form})

@login_required
def home(request):
    patient = get_object_or_404(Patient, user=request.user)
    return render(request, 'patients/home.html', {'patient': patient})

@login_required
def edit_report(request):
    patient = get_object_or_404(Patient, user=request.user)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/edit_report.html', {'form': form})

def user_logout(request):
    django_logout(request)
    return redirect('login')

@login_required
def patient_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    patient = get_object_or_404(Patient, user=user)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patient_api(request):
    patient = get_object_or_404(Patient, user=request.user)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)

# Chatbot View
def chatbot(request):
    return render(request, 'patients/chatbot.html')
