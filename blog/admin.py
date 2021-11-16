from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "criado", "autor", "atualizado", "situacao", "resumo")
    fieldsets = (
        (None, {
            'fields': ('titulo', 'slug')
        }),
        ('Corpo', {
            'fields': ('body', 'situacao', 'resumo')
        }),
    )
    #list_filter = ('titulo', 'situacao')
    #prepopulated_filds = {"slug": ("titulo",)}
    #readonly_fields = ('autor',)

    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.autor = usuario
        super(PostAdmin, self).save_model(request, obj, form, change)

    #def get_queryset(self, request):
        #filtragem = super(PostAdmin, self).get_queryset(request)
        #filtragem = filtragem.filter(autor=request.user)
        #return filtragem
        