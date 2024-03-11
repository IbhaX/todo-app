from django.urls import path
from todo import views


urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
    path('contact/', views.contact, name='contact'),
]
