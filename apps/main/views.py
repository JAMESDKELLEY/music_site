from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
	return render (request, 'main/index.html')

def about(request):
	return render (request, 'main/about.html')

def music(request):
	return render (request, 'main/music.html')

def press(request):
	return render (request, 'main/press.html')

def contact_booking(request):
	return render (request, 'main/contact.html')

def upcoming_dates(request):
	return render (request, 'main/upcoming.html')

def subscribe(request):
	if Subscriber.objects.validate(request.POST):

		Subscriber.objects.create (
			email = request.POST.get("email"))
		messages.success(request,'Thanks for supporting techno!')
		return redirect("/")
	else:
		messages.error(request,'Invalid Email')
		return redirect('/')

def subscribe2(request):
	if Subscriber.objects.validate(request.POST):

		Subscriber.objects.create (
			email = request.POST.get("email"))
		messages.success(request,'Thanks for supporting techno!')
		return redirect("/about")	
	else:
		messages.error(request,'Invalid Email')
		return redirect('/about')

def subscribe3(request):
	if Subscriber.objects.validate(request.POST):

		Subscriber.objects.create (
			email = request.POST.get("email"))
		messages.success(request,'Thanks for supporting techno!')
		return redirect("/music")	
	else:
		messages.error(request,'Invalid Email')
		return redirect('/music')

def subscribe4(request):
	if Subscriber.objects.validate(request.POST):

		Subscriber.objects.create (
			email = request.POST.get("email"))
		messages.success(request,'Thanks for supporting techno!')
		return redirect("/press")	
	else:
		messages.error(request,'Invalid Email')
		return redirect('/press')

def subscribe5(request):
	if Subscriber.objects.validate(request.POST):

		Subscriber.objects.create (
			email = request.POST.get("email"))
		messages.success(request,'Thanks for supporting techno!')
		return redirect("/upcoming_dates")	
	else:
		messages.error(request,'Invalid Email')
		return redirect('/upcoming_dates')

def subscribe6(request):
	if Subscriber.objects.validate(request.POST):

		Subscriber.objects.create (
			email = request.POST.get("email"))
		messages.success(request,'Thanks for supporting techno!')
		return redirect("/contact_booking")	
	else:
		messages.error(request,'Invalid Email')
		return redirect('/contact_booking')


