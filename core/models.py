from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField
from stdimage.models import StdImageField

# Create your models here.
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateTimeField('Data de Criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Inicio(Base):
    cabecalho = models.CharField('Cabeçalho', max_length=255, blank=True)
    subtitulo = models.CharField(max_length=255, blank=True)
    site = models.CharField(max_length=255, blank=True)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': (124, 124)})
    icon = models.ImageField()

    class Meta:
        verbose_name_plural = 'Inicio'
        ordering = ("id",)

    def __str__(self):
        return self.cabecalho


class Sobre(Base):
    titulo = models.CharField(max_length=255, blank=True)
    subtitulo = models.CharField(max_length=255, blank=True)
    texto = models.TextField(max_length=800, blank=True)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': (124, 124)})

    class Meta:
        verbose_name_plural = 'Sobre'
        ordering = ("titulo",)
    
    def __str__(self):
        return self.titulo  

class Contato(Base):
    titulo = models.CharField(max_length=255, blank=True)
    subtitulo = models.CharField(max_length=255, blank=True)
    texto = models.TextField(max_length=255, blank=True)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': (124, 124)})

    class Meta:
        verbose_name_plural = 'Contato'
        ordering = ("-modificado",)
    
    def __str__(self):
        return self.titulo                      

class Social(Base):
    linkedin = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'Redes Sociais'
        ordering = ("-modificado",)
    
    def __str__(self):
        return self.linkedin


class Post(Base):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)       
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'Postagens'
        ordering = ("-modificado",)

    def __str__(self):
        return self.titulo

def post_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)    

signals.pre_save.connect(post_pre_save, sender=Post)    



