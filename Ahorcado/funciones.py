import string
import unicodedata
from random import choice

def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''

    with open(archivo,'r') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla:str)->dict:
    '''
    Carga las plantillas del juego a partir de un archivo de texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./Plantilla/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel >= 0 and nivel <=5:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

def obten_palabras(lista:list)->list:
    '''
    Obtiene las palabras de un texto
    '''
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    #convertimos a minusculas
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    #removemos signos de puntuacion y caracteres especiales
    set_palabras = {palabra.strip(string.punctation) for palabra in set_palabras}
    #removemos numeros, parentesis, corchetes y otros caracteres
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    #removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii','ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)

if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla, 5)
    lista_oraciones = carga_archivo_texto('./Datos/plantilla.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)