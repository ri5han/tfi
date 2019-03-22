from django.forms import ModelForm
from .models import Application
from django.contrib.auth.models import User

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'