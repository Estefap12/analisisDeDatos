#1. Importar el paquete o paquetes con los que voy analizar la informacion

import pandas as pd

def analizarCanastaBasica():
    #2. Sin importar la fuente (sql, xls, JSON, csv..)
    #Crear tabla tabulada que se le llama DATAFRAME
    tabla=pd.read_csv("./data/bdcanasta.csv")
    #print(tabla)

# Aplico filtros para limpiar o seleccionar datos
   # print(tabla.head(20)) #Primeros N registros.
   # print(tabla.tail())

    print(tabla.describe())


