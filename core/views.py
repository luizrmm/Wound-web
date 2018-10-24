from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, EquinoForm, BovinoForm, EquinoImagemForm, BovinoImagemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .models import Bovino, Equino, MedidaEquino, MedidaBovino

#view para o documento html de home
def home(request):
	return render(request, 'home.html')

#view que permite o usuário selecionar a espécie de animal
def Especie(request):
	return render(request, 'Especie_animal.html')

#view de cálculo da área
@login_required
def paint_image(request):
	return render(request, 'paint_image.html')

@login_required
def list_bovinos(request):
	context = {'Bovinos' : Bovino.objects.all()}
	return render(request, 'list_bovinos.html', context)

@login_required
def list_equinos(request):
	context = {'Equinos': Equino.objects.all()}
	return render(request, 'list_equinos.html', context)

@login_required
def list_medidasEquinos(request, id):
	context = {'MedidasEquino': MedidaEquino.objects.filter(animal_da_medida_id=id)}
	return render(request, 'list_medidas_equino.html', context)

@login_required
def list_medidasBovinos(request, id):
	context = {'MedidasBovino': MedidaBovino.objects.filter(animal_da_medida_id=id)}
	return render(request, 'list_medidas_bovino.html', context)

#view de cadastro de usuário
def cadastro(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, 'cadastro.html', {'form': form})

#view que faz o cadastro de bovinos
@login_required
def cadastroBovino(request):
	form = BovinoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, 'cadastro_bovino.html', {'form': form})

#view que faz o cadastro de equinos
@login_required
def cadastroEquino(request):
	form = EquinoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, 'cadastro_equino.html', {'form': form})

#view que permite o cadastro de medias de bovinos
@login_required
def cadastroMedidaBovino(request):
    form = BovinoImagemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('paint_image')
    return render(request, 'cadastro_medida_bovino.html', {'form': form})

#view que permite o cadastro de medias de equinos
@login_required
def cadastroMedidaEquino(request):
    form = EquinoImagemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('paint_image')
    return render(request, 'cadastro_medida_equino.html', {'form': form})

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


#view de update dos bovinos
@login_required
def update_bovino(request, id):
    bovino = get_object_or_404(Bovino, pk=id)
    form = BovinoForm(request.POST or None, request.FILES or None, instance=bovino)

    if form.is_valid():
        form.save()
        return redirect('list_bovinos')

    return render(request, 'cadastro_bovino.html', {'form': form})


 #view de update dos bovinos
@login_required
def update_equino(request, id):
    equino = get_object_or_404(Equino, pk=id)
    form = EquinoForm(request.POST or None, request.FILES or None, instance=equino)

    if form.is_valid():
        form.save()
        return redirect('list_equinos')

    return render(request, 'cadastro_equino.html', {'form': form})


@login_required
def delete_bovino(request, id):
	bovino = get_object_or_404(Bovino, pk=id)
	form = BovinoForm(request.POST or None, request.FILES or None, instance=bovino)

	if request.method == 'POST':
		bovino.delete()
		return redirect('list_bovinos')

	return render(request, 'bovino_delete.html', {'bovino': bovino})


@login_required
def delete_equino(request, id):
	equino = get_object_or_404(Equino, pk=id)
	form = EquinoForm(request.POST or None, request.FILES or None, instance=equino)

	if request.method == 'POST':
		equino.delete()
		return redirect('list_equinos')

	return render(request, 'equino_delete.html', {'equino': equino})

@login_required
def detail_medida_bovino(request, id):
	medida_bovino = MedidaBovino.objects.get(id=id)
	return render(request, 'detail_medida_bovino.html', {'medida_bovino': medida_bovino})

@login_required
def detail_medida_equino(request, id):
	medida_equino = MedidaEquino.objects.get(id=id)
	return render(request, 'detail_medida_equino.html', {'medida_equino': medida_equino})


@login_required
def delete_medida_equino(request, id):
	medida_equino = MedidaEquino.objects.get(id=id)
	form = EquinoImagemForm(request.POST or None, request.FILES or None, instance=medida_equino)

	if request.method == 'POST':
		medida_equino.delete()
		return redirect('list_equinos')

	return render(request, 'delete_medida_equino.html', {'medida_equino': medida_equino})

@login_required
def delete_medida_bovino(request, id):
	medida_bovino = MedidaBovino.objects.get(id=id)
	form = BovinoImagemForm(request.POST or None, request.FILES or None, instance=medida_bovino)

	if request.method == 'POST':
		medida_bovino.delete()
		return redirect('list_bovinos')

	return render(request, 'delete_medida_bovino.html', {'medida_bovino': medida_bovino})