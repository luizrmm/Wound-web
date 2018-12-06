from django.db import models


#tipos das feridas nos animais
class TipoFerida(models.Model):
	FERIDA_CHOICES = (
		('acidental', 'acidental'),
		('induzida', 'induzida')
	)
	tipo = models.CharField(max_length=20,choices=FERIDA_CHOICES)
	class Meta:
		verbose_name_plural = 'Tipo da ferida'

	def __str__(self):
		return self.tipo



#classe que representa o sexo do animal
class SexoAnimal(models.Model):
	SEX_CHOICES = (
		('F', 'Feminino'),
		('M', 'Masculino')
	)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES)

	class Meta:
		verbose_name_plural = 'Sexo'

	def __str__(self):
		return self.sex

class Especie(models.Model):
	especie = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'Espécies'

	def __str__(self):
		return self.especie


#classe que representa o animal
class Animal(models.Model):
	nome_do_animal = models.CharField(max_length=50)
	numeracao_do_animal = models.IntegerField(unique=True)
	peso_do_animal = models.DecimalField(max_digits=5, decimal_places=2)
	anos = models.IntegerField()
	meses = models.IntegerField()
	especie = models.ForeignKey(Especie, null=True, blank=True, on_delete=models.SET_NULL)
	raca = models.CharField(max_length=50)
	sexo_do_animal = models.ForeignKey(SexoAnimal, null=True, blank=True, on_delete=models.PROTECT)

	class Meta:
		verbose_name_plural = 'Animais'

	def __str__(self):
		return self.nome_do_animal

####################################################################################################


# classe que representa a medida da obtida de cada imagem
class MedidaAnimal(models.Model):
	data_medida = models.DateField()
	image = models.ImageField(upload_to='imagens_medidas', blank=True)
	medida_obtida = models.DecimalField(max_digits=5, decimal_places=2)
	tipo_ferida = models.ForeignKey(TipoFerida, null=True, blank=True, on_delete=models.PROTECT)
	animal_da_medida = models.ForeignKey(Animal, on_delete=models.CASCADE)
	local_ferida = models.CharField(max_length=100, blank=True)
	observacoes = models.TextField(null=True, blank=True)

	class Meta:
		verbose_name_plural = "Medidas"

