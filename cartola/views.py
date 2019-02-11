from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# Create your views here.

def home(request):
    template = loader.get_template("cartola/home.htm")
    return HttpResponse(template.render({}, request))
