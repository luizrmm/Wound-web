from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, paint_image, list_animais, list_medidas, cadastro, cadastroAnimal, my_login, my_logout, update_animal, delete_animal, delete_medida, detail_medida
urlpatterns = [
	path('logout/', my_logout, name='logout'),
	path('login/', my_login, name='login'),
	path('', home, name='home'),
	path('cadastro_animal/', cadastroAnimal, name='cadastro_animal'),
	path('cadastro/', cadastro, name='cadastro'),
	path('paint_image/', paint_image, name='paint_image'),
	path('list_animais/', list_animais, name='list_animais'),
	path('list_medidas/<int:id>/', list_medidas, name='list_medidas'),
	path('update_animal/<int:id>/', update_animal, name='update_animal'),
	path('delete_animal/<int:id>/', delete_animal, name='delete_animal'),
	path('detail_medida/<int:id>/', detail_medida, name='detail_medida'),
	path('delete_medida/<int:id>/', delete_medida, name='delete_medida'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)