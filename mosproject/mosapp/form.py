from django import forms
from mosapp.models import register,email
class registerform(forms.ModelForm):
    class Meta:
        model=register
        fields='__all__'

class emailform(forms.ModelForm):
    class Meta:
        model=email
        fields='__all__'