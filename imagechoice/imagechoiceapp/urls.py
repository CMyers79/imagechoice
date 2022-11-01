from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quantity>/', views.choice, name='choice'),
    ]
