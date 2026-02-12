from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .forms import BookingForm

from .models import Department, Doctors


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Email content
            subject = f'New Appointment Booking - {booking.p_name}'
            message = f'''
            A new booking has been made:

            Name: {booking.p_name}
            Phone: {booking.p_phone}
            Email: {booking.p_email}
            Doctor: {booking.doc_name}
            Date: {booking.booking_date}
            '''

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,        # From email
                ['arshadarshaz135@gmail.com'],     # To email(s)
                fail_silently=False,
            )

            return render(request, 'confirmation.html') # or some success page
    else:
        form = BookingForm()
    return render(request,'booking.html', {'form': form})

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept = {
        'dept': Department.objects.all()
    }
    return render(request,'department.html', dict_dept)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html', dict_docs)