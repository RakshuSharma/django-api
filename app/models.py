from django.db import models
from django.utils import timezone
# Create your models here.,

class Contact(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=200)
    created_at=models.DateTimeField(default=timezone.now)

