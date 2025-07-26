from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from visform.models import Visitor
from .models import ApprovedVisitor, RejectedVisitor, RescheduledVisitor
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('appointments')  # redirect to dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


def custom_logout(request):
    logout(request)
    return redirect('login')

def appointments_view(request):
    # Only show pending appointments
    appointments = Visitor.objects.filter(status='pending').order_by('-submitted_at')
    return render(request, 'appoinment.html', {'appointments': appointments})

def approve_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)
    ApprovedVisitor.objects.create(visitor=visitor)

    # Update status instead of deleting
    visitor.status = 'approved'
    visitor.save()

    send_mail(
        subject="Your appointment is approved",
        message=f"Hi {visitor.name}, your appointment request has been approved.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[visitor.email],
        fail_silently=False
    )
    return redirect('appointments')

def reject_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)
    RejectedVisitor.objects.create(visitor=visitor)

    visitor.status = 'rejected'
    visitor.save()

    send_mail(
        subject="Your appointment is rejected",
        message=f"Hi {visitor.name}, your appointment request has been rejected.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[visitor.email],
        fail_silently=False
    )
    return redirect('appointments')

def reschedule_form(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)

    if request.method == 'POST':
        new_date = request.POST.get('new_date')
        new_time = request.POST.get('new_time')

        # Save in rescheduled table
        RescheduledVisitor.objects.create(
            visitor=visitor,
            new_date=new_date,
            new_time=new_time
        )

        # Update status in Visitor model
        visitor.status = 'rescheduled'
        visitor.save()

        # Send email to user
        send_mail(
            subject="Your appointment is rescheduled",
            message=f"Hi {visitor.name}, your appointment has been rescheduled to {new_date} at {new_time}.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[visitor.email],
            fail_silently=False
        )

        return redirect('appointments')

    return render(request, 'r-form.html', {'visitor': visitor})

def approved_view(request):
    approved = ApprovedVisitor.objects.select_related('visitor')
    return render(request, 'approved.html', {'approved': approved})

def rejected_view(request):
    rejected = RejectedVisitor.objects.select_related('visitor')
    return render(request, 'rejected.html', {'rejected': rejected})

def rescheduled_view(request):
    rescheduled = RescheduledVisitor.objects.select_related('visitor')
    return render(request, 'reschedule.html', {'rescheduled': rescheduled})
