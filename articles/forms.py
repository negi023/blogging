from .models import Articles
from django import forms


class Writeform(forms.ModelForm):
    thumb = forms.ImageField(label='Image')

    class Meta:
        model = Articles
        fields = (
            'title',
            'body',
            'thumb',
            'category'
        )

