from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.shortcuts import redirect
from collections import namedtuple
from django.core.serializers.json import DjangoJSONEncoder
import json
import sys
import datetime

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
    try:
        if request.POST['username'] == "":
            raise Exception("Username vacio")
        if request.POST['password'] == "":
            raise Exception("Contraseña vacia")
        if request.POST['nombre'] == "":
            raise Exception("Nombre vacio")

        usuarios = Usuario.objects.raw("SELECT * FROM Usuario WHERE Username = '" + request.POST['username'] + "'")

        if(len(list(usuarios)) > 0): #si existe el username
            resultado = "Username ya existe"
        else:
            with connection.cursor() as cursor:
                query = "INSERT INTO Usuario (Username, Nombre, Apellidos,Password, Privilegios) VALUES (%s , %s, %s, %s ,'2');"
                cursor.execute(query,[request.POST['username'],request.POST['nombre'],request.POST['apellido'],request.POST['password']])

                query = "INSERT INTO Logs (id_Planta, fecha , usuario,  desc_cambio ,  new_value ) VALUES (%s , %s, %s, %s ,%s);"
                cursor.execute(query,["0",str(datetime.datetime.now()),"Registro","creacion de usuario",request.POST['username']])
            resultado = "Success"
    except Exception as e:
        resultado = str(e)
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
    if request.COOKIES.get('user') != "" and request.COOKIES.get('user') != None:
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

                query = "SELECT t.* FROM Config_planta t WHERE t.id_Planta = %s"
                cursor.execute(query, [planta.id])
                configuraciones = namedtuplefetchall(cursor)

            return render(request, "home.html",{'usuario': usuario, 'planta': planta,'last_medida':ultima_medicion,'medidas':medidas,'configuracion':configuraciones[0]})
        else:
            planta.id = 0
            return render(request, "home.html",{'usuario': usuario, 'planta': planta})
    else:
        return redirect('/')

def home_datos(request):
    data = dict()
    with connection.cursor() as cursor:
        query = "SELECT * FROM `Mediciones` WHERE id_Planta = %s and (%s <= fecha and fecha <= %s + INTERVAL 1 DAY)"
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
    if request.COOKIES.get('user') != "" and request.COOKIES.get('user') != None:
        usuario = Usuario.objects.raw("SELECT * FROM `Usuario` WHERE Username = %s",[request.COOKIES.get('user')])[0]

        planta = Planta.objects.raw("SELECT Planta.* FROM (Planta INNER JOIN Usuario_Planta ON Planta.ID = Usuario_Planta.id_Planta) WHERE Usuario_Planta.id_Usuario = %s",[usuario.id])
        if (len(planta)>0):  # si hay plantas
            planta = planta[0]
            with connection.cursor() as cursor:
                query = "SELECT t.* FROM Config_planta t WHERE t.id_Planta = %s"
                cursor.execute(query,[planta.id])
                configuraciones = namedtuplefetchall(cursor)

            return render(request, "perfil.html",{'usuario': usuario, 'planta': planta,'configuracion':configuraciones[0]})
        else:
            planta.id = 0
            return render(request, "perfil.html",{'usuario': usuario, 'planta': planta})
    else:
        return redirect('/')

def perfil_actualizar(request):
    data = dict()

    with connection.cursor() as cursor:
        query = "SELECT * FROM Usuario WHERE Username = %s"
        cursor.execute(query, [request.POST['username']])
        user = namedtuplefetchall(cursor)[0]

        query = "UPDATE Usuario SET Username = %s , Nombre = %s, Apellidos = %s, Password = %s WHERE Username = %s;"
        cursor.execute(query, [request.POST['username'], request.POST['nombre'], request.POST['apellido'],request.POST['password'],request.POST['username']])

        query = "INSERT INTO Logs (id_Planta, fecha , usuario,  desc_cambio ,  new_value , old_value ) VALUES (%s , %s, %s, %s ,%s,%s);"
        new = request.POST['nombre'] + "__" + request.POST['apellido'] + "__" + request.POST['password']
        old = user.Nombre + "__" + user.Apellidos + "__" + user.Password

        cursor.execute(query,["0", str(datetime.datetime.now()), request.POST['username'], "Actualizacion de perfil", new,old])

    resultado = "correcto"

    data["result"] = resultado
    return JsonResponse(data)

def perfil_actualizar_admin(request):
    data = dict()
    try:
        with connection.cursor() as cursor:
            query = "UPDATE Usuario SET Nombre = %s, Apellidos = %s, Privilegios = %s WHERE Username = %s;"
            cursor.execute(query, [request.POST['nombre'], request.POST['apellido'],request.POST['privilegios'],request.POST['username']])

            query = "select t1.* from Usuario_Planta t1 INNER JOIN Usuario t2 ON t1.id_Usuario = t2.ID where t2.Username = %s"
            cursor.execute(query,[request.POST['username']])
            usuario_rel = namedtuplefetchall(cursor)


            query = "select * from Usuario where Username = %s"
            cursor.execute(query,[request.POST['username']])
            usuario = namedtuplefetchall(cursor)[0]


            if len(usuario_rel) == 0:
                query = "INSERT into Usuario_Planta (id_Planta,id_Usuario) values (%s,%s)"
                cursor.execute(query, [request.POST['planta'], usuario.ID])
                old = usuario.Nombre + "__" + usuario.Apellidos + "__" + str(usuario.Privilegios) + "__" + "NULL"

            else:
                usuario_rel = namedtuplefetchall(cursor)[0]
                if request.POST['planta'] != "":
                    query = "UPDATE Usuario_Planta SET id_Planta = %s WHERE id_Usuario = %s"
                    cursor.execute(query, [request.POST['planta'], usuario.ID])
                else:
                    query = "UPDATE Usuario_Planta SET id_Planta = NULL WHERE id_Usuario = %s"
                    cursor.execute(query, [usuario.ID])

                old = usuario.Nombre + "__" + usuario.Apellidos + "__" + str(usuario.Privilegios) + "__" + str(usuario_rel.id_Planta)

            new = request.POST['nombre'] + "__" + request.POST['apellido'] + "__" + request.POST['privilegios'] + "__" + request.POST['planta']
            query = "INSERT INTO Logs (id_Planta, fecha , usuario,  desc_cambio ,  new_value , old_value ) VALUES (%s , %s, %s, %s ,%s,%s);"
            cursor.execute(query,["0", str(datetime.datetime.now()), request.COOKIES['user'], "Actualizacion(Admin)", new, old])

    except Exception as e:
        ex_type, ex_value, ex_traceback = sys.exc_info()
        resultado = str(ex_value)
    data["result"] = resultado
    return JsonResponse(data)

def buscar_username(request):
    data = dict()
    with connection.cursor() as cursor:
        query = "SELECT * FROM Usuario WHERE Username like '%%" + request.GET['username'] + "%%'"
        cursor.execute(query)
        usuarios = namedtuplefetchall(cursor)

        query = "SELECT * FROM Roles"
        cursor.execute(query)
        roles = namedtuplefetchall(cursor)

        query = "select * from Planta"
        cursor.execute(query)
        plantas = namedtuplefetchall(cursor)

    data["usuarios"] = []
    data["roles"] = []
    data["plantas"] = []

    for usuario in usuarios:
        usr = dict()

        usr["id"] = usuario.ID
        usr["username"] = usuario.Username
        usr["nombre"] = usuario.Nombre
        usr["apellidos"] = usuario.Apellidos
        usr["privilegios"] = usuario.Privilegios

        data["usuarios"].append(usr)

    for rol in roles:
        rol_list = dict()

        rol_list["ID"] = rol.IDRol
        rol_list["nombre"] = rol.Nombre

        data["roles"].append(rol_list)

    for planta in plantas:
        plt = dict()
        rel = []

        plt["id"] = planta.ID
        plt["tipo"] = planta.tipo

        with connection.cursor() as cursor:
            query = "SELECT t1.* from Usuario_Planta t1 INNER JOIN Planta t2 ON t1.id_Planta = t2.ID where t1.id_Planta = %s"
            cursor.execute(query,[planta.ID])
            relaciones = namedtuplefetchall(cursor)

        for relacion in relaciones:
            if planta.ID == relacion.id_Planta:
                rel.append(relacion.id_Usuario)
        plt["usuarios"] = rel

        data["plantas"].append(plt)


    return JsonResponse(data)

def saveconfig(request):
    data = dict()
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM Config_planta WHERE id_planta = %s"
            cursor.execute(query, [request.POST['id_planta']])
            conf = namedtuplefetchall(cursor)[0]

            query = "UPDATE Config_planta SET Tiempo_toma_de_datos = %s , threshold_riego_min = %s, threshold_riego_max = %s" \
                " WHERE  id_planta = %s;"
            cursor.execute(query, [request.POST['tiempo'], request.POST['riego_min'], request.POST['riego_max'],
                                   request.POST['id_planta']])

            old = str(conf.Tiempo_toma_de_datos) + "__" + str(conf.threshold_riego_min) + "__" + str(conf.threshold_riego_max)
            new = request.POST['tiempo'] + "__" + request.POST['riego_min'] + "__" + request.POST['riego_max']

            query = "INSERT INTO Logs (id_Planta, fecha , usuario,  desc_cambio ,  new_value , old_value ) VALUES (%s , %s, %s, %s ,%s,%s);"
            cursor.execute(query,
                           [request.POST['id_planta'], str(datetime.datetime.now()), request.COOKIES['user'], "Actualizacion de configuracion", new,
                            old])
        resultado = "Se realizaron los cambios correctamente"

    except Exception as e:
        ex_type, ex_value, ex_traceback = sys.exc_info()
        resultado = str(ex_value)
    data["result"] = resultado
    return JsonResponse(data)
