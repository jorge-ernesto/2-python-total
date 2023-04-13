'''
Explicación requests y urllib

Tanto requests como urllib son bibliotecas de Python para hacer solicitudes HTTP y trabajar con recursos web, pero hay algunas diferencias importantes entre ellas.
requests es una biblioteca de Python de terceros que proporciona una interfaz de alto nivel para enviar solicitudes HTTP. Es una biblioteca muy popular porque es fácil de usar y muy potente. requests está diseñado para ser simple, pero también flexible y extensible.
urllib, por otro lado, es una biblioteca de Python incorporada que se utiliza para trabajar con recursos web. Proporciona varias submódulos para diferentes operaciones relacionadas con la red, como urllib.request para realizar solicitudes HTTP, urllib.parse para analizar URL y urllib.error para manejar errores relacionados con la red. Aunque es una biblioteca incorporada, puede ser más complicado de usar que requests.
En resumen, ambas bibliotecas se pueden utilizar para realizar solicitudes HTTP y trabajar con recursos web, pero requests es más fácil de usar y más popular, mientras que urllib es una biblioteca incorporada con más submódulos y características para manejar tareas de red.
'''

# modulos necesarios para web scraping
import bs4            # biblioteca que facilita extraer información de páginas web
import requests       # biblioteca HTTP simple pero elegante
import urllib.request # biblioteca extensible para abrir URLs



# lista de fotos
list_fotos = []



# obtenemos contenido
with open("./contenido/contenido.txt", encoding="utf-8") as archivo:
    contenido = archivo.read()

# crear sopa
sopa = bs4.BeautifulSoup(contenido, 'lxml')

# verificar
# print("Resultado text:", contenido)
# print("Sopa:"          , sopa)

# seleccionar datos de las fotos
fotos = sopa.select('a.x1i10hfl.xjbqb8w.x6umtig')

# iterar fotos
for index, foto in enumerate(fotos):
    # print('index', index)
    # print('photo', foto)

    # seleccionar img
    img = foto.select_one('img') # select_one se puede utilizar para seleccionar un solo elemento en Beautiful Soup. Si la consulta devuelve varios elementos, se devuelve solo el primero. Si la consulta no devuelve ningún elemento, se devuelve None.

    # verificar que exista una etiqueta img
    if img:
        # guardar url en variable
        url = img['src']

        # agregar url a la lista
        list_fotos.append(url)
    else:
        print('No se encontró la imagen en la foto', index)

# verificar
# print('list_fotos', list_fotos)

# iterar fotos
for index, foto in enumerate(list_fotos):
    print('index', index)
    print('photo', foto)

    # guardar imagen a partir de una url usando urllib
    url = foto
    filename = f"C:\\Users\\Ernesto\\Downloads\\fotos_fb\\imagen_{index}.jpg"

    urllib.request.urlretrieve(url, filename)
