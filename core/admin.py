from django.contrib import admin
from .models import UserProfile, RacaAnimal, SexoAnimal, Animal

admin.site.register(UserProfile)
admin.site.register(RacaAnimal)
admin.site.register(SexoAnimal)
admin.site.register(Animal)