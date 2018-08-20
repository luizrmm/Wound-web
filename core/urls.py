from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, cadastro, my_logout, my_login, paint_image, cadastroAnimais, cadastroMedida

urlpatterns = [
	path('logout/', my_logout, name='logout'),
	path('login/', my_login, name='login'),
	path('', home, name='home'),
	path('cad_animais/', cadastroAnimais, name='cad_animais'),
	path('cadastro/', cadastro, name='cadastro'),
	path('paint_image/', paint_image, name='paint_image'),
	path('cadastro_medida/', cadastroMedida, name='cadastro_medida'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)