from django import forms
from .models import User
from django.contrib import messages
BIRTH_YEARS = list(range(1940, 2017))
# Creates a login form that asks for a User's email and password
class LoginForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['email', 'password']

# Creates a registration form that makes new Users
class RegForm(forms.ModelForm):
	# Since most of this form is assembled automatically using ModelForm tricks, these first two lines make sure the password and confirm_password fields hide their entries.
	password=forms.CharField(widget=forms.PasswordInput())
	confirm_password=forms.CharField(widget=forms.PasswordInput())
	dob=forms.DateField(
		widget=forms.SelectDateWidget(
			years=(BIRTH_YEARS)
		)
	)
	# This section looks at the User model and makes fields for each of the stated values.
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'dob', 'password']

	# This overrides (and includes) the ModelForm's clean function, which validates data, so that I can check password authenticity using bcrypt
	def clean(self):
		# This runs the inheritied .clean()
		cleaned_data = super(RegForm, self).clean()

		# Snags the entered password
		password = cleaned_data.get("password")
		# Snags the confirm password input
		confirm_password = cleaned_data.get("confirm_password")
		# Checks to see if the two passwords match
		if password and password != confirm_password:
			raise forms.ValidationError("Password fields do not match!")
			messages.error(request, "Passwords do not match!")
			print('We just put up an error message...')
		# Now, when we run .clean() on registration forms, it will also check to make sure the entered passwords match.
		return self.cleaned_data
