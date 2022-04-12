from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    dob = models.DateField("date of birth")
    email = models.EmailField()
    phone = PhoneNumberField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class Event(models.Model):
    event = models.CharField('Event Name', max_length=128)
    event_date = models.DateTimeField('Event Date')
    address = models.CharField('Event Address', max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name