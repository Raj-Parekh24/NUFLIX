from django import forms
from django.forms import fields
from .models import video

class video_form(forms.ModelForm):
    class Meta:
        model=video
        fields=("name", "subject","caption","video")