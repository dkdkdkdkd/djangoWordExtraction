from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('show/',views.Show.as_view(), name='show'),
    path('api/word', views.WordListAPI.as_view()),
]