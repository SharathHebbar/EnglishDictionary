from django.shortcuts import render

# Create your views here.
from PyDictionary import PyDictionary


def index(request):
    return render(request, 'index.html')


def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)

    context = {
        'meaning': meaning,
        'synonyms': synonyms,
        'antonyms': antonyms
    }

    return render(request, 'word.html', context)
