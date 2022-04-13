from audioop import reverse
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

class Client(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    dob = models.DateField("date of birth")
    email = models.EmailField()
    phone = PhoneNumberField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class Event(models.Model):
    title = models.CharField('Event Name', max_length=128)
    description = models.TextField(blank=True)
    address = models.CharField('Event Address', max_length=128, blank=True)
    start_date = models.DateTimeField('Start Date', default=datetime.now())
    end_date = models.DateTimeField('End Date', default=datetime.now())
    

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('main:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'