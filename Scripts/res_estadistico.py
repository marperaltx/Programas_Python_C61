#Importar librerias
import numpy as np 
import pandas as pd 
import argparse

#Crear un objeto de conexión
parser = argparse.ArgumentParser(description = "Resumen estadistico") #Igual siempre
parser.add_argument("input", help = "Archivo csv" ) #Solo cambia el argumento

args = parser.parse_args()

df = pd.read_csv(args.input)
print(df.describe())