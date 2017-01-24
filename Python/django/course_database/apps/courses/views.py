from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
	context = {
		"courseList": Course.objects.all()
	}
	print context
	return render(request, "courses/index.html", context)

def submit(request):
	Course.objects.create(title=request.POST["title"], description=request.POST["description"])
	return redirect('/')

def confirm(request, id):
	details = Course.objects.get(id=id)
	context = {}
	context['courseId'] = details.id
	context['courseTitle'] = details.title
	context['courseDescription'] = details.description
	return render(request, "courses/destroy.html", context)

def delete(request, id):
	Course.objects.get(id=id).delete()
	return redirect('/')
