import os
import argparse
import requests
import csv

def cargar_csv(nombre_archivo):
    frases_peliculas = []
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector)  # Saltar encabezado
        for fila in lector:
            if len(fila) >= 2:
                frase, pelicula = fila[0], fila[1]
                frases_peliculas.append((frase, pelicula))
        return frases_peliculas

def buscar_palabra(palabra, frases_peliculas):
    palabra = palabra.lower()
    encontrados = []
    for frase, pelicula in frases_peliculas:
        if palabra in frase.lower():
            encontrados.append((frase, pelicula))
    return encontrados

if __name__ == '__main__':
    nombre_archivo = "frases.csv" 
    frases_peliculas = cargar_csv(nombre_archivo)
    palabra_buscada = input("Ingresa una palabra para buscar en las frases: ")
    resultados = buscar_palabra(palabra_buscada, frases_peliculas)

    if resultados:
        print("\nFrases encontradas:")
        for frase, pelicula in resultados:
            print(f"\"{frase}\" - {pelicula}")
    else:
        print("No se encontró la palabra en ninguna frase.")

