from django.contrib import admin
from .models import Client, Event

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Details", {"fields": ["name", "surname", "dob"]}),
        ("Contact", {"fields": ["phone", "email"]}),
        ("Administration", {"fields": ["advisor"]}),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Event)