from django.shortcuts import render, redirect
from .models import User
from ..courses.models import Course, EnrollmentTable, Comment
from django.contrib import messages

# Create your views here.
def index(request):
	request.session['requestType'] = ''
	context = {
		'userList': User.objects.all(),
		'courseList': Course.objects.all(),
		'commentList': Comment.objects.all()
	}
	print (context)
	return render(request, 'loginReg/index.html', context)

def register(request):
	print ('THIS IS REGISTER IN VIEWS')
	if request.method == 'POST':
		model_response = User.objects.register(request.POST)
		#If it failed validation:
		if not model_response['status']:
			for error in model_response['errors']:
				messages.error(request, error)
			return redirect('login:index')
		#If it passed...
		else:
			request.session['user_id'] = model_response['user_id']
			request.session['requestType'] = 'registered'
			return redirect('login:success')
	else:
		print ("NO POST DATA")
		return redirect('login:index')

def login(request):
	model_response = User.objects.check_user(request.POST)
	if not 'user_id' in model_response:
		for error in model_response['errors']:
			messages.error(request, error)
		return redirect('login:index')
	else:
		request.session['requestType'] = 'logged in'
		request.session['user_id'] = model_response['user_id']
		return redirect('login:success')

def logout(request):
	request.session.clear()
	return redirect('login:index')

def success(request):
	if not 'user_id' in request.session:
		messages.error(request, "You aren't logged in!")
		return redirect('login:index')
	else:
		context = {}
		user = User.objects.get(id=request.session['user_id'])
		context['first_name'] = user.first_name
		context['requestType'] = request.session['requestType']
	return render(request, 'loginReg/success.html', context)

def users_courses(request):
	user = User.objects.get(id=request.POST['user_id'])
	course = Course.objects.get(id=request.POST['course_id'])
	print ("This would match " + str(user.first_name) + " with " + str(course.title))
	EnrollmentTable.objects.create(user=user, course=course)
	messages.success(request, "User added to class.")
	return redirect('/')
