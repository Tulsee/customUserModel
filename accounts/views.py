from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.http import HttpResponse
User = get_user_model()
def register(request):
	email="ramtulsi022@gmail.com"
	first_name='ramtulsi'
	last_name='Ghimire'
	password='123456'

	user= User.objects.create_user(email=email, first_name=first_name,last_name=last_name, password=password)
	user.save()
	return redirect('home')
def home(request):
	users = User.objects.filter(email=request.user.email)
	for user in users:
		print(user)
	return HttpResponse("<h1>Welcome</h1>")

def login(request):
	email="ramtulsi022@gmail.com"
	password='12345'

	user = auth.authenticate(email=email, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponse("<h1>You are login in</h1>")
	else:
		return HttpResponse("<h1>Error</h1>")

