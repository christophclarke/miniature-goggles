from django import forms
from malsearch.models import SampleComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = SampleComment
        fields = ['sample', 'user', 'comment']
        widgets = {
            'sample': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }
