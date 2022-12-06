# Funcion para ordenar un diccionario por un parametro en especifico con funcion lambda.
# Function to sort a dictionary by a specific parameter with lambda function.


def obtenerCsvOrdenado(nombreArchivo):
    separador = ";" #Separador utilizado en el archivo CSV / Separator used in the CSV file 
    with open (nombreArchivo) as archivo:
        next (archivo)
        datos = []
        
        for linea in archivo:
            linea = linea.strip("\n")
            columnas = linea.split(separador)
            ani= columnas[0]
            type_operation= columnas[1]
            idBo = columnas[2]
            datos.append({
                'ani': ani,
                'type_operation': type_operation,
                'idBo' : idBo,
        })

       
        return sorted(datos, key = lambda i: i['idBo'])
