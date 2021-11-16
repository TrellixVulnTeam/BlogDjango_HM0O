from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    situacao = models.BooleanField(default=False)
    resumo = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Postagens'
        ordering = ("-criado",)

    def __str__(self):
        return self.titulo

    #def get_absolute_url(self):
        #return reverse("blog:detail", kwargs={"slug": self.slug})