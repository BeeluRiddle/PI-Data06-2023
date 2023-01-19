#Importo dependencias/librerías necesarias
from fastapi import FastAPI
import pandas as pd
from pandasql import sqldf
import os
os.environ["OPENBLAS_L2SIZE"]="512k"

#creo una instancia de FastAPI
app = FastAPI()

#----------Carta de presentación----------
@app.get("/")
def presentacion():
    return "Proyecto Individual 01 - Zapata, María Belén. Gracias por testear mi api!"

@app.get("/contacto")
def contacto():
    return "Email: mariabelenzapata6@gmail.com / Github: BeeluRiddle"

@app.get("/menu")
def menu():
    return ("Funciones de mi API: (1) get_word_count (2) get_score_count (3) get_second_score (4) get_longest (5) get_rating_count ")

#----------QUERIES----------

#Consigna 1: Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get("/get_word_count/{plataforma}/{keyword}")
def get_word_count(plataforma: str, keyword: str):
    # lectura de la base de datos:
    df = pd.read_csv("https://raw.githubusercontent.com/BeeluRiddle/pi-movies-database/main/movies_completo.csv")
    
    #Definición de las plataformas:
    if plataforma == "amazon":
        plat = "a%"
    elif plataforma == "disney":
        plat = "d%"
    elif plataforma == "hulu":
        plat = "h%"
    elif plataforma == "netflix":
        plat = "n%"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")
    
    #QUERY:
    query = f"SELECT COUNT(title) FROM df WHERE title LIKE '%{keyword}%' AND id LIKE '{plat}'"
    #Se guarda el resultado en una nueva variable, dándole el formato sql:
    result = sqldf(query)
    
    #Se verifica el contenido de la variable. En caso de no estar vacío:
    if not result.iloc[0,0] == 0:
        return result.to_dict() #retorna los datos solicitados en la consulta, como un diccionario.
    #Si la variable no tiene contenido:
    else:
        return ("No se pudo encontrar la keyword solicitada.")


#Consigna 2: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
@app.get("/get_score_count/{plataforma}/{puntaje}/{ano}")
def get_score_count(plataforma: str, puntaje: int, ano: int):
    #lectura de la base de datos:
    df = pd.read_csv("https://raw.githubusercontent.com/BeeluRiddle/pi-movies-database/main/movies_completo.csv")
    
    #Defino las plataformas:
    if plataforma == "amazon":
        plat = "a%"
    elif plataforma == "disney":
        plat = "d%"
    elif plataforma == "hulu":
        plat = "h%"
    elif plataforma == "netflix":
        plat = "n%"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")
    
    #Fuerzo el cambio a str
    puntaje = str(puntaje)
    ano = str(ano)

    #QUERY:
    query = f"SELECT COUNT(title) FROM df WHERE id LIKE '{plat}' AND type == 'movie' AND score > {puntaje} AND release_year == {ano}"
    #Se guarda el resultado en una nueva variable, dándole el formato sql:
    result = sqldf(query)
    
    #Se verifica el contenido de la variable "result". En caso de no estar vacío:
    if not result.iloc[0,0] == 0:
        return result.to_dict() #retorna los datos solicitados en la consulta, como un diccionario.
    #Si la variable no tiene contenido:
    else:
        return ("No hay peliculas con ese puntaje, en ese año, en esta plataforma.")


#Consigna 3: La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
@app.get("/get_second_score/{plataforma}")
def get_second_score(plataforma: str):
    #lectura de la base de datos:
    df = pd.read_csv("https://raw.githubusercontent.com/BeeluRiddle/pi-movies-database/main/movies_completo.csv")
    
    #Defino las plataformas:
    if plataforma == "amazon":
        plat = "a%"
    elif plataforma == "disney":
        plat = "d%"
    elif plataforma == "hulu":
        plat = "h%"
    elif plataforma == "netflix":
        plat = "n%"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")
    
    #QUERY:
    query = f"SELECT title FROM df WHERE id like '{plat}' and type=='movie' ORDER BY score DESC, title LIMIT 1 OFFSET 1"
    #Se guarda el resultado en una nueva variable, dándole el formato sql:
    result = sqldf(query)

    # Se verifica el contenido de la variable "result". En caso de no estar vacío:
    if not result.iloc[0,0] == 0:
        return result.to_dict() #retorna los datos solicitados en la consulta, como un diccionario.
    #Si la variable no tiene contenido:
    else:
        return ("No se han encontrado peliculas.")

#Consigna 4: Película que más duró según año, plataforma y tipo de duración
@app.get("/get_longest/{plataforma}/{duration_type}/{ano}")
def get_longest(plataforma: str, duration_type: str, ano: int):
    #lectura de la base de datos:
    df = pd.read_csv("https://raw.githubusercontent.com/BeeluRiddle/pi-movies-database/main/movies_completo.csv")
    
    #Defino las plataformas:
    if plataforma == "amazon":
        plat = "a%"
    elif plataforma == "disney":
        plat = "d%"
    elif plataforma == "hulu":
        plat = "h%"
    elif plataforma == "netflix":
        plat = "n%"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")
    
    #QUERY:
    query = f"SELECT title, release_year, duration_int, duration_type FROM df WHERE id like '{plat}' and release_year='{ano}' and duration_type='{duration_type}' ORDER BY duration_int DESC LIMIT 1"
    #Se guarda el resultado en una nueva variable, dándole el formato sql:
    result = sqldf(query)
    
    #Se verifica el contenido de la variable "result". En caso de no estar vacío:
    if not result.iloc[0,0] == 0:
        return result.to_dict() #retorna los datos solicitados en la consulta, como un diccionario.
    #Si la variable no tiene contenido:
    else:
        return ("No se han encontrado peliculas.")

#Consigna 5: Cantidad de series y películas por rating
@app.get("/get_rating_count/{rating}")
def get_rating_count(rating: object):
    #lectura de la base de datos:
    df = pd.read_csv("https://raw.githubusercontent.com/BeeluRiddle/pi-movies-database/main/movies_completo.csv")

    #QUERY:
    query = f"SELECT rating, count(*) as count FROM df WHERE rating = '{rating}' GROUP BY rating"
    #Se guarda el resultado en una nueva variable, dándole el formato sql:
    result = sqldf(query)
    
    #Se verifica el contenido de la variable "result". En caso de no estar vacío:
    if not result.iloc[0,0] == 0:
        return result.to_dict() #retorna los datos solicitados en la consulta, como un diccionario.
    #en caso de que no se encuentre el rating solicitado:
    else:
        return("No se ha encontrado ese rating.")