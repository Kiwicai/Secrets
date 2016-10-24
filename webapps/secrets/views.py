from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from secrets.models import *
from django.utils import timezone

@transaction.atomic
def register(request):
	context = {}

	if request.method == 'GET':
		form = UserCreationForm()
		context['form'] = form
		return render(request, 'register.html', context)

	newUser = User()
	form = UserCreationForm(request.POST, instance=newUser)

	if not form.is_valid():
		context['form'] = form
		return render(request, 'register.html', context)

	form.save()
	newUser.is_active = True
	login(request, newUser)

	return redirect('mySecrets')

@login_required
def mySecrets(request):
	context ={}

	if request.method == 'POST' and 'newPost' in request.POST and request.POST['newPost'] and len(request.POST['newPost']) <= 500:
		newSecret = Secret(content=request.POST['newPost'], postDate=timezone.now(), user=request.user)
		newSecret.save()

	secrets = Secret.objects.filter(user=request.user).order_by('-postDate') # User could only see his/her own secrets
	context['secrets'] = secrets
	context['user'] = request.user
	return render(request, 'mySecrets.html', context)

@login_required
def deleteSecret(request):
	context ={}
	# TODO
	return render(request, 'mySecrets.html', context)

@login_required
def updateSecret(request):
	# TODO
	context ={}
	return render(request, 'mySecrets.html', context)