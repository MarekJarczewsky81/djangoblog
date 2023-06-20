from django import forms
from .models import Post


class ImgForm(forms.Form):
    class Meta:
        model = Post
        fields = ['image']