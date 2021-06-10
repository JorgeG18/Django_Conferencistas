from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Participantes
from .models import Conferencista
from django.contrib import messages
from telegram import Bot
from django.urls import reverse

# Create your views here.a
    #Clase 24/05
    #nombre = request.GET.get('nombre')
    #pellido = request.GET.get('apellido')
    #edad = request.GET.get('edad')
    #return HttpResponse(f'Hola Mundo {nombre} {apellido}, edad es {edad} años???')

    #Clase 25/05

    #nombre = request.GET.get('nombre')

    #Variable get          : name
    #Variablee de python   : n
    #Variable de plantilla : x
    #Enviar valores a la plantilla a travez del contexto

    #Recibir por get los paramentros para calcular la cuota de un prestamo bancario
    #monto: m, tasa: r, plazo: n

    #paso1
    #m = int(request.GET.get('m')) 
    #r = int(request.GET.get('r')) 
    #n = int(request.GET.get('n')) 

    #Preparar los datos para suministrarlos a las formulas
    #r = r / 100 / 12
    #n = n * 12


    #paso 3 Aplicar la formula c = (m * r) / (1 - (1 + r) ** -n)

    #c = (m * r) / (1 - (1 + r) ** -n)

    #ctx = {
    #    'cuota': c
    #}

#Clase 26/05

TOKEN = '1891788970:AAH3tg0QTczsdZvCktUXHRQmKCSPbXMzteA'
GROUP_ID = -500275385

bot = Bot(token=TOKEN)

def index(request):
    return render(request, 'registro/index.html')

def participantes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        p = Participantes(nombre=nombre, apellido=apellido, correo=correo, twitter=twitter)
        p.save()

        msj = f'El participante {nombre} {apellido} ha sido registrado con éxito'
       
    #Codigo para mandar un mensaje a grupo de telegram

        try:
            bot.send_message(chat_id=GROUP_ID, text=msj)
        except Exception as e:
            msj += f'<br/><strong>{e}</strong>'
    
        messages.add_message(request, messages.INFO, msj) 
    activo = 'participantes'
    q = request.GET.get('q')

    if q:
        data = Participantes.objects.filter(nombre__startswith=q).order_by('nombre')

        '''
        select * from participantes
        where nombre like 'n%'
        '''
    else:
        data = Participantes.objects.all().order_by('nombre')

    ctx = {
        'activo': activo,
        'participantes': data,
        'q': q,
    }

    return render(request, 'registro/participantes.html', ctx)

def eliminar_participantes(request, id):
    Participantes.objects.get(pk=id).delete()
    return redirect(reverse('participantes'))

def editar_participantes(request, id):
    #par = Participantes.objects.get(pk=id)
    par = get_object_or_404(Participantes, pk=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        par.nombre = nombre
        par.apellido = apellido
        par.correo = correo
        par.twitter = twitter
        par.save()

    data = Participantes.objects.all().order_by('nombre')

    ctx = {
        'activo': 'Participantes',
        'participantes': data,
        'p': par,
    }
    
    return render(request, 'registro/participantes.html', ctx)

def conferencista(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        experiencia = request.POST.get('experiencia')

        c = Conferencista(nombre=nombre, apellido=apellido, experiencia=experiencia)
        c.save()
        
        msj = f'El Conferecista {nombre} {apellido} ha sido registrado con éxito'

        messages.add_message(request, messages.INFO, msj) 
    activo = 'participantes'
    q = request.GET.get('q')

    if q:
        bd = Conferencista.objects.filter(nombre__startswith=q).order_by('nombre')

    else:
        bd = Conferencista.objects.all().order_by('nombre')

    ctx = {
        'activo': activo,
        'conferencista' : bd,
        'q': q,
    }

    return render(request, 'registro/conferencista.html', ctx)
  
def eliminar_conferencista(request, id):
    Conferencista.objects.get(pk=id).delete()
    return redirect(reverse('conferencista'))

