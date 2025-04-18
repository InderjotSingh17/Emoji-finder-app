from django.shortcuts import render
from django import forms
import emoji

class EmojiSearchForm(forms.Form):
    query = forms.CharField(label='Search for an emoji', max_length=100)

def search_emoji(request):
    form = EmojiSearchForm()
    results = []

    if request.method == 'POST':
        form = EmojiSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'].lower()

            for alias in emoji.EMOJI_UNICODE_ENGLISH:
                cleaned = alias.strip(':').replace('_', ' ').lower()
                if query in cleaned:
                    emoji_char = emoji.emojize(alias)
                    results.append((emoji_char, alias))

    return render(request, 'search.html', {'form': form, 'results': results})
