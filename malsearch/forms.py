from django import forms
from malsearch.models import SampleComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = SampleComment
        fields = ['comment']