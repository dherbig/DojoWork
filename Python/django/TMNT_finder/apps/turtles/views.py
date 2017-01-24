from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'turtles/index.html')

def ninjaLocator(request, color=''):
	context = {}
	context['color'] = color
	print color
	print ("the dict is = " + str(context))
	return render(request, "turtles/ninjas.html", context)
