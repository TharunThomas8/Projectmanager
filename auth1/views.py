from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.template import RequestContext
from django.contrib import messages
from .forms import SignUpForm,EditProfileForm,ProfileForm
from .models import Profile
from datetime import date
from cards.models import Cards

# Create your views here.
def home(request):
	# print (request)
	cards = Cards.objects.all()		#gets all the cards
	today = date.today()	#get's today's date to check if over due
	return render(request,'home.html',{'cards':cards,'today':today})	#renders with data
def login_user(request):
	if request.method =='POST':		#sends a POST request and receives the username and password
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)		#checks if user exists
		if user is not None:	#if exists logs in
			login(request, user)
			messages.success(request,('you have been logged in'))
			return redirect('home')
		else:		#else error page is shown
			messages.success(request,('Error login in log in with valid username..'))
			return redirect('login')
	else:		#login page is rendered
		return render(request,'login.html',{})

def logout_user(request):
    logout(request)	
    messages.success(request,('you ave been successfully Logged Out'))
    return redirect('home')	
def register_user(request):
	if request.method =='POST':		#POST request is send to retrieve the data of the user in a form structure defined in forms.py
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()		
			username = form.cleaned_data['username']   
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)		#is added to the DB and logged in
			login(request, user)
			messages.success(request,('you have been successfully registered in'))
			return redirect('home')			
	else:
		form = SignUpForm()
	context={'form':form}
	return render(request,'register.html',context)		#renders the page with the form to retrive the data




