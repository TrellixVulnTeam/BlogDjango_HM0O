from django.contrib import admin

from pagina.models import Pagina, Social, Cores

# Register your models here.

#admin.site.register(Pagina)
@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome","endereco", "site", "contato", "foto", "situacao", "atualizado")
    fieldsets = (
        (None, {
            'fields': ('nome', 'sobrenome')
        }),
        ('Site', {
            'fields': ('site',)
        }),
        ('Informações', {
            'fields': ('endereco', 'contato')
        }),
        ('Perfil', {
            'fields': ('foto',)
        }),
        ('Informações', {
            'fields': ('situacao',)
        }),
    )

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("linkedin", "twitter", "facebook", "status", "atualizado")
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
            'fields': ('status',)
        }),
    )  
@admin.register(Cores)
class CoresAdmin(admin.ModelAdmin):
    list_display = ("cor", "status", "atualizado")