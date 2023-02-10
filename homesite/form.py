from django.forms import ModelForm
from .models import  Review



class reviewForm(ModelForm):
    

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['user']
