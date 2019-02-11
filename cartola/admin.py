from django.contrib import admin
from .models import Jogador, Clube, Estadio, Partida, Scouts

# Register your models here.

admin.site.register([Jogador, Clube, Estadio, Partida, Scouts])
