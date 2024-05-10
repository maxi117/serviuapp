from django import forms
from serviuApp.models import Subsidio

class CreateSubsidioForm(forms.ModelForm):
    class Meta:
        model = Subsidio
        fields = '__all__'