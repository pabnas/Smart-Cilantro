import time
from datetime import datetime
import RPi.GPIO as GPIO
import netifaces as ni
import smbus
import os
import mysql.connector
import serial
import sys
import glob

import subprocess

proc1 = 0
proc2 = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

id_planta = '1'
tiempo_datos = 1
riego_min = 0
riego_max = 0

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result[0]

class Serial:
	def __init__(self):
		self.ser = serial.Serial(
		    port=serial_ports(),\
		    baudrate=9600,\
		    parity=serial.PARITY_NONE,\
		    stopbits=serial.STOPBITS_ONE,\
		    bytesize=serial.EIGHTBITS,\
		    timeout=0)
		print("connected to: " + self.ser.portstr)
		
	def get_data(self):
		valor1 = -1
		valor2 = -1
		S_reading = True
		
		while(S_reading==True):
			try:
				cadena = self.ser.readline().decode('ASCII')
				S_reading = False
			except:
				pass	
		
		try:
			if cadena == "":
				pass
			else:
				valor1 , valor2 = cadena.split(",")
				if int(valor1) > 1023:
					pass
				else:
					valor1 = int(valor1)
					valor2 = int(valor2)
		except:
			print("Arduino: "+cadena)
		return valor1,valor2

class Sensor_temperatura:
	def __init__(self):
		#conectado al gpio 4 pin con pin 7 
		pass
    
	def get_data(self):
		#change this number to the Device ID of your sensor  
		tempStore = open("/sys/bus/w1/devices/28-031724ad36ff/w1_slave")	
		data = tempStore.read()
		tempStore.close()
		tempData = data.split("\n")[1].split(" ")[9]
		temperature = float(tempData[2:])
		temperature = temperature/1000
		return temperature

class Sensor_luz:
	def __init__(self):
		#vcc 3v
		#scl = pin 5 gpio 3
		#sda = pin 3 gpio 2
		self.bus = smbus.SMBus(1)
		self.bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
		self.bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)
		time.sleep(0.5)
		
	def get_data(self,dato = 3):
		data = self.bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)
		data1 = self.bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)
		ch0 = data[1] * 256 + data[0]
		ch1 = data1[1] * 256 + data1[0]
		if dato == 1:
			return ch0 			#full espectro
		elif dato == 2:
			return ch1 			#infraroja
		else:
			return (ch0 - ch1) 	#visible

class Video:
	def __init__(self):
		#a = os.popen('./camara_init.sh')
		#print(a)
		#abrir la camara
		cmd_total = "lxterminal --command=\"/bin/bash -c './camara_init.sh; /bin/bash'\" "
		proc1 = os.system(cmd_total)
		#cargar el tunel y espera a que se cree
		cmd_total = "lxterminal --command=\"/bin/bash -c './ngrok http 8080; /bin/bash'\" "
		proc2 =os.system(cmd_total)
		time.sleep(3)
		
class Nivel:
	def __init__(self):		
		GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	
	def get_data(self):		
		alto = GPIO.input(22) #pin 15
		bajo = GPIO.input(27) #pin 13		
		
		alto != alto
		bajo != bajo
		return bajo,alto

class Motor:
	def __init__(self):		
		GPIO.setup(21,GPIO.OUT)
		GPIO.setup(20,GPIO.OUT)
		
		GPIO.output(21,GPIO.LOW)
		GPIO.output(20,GPIO.LOW)
		self.set_data(0)
		
	
	def set_data(self,habilitado):	
		if habilitado == 0:			
			GPIO.output(21,GPIO.LOW)
			GPIO.output(20,GPIO.LOW)
		else:
			GPIO.output(21,GPIO.HIGH)
			GPIO.output(20,GPIO.LOW)
			
class DB:
	def __init__(self):	
		conecto = True
		while conecto:
			try:
				self.mydb = mysql.connector.connect\
				(
					host="remotemysql.com",
					user="Nzqw6lmhpB",
					passwd="jomAeyErmk",
					database = "Nzqw6lmhpB",
					port = 3306
				)
				
				mycursor = self.mydb.cursor()
				sql = "update Planta set Planta.Ruta_camara = %s where Planta.ID = %s"
				val = (ip,id_planta)
				mycursor.execute(sql, val)
				self.mydb.commit()
				self.mydb.close()
				print("DB conectada")
				conecto=False
			except Exception as e:
				print(e)
				time.sleep(3)
				
	def actualizar_valores(self):
		self.mydb.reconnect(attempts=5, delay=0)
		mycursor = self.mydb.cursor()
		sql = "select * from Config_planta where id_Planta = %s"
		val = (id_planta,)
		mycursor.execute(sql,val)
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)
			global tiempo_datos
			global riego_max
			global riego_min
			tiempo_datos = x[1]
			riego_min = x[2]
			riego_max = x[3]
		self.mydb.close()
		print("Tiempo entre cada dato: " + str(tiempo_datos)+ " segundos")
	
	def guardar_valores(self,fecha,val_humedad,val_temp,val_pol,nivel1,nivel2,val_luz):
		self.mydb.reconnect(attempts=5, delay=0)
		mycursor = self.mydb.cursor()
		
		sql = "INSERT INTO Mediciones (id_planta, fecha, humedad, temperatura, polucion, nivelbajo, nivelalto, luz) VALUES (%s ,%s, %s, %s, %s, %s, %s, %s)"
		val = (id_planta,fecha, str(val_humedad), str(val_temp), str(val_pol) ,str(nivel1), str(nivel2), str(val_luz))
		
		mycursor.execute(sql, val)
		self.mydb.commit()
		self.mydb.close()
		
	def log_riego(self,estado,fecha):
		self.mydb.reconnect(attempts=5, delay=0)
		mycursor = self.mydb.cursor()
		
		sql = "INSERT INTO Logs (id_planta, fecha, usuario, desc_cambio) VALUES (%s ,%s, %s, %s)"
		
		if estado == 1:
			val = (id_planta,fecha, "Raspberry", "Inicio de riego")
		else:
			val = (id_planta,fecha, "Raspberry", "Fin de riego")
		
		mycursor.execute(sql, val)
		self.mydb.commit()
		self.mydb.close()
		
		
					
vid = Video()
temperatura = Sensor_temperatura()
nivel = Nivel()
luz = Sensor_luz()
arduino = Serial()
motor = Motor()
motor.set_data(0)

ip = subprocess.run(['./dir.sh'], stdout=subprocess.PIPE).stdout.decode('utf-8')
print("Camara en " + ip)

db = DB()
db.actualizar_valores()
print("")
print("")


while 1:
	try:
		db.actualizar_valores()
		
		now = datetime.now()
		fecha = now.strftime('%Y-%m-%d %H:%M:%S')
		
		val_humedad,val_pol = arduino.get_data()
		val_humedad = (val_humedad/1023)*100
		
		val_temp = temperatura.get_data()
		val_luz = luz.get_data()
		nivel1,nivel2 = nivel.get_data()		
		
		print(fecha)
		print("humedad: ",val_humedad," Polucion: ",val_pol)
		print("temp: " , val_temp)
		print("luz: ",val_luz)
		print("nivel1: ",nivel1," nivel2: ",nivel2)
		
		if val_humedad >= 0 and val_temp >= 0:
			
			val_humerdad_guardar = val_humedad
			
			if val_humedad < riego_min:
				riego = True
				print("Riego")
				db.log_riego(1,fecha)
				while riego:
					db.actualizar_valores()
					val_humedad,val_pol = arduino.get_data()
					if val_humedad != -1:
						val_riego = (val_humedad/1023)*100
						
						if val_riego >= riego_max:
							riego=False
							motor.set_data(0)
							db.log_riego(0,fecha)
						else:
							motor.set_data(1)
							print('.', end='', flush=True)
							print(str(round(val_riego,2)) + ":" + str(riego_min))
							time.sleep(2)
				
				print("Fin Riego")
			
			db.guardar_valores(fecha,val_humerdad_guardar,val_temp,val_pol,nivel1,nivel2,val_luz)
			time.sleep(tiempo_datos)
			#time.sleep(5)
		
		print("")
		time.sleep(1)
	#except KeyboardInterrupt:
		#os._exit(1)
	except Exception as e:
		print(e)
		time.sleep(3)

