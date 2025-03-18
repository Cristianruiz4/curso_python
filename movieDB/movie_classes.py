''' Clases para manejar la base de datos de peliculas '''
import csv
import os
import hashlib
import datetime

class Actor:
    ''' Clase para manejar la informacion de un actor '''
    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, username):
        self.id_estrella        = id_estrella
        self.nombre             = nombre
        self.fecha_nacimiento   = fecha_nacimiento
        self.ciudad_nacimiento  = ciudad_nacimiento
        self.url_imagen         = url_imagen
        self.username           = username
    
    def to_dict(self):
        ''' Devuelve un diccionario con la información del actor '''
        return {
            'id_estrella': self.id_estrella,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'ciudad_nacimiento': self.ciudad_nacimiento,
            'url_imagen': self.url_imagen,
            'username': self.username
        }   

class Pelicula:
    ''' Clase para manejar la informacion de una pelicula '''
    def __init__(self, id_pelicula, titulo_pelicula, fecha_lanzamiento, url_poster):
        ''' Inicializa la clase con los datos de al pelicula '''
        self.id_pelicula        = id_pelicula
        self.titulo_pelicula    = titulo_pelicula
        self.fecha_lanzamiento  = datetime.strftime(fecha_lanzamiento, "%Y-%m%-%d").date()
        self.url_poster         = url_poster
        
    def to_dict(self):
        ''' Devuelve un diccionario con la infrmacion de la pelicula '''
        return{
            'id_pelicula' : self.id_pelicula,
            'titulo_pelicula' : self.titulo_pelicula,
            'fecha_lanzamiento' : self.fecha_lanzamiento.strftime("%Y-%m%-%d"),
            'url_poster' : self.url_poster
        }

class Relacion:
    def __init__(self, id_relacion, id_pelicula, id_estrella):
        ''' Inicializa la clase para manejar la informacion entre actores y peliculas '''
        self.id_relacion        = id_relacion,
        self.id_pelicula        = id_pelicula,
        self.id_estrella        = id_estrella

    def to_dict(self):
        ''' Devuelve un diccionario con la informacion entre actores y peliculas '''
        return{
            'id_relacion' : self.id_relacion,
            'id_pelicula' : self.id_pelicula,
            'id_estrella' : self.id_estrella
        }
    
class User:
    ''' Clase para manejar la informacion de un usuario '''
    def __init__(self, username, nombre_completo, email, password, admin):
        self.username       =username,
        self.nombre_completo = nombre_completo,
        self.email          = email,
        self.password       = password,
        self.admin          = admin
    
    def to_dict(self):
        ''' Devuelve un diccionario con la información del usuario '''
        return {
            'username': self.username,
            'nombre_completo': self.nombre_completo,
            'email': self.email,
            'password': self.password,
            'admin': self.admin
        }

    def hash_string(self, string):
        ''' Devuelve el hash de un string '''
        return hashlib.sha256(string.encode()).hexdigest()

class SistemaCine:
    def __init__(self):
        ''' Inicializa la clase con los datos de tu base de datos '''
        self.actores = {}
        self.peliculas = {}
        self.relaciones = {}
        self.usuarios = {}

    def cargar_csv(self, archivo, clase):
        ''' Carga los datos de un archivo CSV a la base de datos '''
        with open(archivo, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if clase == Actor:
                    actor = Actor(**row)
                    self.actores[actor.id_estrella] = actor
                elif clase == Pelicula:
                    pelicula = Pelicula(**row)
                    self.peliculas[pelicula.id_pelicula] = pelicula
                elif clase == Relacion:
                    relacion = Relacion(**row)
                    self.relaciones[relacion.id_relacion] = relacion
                elif clase == User:
                    user = User(**row)
                    self.usuarios[user.username] = user

if __name__ == '__main__':
    archivo_actores = "datos/movies_db - actores.csv"
    archivo_peliculas = "datos/movies_db - peliculas.csv"
    archivo_relaciones = "datos/movies_db - relacion.csv"
    archivo_usuarios = "datos/usuarios.csv - usuarios.csv"
    sistema = SistemaCine()
    sistema.cargar_csv(archivo_actores, Actor)
    sistema.cargar_csv(archivo_peliculas, Pelicula)
    sistema.cargar_csv(archivo_relaciones, Relacion)
    sistema.cargar_csv(archivo_usuarios, User)
    actores = sistema.actores
    for id_estrella, actor in actores.items():
        print(f"{id_estrella}: {actor.nombre:35s} - {actor.fecha_nacimiento}")