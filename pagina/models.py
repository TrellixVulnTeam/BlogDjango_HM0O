from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pagina(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    foto = models.ImageField()
    situacao = models.BooleanField(default=False)
    atualizado = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ("-atualizado",)

    def __str__(self):
        return self.nome

class Social(models.Model):
    linkedin = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=False)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Redes Sociais'
        ordering = ("-atualizado",)
    
    def __str__(self):
        return self.linkedin

class Cores(models.Model):
    cor = models.CharField(max_length=255, blank=False)
    status = models.BooleanField(default=False)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Cores'
        ordering = ("atualizado",)
    
    def __str__(self):
        return self.cor

