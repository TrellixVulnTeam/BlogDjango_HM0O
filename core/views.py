from django.shortcuts import render
from .models import Inicio, Social, Sobre, Contato, Post
from .forms import ContatoForm

def index(request):
    inicio = Inicio.objects.all()
    postagens = Post.objects.all()
    social = Social.objects.all()
    context = {
        'postagens': postagens,
        'inicio': inicio,
        'social': social,
    }
    return render(request, 'index.html', context)  

def contact(request):
    inicio = Inicio.objects.all()
    contato = Contato.objects.all()
    social = Social.objects.all()
    form = ContatoForm()
    context = {
        'form': form,
        'contato': contato,
        'inicio': inicio,
        'social': social,
    }
    return render(request, 'contact.html', context)  

def about(request):
    inicio = Inicio.objects.all()
    sobre = Sobre.objects.all()
    social = Social.objects.all()
    context = {
        'sobre': sobre,
        'inicio': inicio,
        'social': social,
    }
    return render(request, 'about.html', context)      

def post(request):
    return render(request, 'api/api.html')  
