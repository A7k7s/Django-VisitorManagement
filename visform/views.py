from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Visitor

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        category = request.POST.get('category')
        designation = request.POST.get('designation')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')
        document = request.FILES.get('document')  # Optional

        visitor = Visitor(
            name=name,
            email=email,
            category=category,
            designation=designation,
            phone=phone,
            date=date,
            time=time,
            reason=reason,
            document=document
        )
        visitor.save()
        
        if designation == 'HOD':
            recipient = 'akshayaapaneer7@gmail.com'
        elif designation == 'Associate Professor':
            recipient = 'akshayaapanneerselvam@gmail.com'
        elif designation == 'Assistant Professor':
            recipient = 'akshayaaselvam7@gmail.com'
        # Send email to visitor
        send_mail(
            subject="Your response has been submitted",
            message=f"Hi {name},\nYour response has been successfully submitted.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        # Send email to admin
        send_mail(
            subject="An appointment has been requested",
            message=f"{name} has submitted an appointment request.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],  # replace with actual
            fail_silently=False,
        )

        return render(request, 'vform.html', {'success': True})

    return render(request, 'vform.html')

# Create your views here.
