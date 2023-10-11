from django.db import models

# Create your models here.


class Amigo(models.Model):
    nome = models.CharField("nome", max_length=200, blank=True)
    modelo = models.CharField("Marca", max_length=200, blank=True)
    # email = models.EmailField("Email", max_length=100)
    # informacao = models.TextField("Informações", blank=True)
    fabricante = models.CharField("Fabricante", max_length=200)
    # endereco = models.CharField("Endereço", max_length=200, blank=True)
    ano = models.DateField("Ano de fabricação", blank=True, null=True)
    avatar = models.ImageField("Avatar", upload_to="avatares", blank=True, null=True)
    whatsapp = models.CharField("whatsapp", max_length=200, blank=True)
    
    def __str__(self):
        return self.modelo
