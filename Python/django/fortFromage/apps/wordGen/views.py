from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    return render(request, "wordGen/index.html")

def generate(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 1
    else:
        request.session['attempt'] += 1
    result = ''
    dict = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    for counter in range(13):
        result += random.choice(dict)
        counter += 1
    request.session['WOTD'] = result
    return redirect('/result', request)
