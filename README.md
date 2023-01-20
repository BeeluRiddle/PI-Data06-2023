## Proyecto Individual - Data Engineer 
_Ingeniera: Zapata, María Belén_

> En este README encontrarán toda la documentación, e instrucciones necesarias, para poder utilizar la API que se me solicitó desarrollar.

[Video explicativo](https://youtu.be/rLUn2rhO37s)

:purple_circle: **MENU:** :purple_circle:
* **Datasets_RAW** - _las bases de datos que recibí para trabajar._
* **pycache** - _carpeta necesaria para el funcionamiento de la api._
* **PI01_Queries.ipynb** - _notebook con pruebas de las queries._
* **PI01_Transformación de Datos.ipynb** - _paso a paso del ETL._
* **README** - _Instrucciones de uso._
* **main.py** - _el código de la API._
* **movies_completo.csv** - _el csv que se utiliza para las consultas._ 
* **requirements.txt** - _dependencias necesarias para que funcione._
 
:purple_circle: **Las funciones que componen la API son:** :purple_circle:

:small_blue_diamond: Conteo de palabras clave, por plataforma. <br>
:small_blue_diamond: Conteo de peliculas, por año, plataforma y puntuación. <br>
:small_blue_diamond: Segunda película mejor puntuada en la plataforma seleccionada. <br>
:small_blue_diamond: Película de mayor duración, por plataforma y por año. <br>
:small_blue_diamond: Cantidad de películas con determinada clasificación. <br>

:purple_circle: **Cómo escribir cada función en el navegador:** :purple_circle: 

:white_medium_small_square: https://twj1kq.deta.dev/get_word_count/{plataforma}/{keyword} <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_score_count/{plataforma}/{puntaje}/{ano} <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_second_score/{plataforma} <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_longest/{plataforma}/{duration_type}/{ano} <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_rating_count/{rating} <br>

:purple_circle: **Queries de ejemplo para probar la api** :purple_circle: 

:white_medium_small_square: https://twj1kq.deta.dev/get_word_count/netflix/love <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_score_count/netflix/85/2010 <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_second_score/amazon <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_longest/netflix/min/2016 <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_rating_count/18+ <br>

:warning: **Sintaxis a tener en cuenta al escribir una consulta:** :warning:<br>
:small_blue_diamond: Todo debe estar escrito en minúsculas.  <br>
:small_blue_diamond: Las plataformas que admite son: Amazon, Disney, Hulu y Netflix. <br>
:small_blue_diamond: Evite utilizar caracteres hispanos. <br>
:small_blue_diamond: En caso de la query no arroje resultados, un mensaje explicativo se imprimirá en pantalla.<br>
:small_blue_diamond: En caso de que se ingrese una plataforma inválida, un mensaje explicativo se imprimirá en pantalla. <br>

:purple_circle: **Funciones extra** :purple_circle: <br>
:small_blue_diamond: Función _Presentación_: `/` <br>
Simplemente invocando el link vacío, muestra el nombre y a quien pertenece la api.<br>
:small_blue_diamond: Función _menú_: `/menu` <br>
Muestra una lista de las funciones disponibles para consultar. <br>
:small_blue_diamond: Función _Contacto_: `/contacto`<br>
Muestra dos maneras de contactar conmigo, en caso de necesidad. <br>
:small_blue_diamond: Función _docs_: `/docs` <br>
Muestra el menú principal de la api, donde también se puede testear las consultas.<br>

:purple_circle: **Notas finales:** :purple_circle:<br>
:innocent: Muchas gracias por testear mi api! <br> 
Todo el feedback es bien recibido. :coffee: