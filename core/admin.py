from django.contrib import admin

from .models import Inicio, Social, Sobre, Contato, Post

# Register your models here.

#admin.site.register(Pagina)
@admin.register(Inicio)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ("id", "cabecalho","subtitulo", "site", "criado", "modificado", "ativo")
    fieldsets = (
        ('Cabeçalho', {
            'fields': ('cabecalho', 'subtitulo')
        }),
        (None, {
            'fields': ('site','icon')
        }),
        (None, {
            'fields': ('imagem','ativo')
        }),
    )

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("linkedin", "twitter", "facebook", "criado", "modificado", "ativo")
    fieldsets = (
        (None, {
            'fields': ('linkedin',)
        }),
        (None, {
            'fields': ('twitter',)
        }),
        (None, {
            'fields': ('facebook',)
        }),
        (None, {
            'fields': ('ativo',)
        }),
    )  
@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ("titulo", "criado", "modificado", "ativo", "imagem")

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "criado", "modificado", "ativo")    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "criado", "modificado","autor", "ativo")
    fieldsets = (
        (None, {
            'fields': ('titulo',)
        }),
        ('Corpo', {
            'fields': ('body', 'ativo')
        }),
    )   
    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.autor = usuario
        super(PostAdmin, self).save_model(request, obj, form, change) 
