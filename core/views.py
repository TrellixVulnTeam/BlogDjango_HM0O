from django.shortcuts import render
from blog.models import Post
from pagina.models import Pagina, Social, Cores

def index(request):
    pagina = Pagina.objects.all()
    lista = Post.objects.all()
    social = Social.objects.all()
    cores = Cores.objects.all()
    context = {
        'lista': lista,
        'pagina': pagina,
        'social': social,
        'cores': cores,
    }
    return render(request, 'index.html', context)  
