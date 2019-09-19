from datetime import datetime  
from datetime import timedelta 

inicio = datetime.strptime("2019/08/28 00:00:00", "%Y/%m/%d %H:%M:%S")
print(inicio)

f = open("temp.sql", "r")
fn = open("tempcambiado.txt","w")
for line in f:
    s = line 	    
    timestampStr = inicio.strftime("%Y/%m/%d %H:%M:%S")
    inicio = inicio + timedelta(minutes=15)
    new = s[:-3] + ",'" + timestampStr + "'"+ s[-3:]

    fn.write(new)
f.close() 
fn.close()

