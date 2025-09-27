#Importar librerias
import argparse
import random

#Crear un objeto de conexión
parser = argparse.ArgumentParser() #Igual siempre
parser.add_argument("--saludo", default = " ") #Opción (--)

args = parser.parse_args()

mensaje = str(args.saludo)

dr = random.randint(1,100)

if mensaje == "Hola":
   if dr <= 50:
        print("Hola, cómo estas?")
   elif dr <= 75:
        print("Hola, me llamo Computina")
   else:
        print("Háblale a la mano")
else:
    print("Saluda primero!!!")     
