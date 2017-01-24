from django.shortcuts import render, redirect
import re


# Create your views here.
def index(request, errors = 0):
	context = {}
	context['isHidden'] =  'hidden'
	return render(request, 'emailVal/index.html', context)

def submit(request):
	ettempt = request.POST['address']
	if EMAIL_REGEX.match(ettempt):
		Email.objects.create(address=ettempt)
	else:
		return redirect('/', 1)

	return redirect(request, '/success')


def success(request):
	context = {
		"emailList" : Email.objects.all()
	}
	return render(request, 'emailVal/success.html')
