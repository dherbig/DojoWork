from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    request.session["name"] = request.POST['name']
    request.session["location"] = request.POST['location']
    request.session["language"] = request.POST['language']
    request.session["comment"] = request.POST['comment']
    return redirect('/results')

def results(request):
    print request.session['name']
    return render(request, 'survey/results.html')
