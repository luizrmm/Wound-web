from django.contrib import admin
from django.urls import path
from .views import home, cadastro, my_logout, my_login, paint_image, cadastroAnimais

urlpatterns = [
	path('logout/', my_logout, name='logout'),
	path('login/', my_login, name='login'),
	path('', home, name='home'),
	path('cad_animais', cadastroAnimais, name='cad_animais'),
	path('cadastro/', cadastro, name='cadastro'),
	path('paint_image', paint_image, name='paint_image'),
]