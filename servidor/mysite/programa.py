import mysql.connector
from datetime import datetime
from time import sleep

#https://kyup.com/tutorials/create-new-user-grant-permissions-mysql/

mydb = mysql.connector.connect\
(
    host="localhost",
    user="user",
    passwd="071930",
    database = "testdb"
)

mycursor = mydb.cursor()

#crear una tabla nueva
#mycursor.execute("CREATE TABLE datos (fecha DATETIME, humedad FLOAT,temperatura FLOAT)")

#mostrar las tablas
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

#insertar datos
#for a in range(20):
    #now = datetime.now()
    #fecha = now.strftime('%Y-%m-%d %H:%M:%S')
    #humedad = 50
    #temperatura = 20
    #print(fecha + " , " + str(humedad) + " , " + str(temperatura))

    #sql = "INSERT INTO pages_datos (fecha, humedad, temperatura) VALUES (%s, %s, %s)"
    #val = (fecha, humedad,temperatura)

    #mycursor.execute(sql, val)
    #mydb.commit()
    #sleep(1)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pages_datos")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#borrar la tabla
#sql = "DELETE FROM datos WHERE humedad = %s"
#adr = (50, )
#mycursor.execute(sql, adr)
#mydb.commit()
