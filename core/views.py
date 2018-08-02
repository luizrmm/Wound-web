from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

#view para o documento html de home
def home(request):
	return render(request, 'home.html')

#view de cálculo da área
@login_required
def paint_image(request):
	return render(request, 'paint_image.html')

#view de cadastro
def cadastro(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, 'cadastro.html', {'form': form})

#view de login
def my_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('home')
	return render(request, 'login.html')

#view de logout
def my_logout(request):
	logout(request)
	return redirect('home')