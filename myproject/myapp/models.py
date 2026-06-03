from django.db import models

class Fashion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='fashion_items/', blank=True, null=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    complete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.contrib.auth.models import User

class PendingEmployee(User):
    class Meta:
        proxy = True
        verbose_name = 'Pending Employee'
        verbose_name_plural = 'Pending Employees'
