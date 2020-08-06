from django import forms
from .models import image_container


class image_form(forms.ModelForm):
    img_content = forms.ImageField(required=True)
    img_style = forms.ImageField(required=True)

    class Meta:
        model = image_container
        fields = ('img_content', 'img_style')
