from django.urls import path
from . import views

app_name = 'cartola'
urlpatterns = [path("", views.home, name = "home"),
               path("home/", views.home, name = "home"),
               path("cartola/", views.home, name = "home"),
]
