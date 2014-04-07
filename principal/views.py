from django.shortcuts import render_to_response
from .models import Bebida


def lista_bebidas(request):
    bebidas = Bebida.objects.all()
    return render_to_response('lista_bebidas.html',
            {'lista': bebidas})

