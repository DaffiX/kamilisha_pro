from django.db import models

# Create your models here.
class Subscriber(models.Model):
    first_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    # agree_to_subscribe = models.BooleanField(default=False)
    subscribe_date = models.DateTimeField(auto_now_add=True)
