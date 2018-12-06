from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Animal, SexoAnimal, MedidaAnimal, TipoFerida, Especie
from django.forms import ModelForm


class AnimalForm(ModelForm):

	class Meta:
		model = Animal
		fields = [
			'nome_do_animal',
			'numeracao_do_animal',
			'peso_do_animal',
			'especie',
			'raca',
			'anos',
			'meses',
			'sexo_do_animal'
		]

		widgets = {
			'nome_do_animal': forms.TextInput(attrs={'class': 'form-control'}),
			'numeracao_do_animal': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
			'peso_do_animal': forms.NumberInput(attrs={'class': 'form-control'}),
			'especie': forms.Select(attrs={'class': 'form-control'}),
			'raca': forms.TextInput(attrs={'class': 'form-control'}),
			'anos': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
			'meses': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
			'sexo_do_animal': forms.Select(attrs={'class': 'form-control'})
		}

		error_messages = {
			'numeracao_do_animal': {
				'unique': 'Numeração já existente'
			},
		}


class MedidaForm(ModelForm):

	class Meta:
		model = MedidaAnimal
		fields = [
			'data_medida',
			'image',
			'medida_obtida',
			'tipo_ferida',
			'animal_da_medida',
			'local_ferida',
			'observacoes'
		]

		widgets = {
			'data_medida': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
			'animal_da_medida': forms.Select(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),
			'medida_obtida': forms.NumberInput(attrs={'class': 'form-control'}),
			'tipo_ferida': forms.Select(attrs={'class': 'form-control'}),
			'local_ferida': forms.TextInput(attrs={'class': 'form-control'}),
			'observacoes': forms.Textarea(attrs={'class': 'form-control'})
		}



class RegistrationForm (UserCreationForm):
	email = forms.EmailField(required=True)

	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Deve conter números e letras'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita sua senha'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Insira seu email'}))


	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		]

		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira seu nome de usuário'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insria seu nome'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira seu sobrenome'})
		}

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user