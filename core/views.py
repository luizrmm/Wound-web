from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, AnimalForm, MedidaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .models import Animal, MedidaAnimal
from django.contrib import messages

#view para o documento html de home
def home(request):
	return render(request, 'home.html')

#view de cálculo da área
@login_required
def paint_image(request):
	form = MedidaForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			messages.success(request, 'Medida salva com sucesso')
			return redirect('paint_image')
		else:
			messages.error(request, "Algo de inesperado ocorreu, por favor verifique todos os campos.")
	return render(request, 'paint_image.html', {'form': form})

@login_required
def list_animais(request):
	context = {'Animais' : Animal.objects.all()}
	return render(request, 'list_animais.html', context)

@login_required
def list_medidas(request, id):
	context = {'Medidas': MedidaAnimal.objects.filter(animal_da_medida_id=id)}
	return render(request, 'list_medidas.html', context)

#view de cadastro de usuário
def cadastro(request):
	form = RegistrationForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			messages.success(request, 'Usuário cadatrado com sucesso, faça seu login!')
			return redirect('home')
		else:
			messages.error(request, "Algo de inesperado ocorreu, por favor verifique todos os campos.")
	return render(request, 'cadastro.html', {'form': form})


@login_required
def cadastroAnimal(request):
	form = AnimalForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			messages.success(request, 'Animal cadastrado com sucesso')
			return redirect('home')
		else:
			messages.error(request, "Algo de inesperado ocorreu, por favor verifique todos os campos.")
	return render(request, 'cadastro_animal.html', {'form': form})

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



@login_required
def update_animal(request, id):
	animal = get_object_or_404(Animal, pk=id)
	form = AnimalForm(request.POST or None, request.FILES or None, instance=animal)

	if form.is_valid():
		form.save()
		return redirect('list_animais')

	return render(request, 'cadastro_animal.html', {'form': form})



@login_required
def delete_animal(request, id):
	animal = get_object_or_404(Animal, pk=id)
	form = AnimalForm(request.POST or None, request.FILES or None, instance=animal)

	if request.method == 'POST':
		animal.delete()
		return redirect('list_animais')

	return render(request, 'animal_delete.html', {'animal': animal})

@login_required
def detail_medida(request, id):
	medida_animal = MedidaAnimal.objects.get(id=id)
	return render(request, 'detail_medida.html', {'medida_animal': medida_animal})


@login_required
def delete_medida(request, id):
	medida_animal = MedidaAnimal.objects.get(id=id)
	form = MedidaForm(request.POST or None, request.FILES or None, instance=medida_animal)

	if request.method == 'POST':
		medida_animal.delete()
		return redirect('list_animais')

	return render(request, 'delete_medida.html', {'medida_animal': medida_animal})

	