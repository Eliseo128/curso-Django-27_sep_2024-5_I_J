from django import forms
from .models import Templeado

class empleadoappform(forms.Form):
    nombre=forms.CharField()
    url=forms.URLField()
    
class EmpleadoappModelForm(forms.ModelForm):
    class Meta:
        model=Templeado
        fields='__all__' # ['nombre']