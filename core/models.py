from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)

class RacaAnimal(models.Model):
    nome_raca = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_raca

class SexoAnimal(models.Model):
    SEX_CHOICES = (
        ('F', 'Fêmea'),
        ('M', 'Macho')
    )
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)

    def __str__(self):
        return self.sex

class Animal(models.Model):
    nome_animal = models.CharField(max_length=50)
    numeracao_animal = models.IntegerField(unique=True)
    peso_animal = models.DecimalField(max_digits=5, decimal_places=2)
    idade_animal = models.IntegerField()
    raca_animal = models.ForeignKey(RacaAnimal, null=True, blank=True, on_delete=models.PROTECT)
    sexo_animal = models.ForeignKey(SexoAnimal, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_animal


