from django.contrib import admin
from .models import UserProfile,History,Request,Interact
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(History)
admin.site.register(Request)
admin.site.register(Interact)