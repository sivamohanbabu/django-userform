from .models import User
from django import forms

class Userregister(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name","email","password","cpassword"]