from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, cadastro, my_logout, my_login, paint_image, cadastroBovino, cadastroEquino,\
cadastroMedidaEquino, cadastroMedidaBovino, Especie, list_bovinos, list_equinos, update_bovino, update_equino,\
list_medidasEquinos, list_medidasBovinos, delete_bovino, delete_equino, detail_medida_bovino, detail_medida_equino,\
delete_medida_bovino, delete_medida_equino
urlpatterns = [
	path('logout/', my_logout, name='logout'),
	path('login/', my_login, name='login'),
	path('', home, name='home'),
	path('especie_animal/', Especie, name='especie_animal'),
	path('cadastro_bovino/', cadastroBovino, name='cadastro_bovino'),
	path('cadastro_equino/', cadastroEquino, name='cadastro_equino'),
	path('cadastro/', cadastro, name='cadastro'),
	path('paint_image/', paint_image, name='paint_image'),
	path('cadastro_medida_bovino/', cadastroMedidaBovino, name='cadastro_medida_bovino'),
	path('cadastro_medida_equino/', cadastroMedidaEquino, name='cadastro_medida_equino'),
	path('list_bovinos/', list_bovinos, name='list_bovinos'),
	path('list_equinos/', list_equinos, name='list_equinos'),
	path('list_medidasEquinos/<int:id>/', list_medidasEquinos, name='list_medidas_equinos'),
	path('list_medidasBovinos/<int:id>/', list_medidasBovinos, name='list_medidas_bovinos'),
	path('update_bovino/<int:id>/', update_bovino, name='update_bovino'),
	path('update_equino/<int:id>/', update_equino, name='update_equino'),
	path('delete_bovino/<int:id>/', delete_bovino, name='delete_bovino'),
	path('delete_equino/<int:id>/', delete_equino, name='delete_equino'),
	path('detail_medida_bovino/<int:id>/', detail_medida_bovino, name='detail_medida_bovino'),
	path('detail_medida_equino/<int:id>/', detail_medida_equino, name='detail_medida_equino'),
	path('delete_medida_bovino/<int:id>/', delete_medida_bovino, name='delete_medida_bovino'),
	path('delete_medida_equino/<int:id>/', delete_medida_equino, name='delete_medida_equino'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)