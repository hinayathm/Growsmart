from django.forms import ModelForm

from .models import *


class Adduser_form(ModelForm):
    class Meta:
        model = User_model
        fields = ('Name', 'Email', 'Phone_no')

class Addproduct_form(ModelForm):
    class Meta:
        model = Product_model
        fields = ('Product_name', 'Quantity','Price','Image','details')

class Addseed_form(ModelForm):
    class Meta:
        model = manageseeds_model
        fields=('Seed_name','seed_image','Tempurature','Humidity','Moisture')