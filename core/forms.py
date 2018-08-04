from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Animal, RacaAnimal, SexoAnimal
from django.forms import ModelForm

class AnimalForm(ModelForm):

    class Meta:
        model = Animal
        fields = [
            'nome_animal',
            'numeracao_animal',
            'peso_animal',
            'idade_animal',
            'raca_animal',
            'sexo_animal'
        ]

        error_messages = {
            'numeracao_animal': {
                'unique': 'Numeração já existente'
            },
        }

class RegistrationForm (UserCreationForm):
    email = forms.EmailField(required=True)

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


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
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user