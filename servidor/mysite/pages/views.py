from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.shortcuts import redirect
from collections import namedtuple
from django.core.serializers.json import DjangoJSONEncoder
import json

from .models import *
#https://docs.djangoproject.com/en/2.1/topics/db/sql/

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def index(request):
    return render(request,"login.html",{})

def registro(request):
    return render(request,"registro.html",{})

def validar_registro(request):
    data = dict()
    usuarios = Usuario.objects.raw("SELECT * FROM Usuario WHERE Username = '" + request.POST['username'] + "'")

    if(len(list(usuarios)) > 0): #si existe el username
        resultado = "Username ya existe"
    else:
        query = "INSERT INTO Usuario (Username, Nombre, Apellidos, Password, Privilegios) VALUES (%s , %s, %s, %s ,'2');"
        with connection.cursor() as cursor:
            cursor.execute(query,[request.POST['username'],request.POST['nombre'],request.POST['apellido'],request.POST['password']])
        resultado = "Success"
    data["result"] = resultado
    return JsonResponse(data)

def validar_login(request):
    data = dict()
    usuarios = Usuario.objects.raw("SELECT * FROM Usuario WHERE Username= %s AND Password= %s ",[request.POST['user'],request.POST['password']])
    if (len(list(usuarios)) > 0):  # si los datos son correctos
        resultado = "home"
    else:
        resultado = "/"
    data["url"] = resultado
    return JsonResponse(data)

def home(request):
    if request.COOKIES.get('user') != "":
        usuario = Usuario.objects.raw("SELECT * FROM `Usuario` WHERE Username = %s",[request.COOKIES.get('user')])[0]
        planta = Planta.objects.raw("SELECT Planta.* FROM (Planta INNER JOIN Usuario_Planta ON Planta.ID = Usuario_Planta.id_Planta) WHERE Usuario_Planta.id_Usuario = %s",[usuario.id])
        if (len(planta)>0):  # si hay plantas
            planta = planta[0]
            with connection.cursor() as cursor:
                query = "SELECT Mediciones.* FROM Mediciones WHERE id_Planta = %s ORDER BY fecha DESC LIMIT 1"
                cursor.execute(query,[planta.id])
                ultima_medicion = namedtuplefetchall(cursor)[0]

                query = "SELECT Mediciones.* FROM Mediciones WHERE id_Planta = %s and Mediciones.fecha > DATE_ADD(NOW(), INTERVAL -4 WEEK) ORDER BY fecha"
                #query = "SELECT Mediciones.* FROM Mediciones WHERE id_Planta = %s ORDER BY fecha"
                cursor.execute(query,[planta.id])
                medidas = namedtuplefetchall(cursor)
            return render(request, "home.html",{'usuario': usuario, 'planta': planta,'last_medida':ultima_medicion,'medidas':medidas})
        else:
            planta.id = 0
            return render(request, "home.html",{'usuario': usuario, 'planta': planta})
    else:
        return redirect('/')

def home_datos(request):
    data = dict()
    with connection.cursor() as cursor:
        query = "SELECT * FROM `Mediciones` WHERE id_Planta = %s and %s <= fecha and fecha <= %s"
        cursor.execute(query, [request.POST['planta_id'] , request.POST['fecha_inicio'] , request.POST['fecha_fin'] ])
        medidas = namedtuplefetchall(cursor)

    data["medidas"] = []
    for medida in medidas:
        med = dict()
        med["fecha"] = medida.fecha.strftime("%d/%m/%Y %H:%M:%S")
        med["humedad"] = medida.humedad
        med["temperatura"] = medida.temperatura
        med["polucion"] = medida.polucion
        med["luz"] = medida.luz

        data["medidas"].append(med)
    return JsonResponse(data)

def perfil(request):
    if request.COOKIES.get('user') != "":
        usuario = Usuario.objects.raw("SELECT * FROM `Usuario` WHERE Username = %s",[request.COOKIES.get('user')])[0]
        return render(request,"perfil.html",{'usuario':usuario})
    else:
        return redirect('/')

def perfil_actualizar(request):
    data = dict()

    query = "UPDATE Usuario SET Username = %s , Nombre = %s, Apellidos = %s, Password = %s WHERE Username = %s;"
    with connection.cursor() as cursor:
        cursor.execute(query, [request.POST['username'], request.POST['nombre'], request.POST['apellido'],request.POST['password'],request.POST['username']])
    resultado = "correcto"

    data["result"] = resultado
    return JsonResponse(data)