from django.shortcuts import render, HttpResponse
# Create your views here.
def index(request):
    print ("*"*50)
    returrn render(request, 'first_app/index.html')
