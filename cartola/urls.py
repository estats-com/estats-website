from django.urls import path
from . import views

app_name = 'cartola'
urlpatterns = [path("", views.home, name = "home"),
               path("home/", views.home, name = "home"),
               path("jogador<int:jogId>/", views.jogProfile, name = "jogProfile"),
               path("clube<int:cluId>/", views.clubeProfile, name = "clubeProfile"),
               path("partida<int:partId>/", views.PartidaProfile, name = "PartidaProfile"),
               path("partidas<int:ano>-<int:rodada>/", views.PartidasIndexByRodada, name = "PartidasRodada"),
]
