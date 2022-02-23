from django import forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='first name', max_length=50)
    email = forms.EmailField(label='email')