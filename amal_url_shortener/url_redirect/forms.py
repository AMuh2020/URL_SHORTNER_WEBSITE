from django import forms

class urlForm(forms.Form):
    url = forms.URLField(label='Url:', max_length=100,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    
#did not use, use html form instead
class editShortUrlForm(forms.Form):
    editShortUrl = forms.CharField(label='',max_length=10)