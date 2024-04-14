from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Create
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		return render(request,'home.html',{})
	return redirect('login')
	

def login_user(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user:
			login(request,user)
			messages.success(request,"Status : Logged In ")
			return redirect('home')
	return render(request,'login.html',{})

def logout_user(request):
	logout(request)
	messages.success(request,"Status : Logged Out ")
	return redirect('login')

def register(request):
	if request.method=='POST':
		form=Create(request.POST)
		if form.is_valid:
			try:
			 form.save()
			except:	
				messages.success(request,"Error : Password's Didn't Match or Your password did meet the requirements ")
				return redirect('register')
			messages.success(request,"Status : Please Login ")
			return redirect('login')
	return render(request,'register.html',{})

def room(request):
	return render(request,'room.html',{'name':request.user.username})

def joinroom(request):
	if request.method=='POST':
		roomid=request.POST['roomid']
		return redirect('/room/?roomID='+roomid)
	return render(request,'join_room.html',{})


