
from django.db import models

class Visitor(models.Model):
    CATEGORY_CHOICES = [
        ('Parent', 'Parent'),
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('General', 'General'),
    ]

    DESIGNATION_CHOICES = [
        ('HOD', 'HOD'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
    ]
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ('rescheduled', 'Rescheduled'),
        ],
        default='pending')

    name = models.CharField(max_length=100)
    email = models.EmailField()
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    designation = models.CharField(max_length=30, choices=DESIGNATION_CHOICES)
    phone = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.date} {self.time})"

# Create your models here.
