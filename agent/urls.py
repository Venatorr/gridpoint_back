from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.get_file, name='upload'),
]
