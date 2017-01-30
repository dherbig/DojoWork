from django.shortcuts import render, redirect
from .models import Email
import re


# Create your views here.
def index(request):
	return render(request, 'emailVal/index.html')

def submit(request):
	if Email.emailManager.register(request.POST):
		request.session['errors'] = 0
		return redirect('/success')
	else:
		request.session['errors'] += 1
		return redirect('/')

def success(request):
	context = {
		"emailList" : Email.emailManager.all()
	}
	return render(request, 'emailVal/success.html', context)

def delete(request, id):
	Email.emailManager.get(id=request.GET['id']).delete()
	return redirect('/success')
