from django.contrib import admin
from .models import users, userDetails

# Register your models here.
admin.site.register(users)
admin.site.register(userDetails)