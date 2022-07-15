from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client, Event


# Extension of UserCreationForm 
# that adds email field to the user

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_date': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_date': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_date'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_date'].input_formats = ('%Y-%m-%dT%H:%M',)

class NewClientForm(forms.ModelForm):
  class Meta:
    model = Client
    widgets = {
      'dob': forms.DateInput(attrs={'type': 'date'}, format='%d/%M/%Y'),
      'advisor': forms.HiddenInput(),
      'phone': forms.TextInput(attrs={'placeholder': 'Must be in format +44 1234 567 890'})
    }
    fields = ["name","surname","dob","phone","email"]