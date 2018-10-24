from django.contrib import admin
from .models import Equino, Bovino, SexoAnimal, MedidaBovino, MedidaEquino, RacaBovino, RacaEquino, TipoFerida

admin.site.register(RacaEquino)
admin.site.register(RacaBovino)
admin.site.register(SexoAnimal)
admin.site.register(Bovino)
admin.site.register(Equino)
admin.site.register(MedidaBovino)
admin.site.register(MedidaEquino)
admin.site.register(TipoFerida)