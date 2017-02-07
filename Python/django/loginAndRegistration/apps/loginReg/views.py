from django.shortcuts import render, redirect
from .models import User
from .forms import RegForm, LoginForm
from django.contrib import messages
import bcrypt

# Create your views here.
# Loads the login page
def index(request):
	context = {}
	# Checks to see if anyone is logged in
	if 'user_id' in request.session:
		# Then you don't need to be here!  Move along!
		return redirect('loginReg:success')
	# Otherwise:
	else:
		# Generate and store the forms this page uses as arguments
		regForm = RegForm()
		logForm = LoginForm()
		# And pass them to the page using the context dictionary
		context['regForm'] = regForm
		context['logForm'] = logForm
	return render(request, 'loginReg/index.html', context)

# Attempts to register a new user
def register(request):
	if request.method == 'POST':
		print ("Method was POST")
		# Takes the data from the form and makes an object out of it. Commit = False prevents it from being saved so we can check it out before we save it.  The data is validated by .save, but we need to check if there's a user with the same email first.
		candidate = request.POST['email']
		# Take all the form data and store it (bind the form)
		bound_form = RegForm(request.POST)
		# Barf if the user is already registered
		if User.objects.filter(email=candidate):
			print ("Duplicate User!")
			messages.error(request, 'This account already exists')
			return redirect('loginReg:index')
		# If it really is a new email, we make an entry.  We check to see if the data is valid, which was determined when we bound the form.
		elif bound_form.is_valid():
			print(bound_form)
			bound_form=bound_form.save()
			print(bound_form)
			print("Bound Form is Valid?? I guess??")
			# Use bcrypt to hash the password
			print (bound_form.password)
			bound_form.password = bcrypt.hashpw(bound_form.password.encode(), bcrypt.gensalt())
			print (bound_form.password)
			# Create a new object based on the form data.
			bound_form.save()
			# Let the user know it worked
			messages.success(request, 'Registration Successful!')
			# Store the user's ID in session so other controller functions can look up the active user.
			request.session['user_id'] = bound_form.id
			return redirect('loginReg:success')
		# If the form data was invalid
		else:
			# Go to .errors and look at all of the places that errors could get sorted to. (e.g. first_name, dob, non_field_errors)
			for field in bound_form.errors:
				# If that section of the form has 1+ errors,
				if bound_form.errors[field]:
					# Report each error
					for error in bound_form.errors[error]:
						# By making an error flash message.
						messages.error(request, error2)
			print("Invalid Data on Forms")

	print ('Final Else Statement')
	return redirect('loginReg:index')

def login(request):
	# Grab the login form data and store it for easy reference
	bound_form = LoginForm(request.POST).save(commit=False)
	# Check to see in the email corresponds to a User
	try:
		# Get User from database by email
		loginTest = User.objects.get(email=bound_form.email)
		# Check to see if the User's passord matches the form's password entry
		if bcrypt.hashpw(bound_form.password.encode(), loginTest.password.encode()) == loginTest.password:
			# Stores the User's ID for future reference
			request.session['user_id'] = loginTest.id
			# Success
			messages.success(request, 'You are now logged in.')
			return redirect('loginReg:success')
		else:
			# Password mismatch
			messages.error(request, 'Passwords do not match')
	# If you can't find a User for the entered email:
	except User.DoesNotExist:
		messages.error(request, 'No such user!')
	# If your query returns more than one User object for the email entered:
	except User.MultipleObjectsReturned:
		messages.error(request, 'Database Error: There are two entries for that email address. PURGE!')
	# If things didn't work, reload the page.
	return redirect('loginReg:index')

def logout(request):
	# Clear all session data
	request.session.clear()
	return redirect('loginReg:index')

def success(request):
	# If there's no stored user_id value in session:
	if not 'user_id' in request.session:
		messages.error(request, "You aren't logged in!")
		# Something went wrong, so return to the login page.
		return redirect('loginReg:index')
	# Make a context dictionary the page can work with
	context = {}
	context['user'] = User.objects.get(id=request.session['user_id'])
	# And pass it to the page you render.
	return render(request, 'loginReg/success.html', context)
