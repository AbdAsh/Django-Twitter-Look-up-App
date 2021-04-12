from django import forms
from twitterlookup.models import options

class SortForm(forms.ModelForm):
    class Meta:
        model = options
        fields = '__all__'