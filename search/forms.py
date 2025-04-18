from django import forms
class EmojiSearchForm(forms.Form):
    query=forms.CharField(label='Enter a word', max_length=100)