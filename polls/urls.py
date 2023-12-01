from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/엉루지/
    path('<character_name>/', views.detail, name='detail'),
    # ex: /polls/엉루지/results/
    path('<str:character_name>/', views.results, name='results'),
]
