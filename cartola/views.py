from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404,get_list_or_404
from cartola.models import Jogador, Clube, Partida

# Create your views here.
def home(request):
    template = loader.get_template("cartola/home.htm")
    return HttpResponse(template.render({}, request))

def jogProfile(request, jogId):
    jog = get_object_or_404(Jogador, cartola_id = jogId)
    return render(request, 'cartola/jogador.html',{'jogador':jog})

def clubeProfile(request, cluId):
    clube = get_object_or_404(Clube, cartola_id = cluId)
    return render(request, 'cartola/clube.html',{'clube':clube})

def PartidaProfile(request, partId):
    partida = get_object_or_404(Partida, id = partId)
    return render(request, 'cartola/partida.html',{'partida':partida})

def PartidasIndexByRodada(request, ano, rodada):
    partidas = get_list_or_404(Partida, ano = ano, rodada=rodada)
    template = loader.get_template("cartola/partidasRodada.html")
    context = {
        'partidas': partidas,
    }
    return render(request, 'cartola/partidasRodada.html',context)
