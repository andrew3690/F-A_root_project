from django import forms
from .models import Run

class RegisterRun(forms.ModelForm):
    class Meta:
        model= Run
        fields = "__all__"
