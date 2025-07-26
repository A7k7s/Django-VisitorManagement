from django.db import models

from visform.models import Visitor

class ApprovedVisitor(models.Model):
    visitor = models.OneToOneField(Visitor, on_delete=models.CASCADE)
    approved_at = models.DateTimeField(auto_now_add=True)

class RejectedVisitor(models.Model):
    visitor = models.OneToOneField(Visitor, on_delete=models.CASCADE)
    rejected_at = models.DateTimeField(auto_now_add=True)

class RescheduledVisitor(models.Model):
    visitor = models.OneToOneField(Visitor, on_delete=models.CASCADE)
    new_date = models.DateField()
    new_time = models.TimeField()
    rescheduled_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
