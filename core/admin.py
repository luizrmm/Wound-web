from django.contrib import admin
from .models import Animal, SexoAnimal, MedidaAnimal, TipoFerida, Especie

admin.site.register(SexoAnimal)
admin.site.register(Animal)
admin.site.register(MedidaAnimal)
admin.site.register(TipoFerida)
admin.site.register(Especie)