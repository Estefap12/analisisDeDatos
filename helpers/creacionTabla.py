import pandas as pd
from bs4 import BeautifulSoup

def crearTabla(dataFrame,nombreHTML):
    
    #Obtener una tabla de HTML desde un dataFrame de python
    archivoHTML=dataFrame.to_html()
    
    #Definir la ruta donde se va a guardar esa tabla
    rutaArchivo=f"tables/{nombreHTML}.html"
    
    #Construir un encabezado <head> del archivo generado
    encabezadoHTML='''
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
          </head>
          <body>
    '''
    #Utilizo BS4 para optimizar mi tabla
    sopa=BeautifulSoup(archivoHTML,'html.parser')
    
    #Encontrar todas las filas 'tr' eliminar atributo style
    for tr in sopa.find_all('tr'):
        tr.attrs.pop('style',None)
        
    archivoHTML=str(sopa)
    
    #Agregar la clase Table y Table striped de bootstrap
    archivoHTML=archivoHTML.replace('<table border="1" class="dataFrame">','<table class="table table-striped">')
    
    #Escribir la tabla y generarla en el proyecto
    with open(rutaArchivo,"w") as archivo:
        archivo.write(f"{encabezadoHTML}\n{archivoHTML}\n</body>\n</html>")
    