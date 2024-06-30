from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_picture = models.URLField(null=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    