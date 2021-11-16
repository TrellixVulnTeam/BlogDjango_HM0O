from django.urls import path

from .views import index

#app_name = "blog"

urlpatterns = [
    path('', index),
    #path("", views.PostListView.as_view(), name="list"),
    #path("<slug:slug>/", views.PostDetaiView.as_view(), name="detail")
]