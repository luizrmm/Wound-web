from django.db import models

#classe que representa a raça do animal
class RacaAnimal(models.Model):
    nome_raca = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_raca
    class Meta:
        verbose_name_plural = 'Raças'

#classe que representa o sexo do animal
class SexoAnimal(models.Model):
    SEX_CHOICES = (
        ('F', 'Fêmea'),
        ('M', 'Macho')
    )
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)

    class Meta:
        verbose_name_plural = 'Sexo'

    def __str__(self):
        return self.sex

#classe que representa o animal
class Animal(models.Model):
    nome_animal = models.CharField(max_length=50)
    numeracao_animal = models.IntegerField(unique=True)
    peso_animal = models.DecimalField(max_digits=5, decimal_places=2)
    idade_animal = models.IntegerField()
    raca_animal = models.ForeignKey(RacaAnimal, null=True, blank=True, on_delete=models.PROTECT)
    sexo_animal = models.ForeignKey(SexoAnimal, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Animais'

    def __str__(self):
        return self.nome_animal


# classe que representa a medida da obtida de casa imagem

class MedidaImagem(models.Model):
    codigo_medida = models.CharField(max_length=50, default='')
    data_medida = models.DateField()
    image = models.ImageField(upload_to='imagens_medidas', blank=True)
    medida_obtida = models.DecimalField(max_digits=5, decimal_places=2)
    animal_da_medida = models.ForeignKey(Animal, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Medida Imagens"

    def __str__(self):
        return 'codigo: ' + self.codigo_medida
