from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	request.session['requestType'] = ''
	return render(request, 'loginReg/index.html')

def register(request):
	if request.method == 'POST':
		model_response = User.objects.register(request.POST)
		#If it failed validation:
		if not model_response['status']:
			for error in model_response['errors']:
				messages.error(request, error)
			return redirect('users:index')
		#If it passed...
		else:
			request.session['user_id'] = model_response['user_id']
			request.session['requestType'] = 'registered'
			return redirect('users:success')
	else:
		return redirect('users:index')

def login(request):
	model_response = User.objects.check_user(request.POST)
	if not 'user_id' in model_response:
		for error in model_response['errors']:
			messages.error(request, error)
		return redirect('users:index')
	else:
		request.session['requestType'] = 'logged in'
		request.session['user_id'] = model_response['user_id']
		return redirect('users:success')

def logout(request):
	request.session.clear()
	return redirect('users:index')

def success(request):
	if not 'user_id' in request.session:
		messages.error(request, "You aren't logged in!")
		return redirect('users:index')
	else:
		context = {}
		user = User.objects.get(id=request.session['user_id'])
		context['first_name'] = user.first_name
		context['requestType'] = request.session['requestType']
	return render(request, 'loginReg/success.html', context)
