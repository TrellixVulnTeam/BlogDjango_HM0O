from django.urls import path

from .views import index, contact, about, post

#app_name = "blog"

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contact, name='contato'),
    path('sobre/', about, name='sobre'),
    path('postagem/', post, name='postagem'),
]