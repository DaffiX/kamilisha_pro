from django.contrib import admin

# Register your models here.
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'department', 'phone_number', 'subscribe_date')
    list_filter = ('department', 'subscribe_date')
    search_fields = ('first_name', 'department', 'phone_number')

admin.site.register(Subscriber, SubscriberAdmin)
