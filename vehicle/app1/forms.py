from django import forms
from app1.models import Vehicle
class VForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=('Vehicle_Name','Brand','Color','Milage','Image')