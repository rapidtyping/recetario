from .forms import ContactoForm
from .models import Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.mail import EmailMessage


def lista_bebidas(request):
    bebidas = Bebida.objects.all()
    return render_to_response('lista_bebidas.html',
            {'lista': bebidas})


def sobre(request):
    html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
    return HttpResponse(html)
    

def inicio(request):
    recetas = Receta.objects.all()
    return render_to_response('inicio.html',{ 'recetas': recetas})
    

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    return render_to_response('usuarios.html',
        {'usuarios':usuarios, 'recetas':recetas})
        
def lista_recetas(request):
    recetas = Receta.objects.all()
    return render_to_response('recetas.html',
        {'datos':recetas},
        context_instance=RequestContext(request))
        

def detalle_receta(request, id_receta):
    dato = get_object_or_404(Receta, pk=id_receta)
    comentarios = Comentario.objects.filter(receta=dato)
    return render_to_response('receta.html',
        {'receta':dato, 'comentarios':comentarios},
        context_instance=RequestContext(request))


def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el rectario de Maestros del Web'
            contenido = formulario.cleaned_data['mensaje']
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['destinatario@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('contactoform.html',
                {'formulario':formulario},
                context_instance=RequestContext(request))
