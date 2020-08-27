from django.contrib import admin

# Register your models here.
from .models import UserAccount,ConsumerProfile

admin.site.register(UserAccount)
admin.site.register(ConsumerProfile)