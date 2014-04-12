from django.shortcuts import render_to_response, get_object_or_404
from .models import Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse

def lista_bebidas(request):
    bebidas = Bebida.objects.all()
    return render_to_response('lista_bebidas.html',
            {'lista': bebidas})


def sobre(request):
    html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
    return HttpResponse(html)
