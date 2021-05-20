from django import forms

from twitterClone.models import TweetModel


class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetModel
        fields = '__all__'

