''' Program principal de MovieDB '''
from flask import Flask, render_template, request, redirect, url_for
import random
import os
import movie_classes as mc
 
app = Flask(__name__)
sistema = mc.SistemaCine()
ruta = 'datos/movies_db - '
actores_csv = ruta + 'actores.csv'
peliculas_csv = ruta + 'peliculas.csv'
relaciones_csv = ruta + 'relacion.csv'
users_csv = ruta + 'users_hashed.csv'
sistema.cargar_csv(actores_csv,mc.Actor)
sistema.cargar_csv(peliculas_csv,mc.Pelicula)
sistema.cargar_csv(relaciones_csv,mc.Relacion)
sistema.cargar_csv(users_csv,mc.User)
 
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/actores')
def actores():
    actores = sistema.actores.values()
    return render_template('actores.html', actores=actores)

@app.route('/peliculas')
def peliculas():
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)
 
if __name__ == '__main__':
    app.run(debug=True)
