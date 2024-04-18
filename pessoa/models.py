from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100)
    rua = models.CharField(verbose_name="Rua", max_length=255)
    cidade = models.CharField(verbose_name="Cidade", max_length=100)
    telfone= models.CharField(verbose_name="Telefone", max_length=20)
    
    class Meta:
        verbose_name = "Pessoa"    
        verbose_name_plural = "Pessoas"