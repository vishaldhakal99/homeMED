from .models import userProfile
from django.forms import ModelForm

class myForm(ModelForm):
    class Meta:
        model = userProfile
        fields = ['appontment_availablity_from', 'appontment_availablity_to']
