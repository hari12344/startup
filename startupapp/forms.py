from django.forms import ModelForm
from .models import Registration

class registraionForm(ModelForm) :
    class Meta:
        model = Registration
        fields = '__all__'