#1. Importar el paquete o paquetes con los que voy a analisar la informacion

import pandas as pd 
from helpers.creacionTabla import crearTabla

def analizarCanastaBasica():
    #2. Sin importar la fuente (sql, xls, JSON ,csv...)
    #Crear una tabla tabulada que se llama DATAFRAME
    tabla=pd.read_csv("./data/bdcanasta.csv")
    #print(tabla)
    crearTabla(tabla,"canastabasica")
    
#3. Aplico filtro para limpiar o seleccionar datos

    #print(tabla.head(20)) #Primeros N registros
    #print(tabla.tail()) #Los ultimos registros
    #Filtros:   
    #filtroPanes=tabla.query(" (Producto=='Pan') and (Origen=='India')")
    
    filtroPrecios=tabla.query("PrecioporUnidad<50")
    
    crearTabla(filtroPrecios, "filtroPrecios")


