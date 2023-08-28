from .models import *
from django.forms import *

class contactForm(forms.Form):
    name = CharField(max_length=100)
    Email=EmailField(required=False)
    phone=IntegerField( required=False)
    des=Textarea()