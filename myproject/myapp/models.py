from django.db import models

class Fashion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='fashion_items/', blank=True, null=True)

    def __str__(self):
        return self.title


