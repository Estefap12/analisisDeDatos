import matplotlib.pyplot as plt
def generarGrafica(dataFrame):
    #Agrupar datos del dataFrame segun el analisis que quiera graficar.
    #Estadisticas de un alimento (PAN) por un pais y su promedio al año
    preciosPromedioPais=dataFrame.groupby('Origen')['PrecioporUnidad'].mean()
    print(preciosPromedioPais)
    
    #0. Generando lista colores
    colores=["#33FFA8","#2B9C6C","#0D8042"]
    
    #1. Generar una figura
    plt.figure(figsize=(10,10))
    
    #2. Genero la grafica que deseo
    plt.bar(preciosPromedioPais.index, preciosPromedioPais.values, color=colores)
    
    #3. Agrego titulo a la tabla
    #Siembra de arboles por municipio
    plt.title("Ventas promedio de panes por paises")
    
    #4. Etiqueta o nombre del eje x
    plt.xlabel("Paises")
    
    #5. Etiqueta o nombre del eje y
    plt.ylabel("Precio Promedio")
    
    #6. Activar el grid
    plt.grid(True)
    
    #7. Rotar los labels
    plt.xticks(rotation=45)
    
    #7. Guardando nuestra grafica
    plt.savefig("./graphs/promediopanes.png")
    
    
    
    # Muestro la grafica
    #plt.show()