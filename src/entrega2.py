import csv
import math
from datetime import datetime
from collections import namedtuple

def hexadecimal_a_palabras(origen, destino) :
    """Lee un fichero en formato hexadecimal, y devuelve otro fichero con las palabras que hay en él.
    Para ello, divida cada línea considerando el espacio como separador, y luego convierta cada
    trozo de hexadecimal a palabra usando chr(int(trozo, 16)).

    Args:
        origen (str): Ruta hacia el fichero de origen.
        destino (str): Ruta hacia el fichero de destino.
    """
    with open(origen, encoding='utf-8') as f:
        with open(destino, mode='w', encoding='utf-8') as g:
            traducido = ""
            traducir = ""
            for linea in f:
                linea.strip()
                for i in linea:
                    if i == " ":
                        traducido += chr(int(traducir,16))
                        traducir = ""
                        continue
                    else:
                        traducir += i
                g.write(traducido)
    g.close()
    f.close()
'''
Esta función primero abre los dos ficheros con los que queremos trabajar (origen como f y destino como g),
lo que hace es recorrer todas las lineas del fichero origen una a una y para traducir de hexadecimal a 
palabra hemos creado dos variables llamadas "traducir" y "traducido" en traducir iremos metiendo todos
los caracteres que no sean cero para posteriormente almacenarlos a la variable traducido que ira sobreescribiendo el nuevo fichero.
'''  

Vivienda = namedtuple('Vivienda','fecha_construccion precio superficie habitaciones baños localidad vendido')

def lee_fichero(fichero):
    """Devuelve una lista de tuplas con nombre, con los datos del fichero.

    Args:
        fichero (str): Ruta hacia el fichero csv.

    Returns:
        list[Vivienda]: Lista de tuplas con los datos del fichero.
    """
    Viviendas = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for fecha_construccion,precio,superficie,habitaciones,baños,localidad,vendido in lector:
            fecha_construccion = datetime.strptime(fecha_construccion, "%Y-%m-%d").date()
            precio = int(precio)
            superficie = int(superficie)
            habitaciones = int(habitaciones)
            baños = int(baños)
            localidad = str(localidad)
            vendido = pasar_bool(vendido)
            tupla = Vivienda(fecha_construccion, precio, superficie, habitaciones, baños, localidad, vendido)
            Viviendas.append(tupla)
    return Viviendas
'''
Esta función consiste en que a cada una de las partes de la namedtuple le asignamos su valor
'''

def pasar_bool(valor):
    if valor == 'S':
        booleano = True
    else:
        booleano = False
    return booleano
'''
Esta funcion simplemente me transforma la S de la namedtuple en "True" mientras que la N me la transforma en "False"
'''

def num_años_meses_dias(viviendas):
    """
Devuelve el número de años, meses y días que han pasado desde la construcción 
de la vivienda más antigua hasta la construcción de la vivienda más reciente.

Args:
    vivendas (list[Vivienda]): Lista de viviendas.

Returns:
    tuple[int, int, int]: Número de años, meses y días que han pasado desde la construcción de la vivienda más antigua hasta la construcción de la vivienda más reciente.
"""
    fechas = []
    for i in viviendas:
            fechas.append(i.fecha_construccion)
    diferencia = int((max(fechas)-min(fechas)).days)
    dias = int(((diferencia%365)%30))
    meses = int((diferencia%365)/30)
    años = int(diferencia/365)
    return años,meses,dias
'''
Esta funcion se encarga de calcular la diferencia de años, meses y dias que hay entre la vivienda construida mas recientemente y la mas vieja y nos devuelve los valores en una tupla
'''

def precios_superficies(viviendas, localidad):
    """Devuelve una lista de tuplas (precio, superficie) de las viviendas de la localidad que se
pasa como parámetro. Suponemos que los precios del dataset están en dólares. Queremos que los
precios estén en euros. Suponga que un dólar equivale a 1.01 euros.

Args:
    viviendas (list[Vivienda]): Lista de viviendas.
    localidad (str): Localidad.
Returns:
    list[tuple[float, int]]: lista de tuplas (precio, superficie) de las viviendas de la localidad que se pasa como parámetro.
"""
    viviendas_localidad = []
    for i in viviendas:
        if i.localidad == localidad:
            viviendas_localidad.append((i.precio*1.01,i.superficie))
        else:
            continue
    return viviendas_localidad
'''
Esta funcion nos devuelve una tupla con el precio por superficie de las viviendas de la localidad que introduzcamos como parametro.
'''

def buena_compra(viviendas, localidades):
    """Devuelve la mejor vivienda de entre las viviendas de las localidades que se pasan como parámetro.
    La mejor vivienda, es aquella que tiene el precio por metro cuadrado más bajo de entre
    las consideradas como buenas compras.
    Se supone que una compra es buena, cuando la relación entre el precio y la superficie de una compra
    es inferior al precio medio por metro cuadrado de la localidad. 
    El precio medio de cada localidad, viene dado por el diccionario 'precios'.

    Args:
        viviendas (list[Vivienda]): Lista de viviendas.
        localidades (set[str]): Conjunto de localidades.

    Returns:
        Vivienda: Mejor vivienda de entre las viviendas de las localidades que se pasan como parámetro.
"""
    precios={'Michaelshire': 1000, 'Spencerberg': 1200, 'Port Travismouth': 1500, 'Knightview': 1800, 'Mistyville': 1900, 'Shawnfurt': 900}
    buenas_compras = []
    for i in viviendas:
        if i.localidad == i.localidad in localidades:
            relacion = i.precio/(i.superficie)
            if relacion<precios[i.localidad]:
                buenas_compras.append(i)
    return min(buenas_compras)
'''
Lo que realiza esta funcion es que segun las localidades que le demos como parametro, nos devuelve la mejor vivienda con el precio/superficie más bajo, es decir, la mejor compra.
'''

def distancia(v1, v2):
    """calcula la distancia entre dos viviendas. Para ello: 
    - calcula la distancia euclídea de las características numéricas
    - calcula la distancia entre las fechas como se describe a continuación. 
      La distancia entre dos fechas se calcula como el número de días que han pasado desde la fecha 
      más antigua hasta la fecha más reciente.
    - suma las dos distancias anteriores y devuelve el resultado.

    Args:
        v1 (Vivienda): Vivienda 1.
        v2 (Vivienda): Vivienda 2.

    Returns:
        float: Distancia entre las dos viviendas.
    """
    distancia_euclidea = math.sqrt((v1.precio-v2.precio)**2+(v1.superficie-v2.superficie)**2+(v1.habitaciones-v2.habitaciones)**2+(v1.baños-v2.baños)**2)
    distancia_temporal = abs(int((v1.fecha_construccion-v2.fecha_construccion).days))
    distancia = distancia_euclidea+distancia_temporal
    return distancia
'''
Esta funcion se encarga de calcular la distancia entre dos viviendas que le pasemos como parametro.
'''

def vivienda_mas_parecida(viviendas, vivienda):
    """Devuelve la vivienda más parecida a la que se pasa como parámetro.  
    Las viviendas deben pertenecer a distintas localidades, y la vivienda resultante, no
    puede estar vendida.

    Args:
        viviendas (list[Vivienda]): Lista de viviendas.
        vivienda (Vivienda): Vivienda.

    Returns:
        Vivienda: Vivienda más parecida a la que se pasa como parámetro.
    """
    lista_distancias = {}
    for i in viviendas:
        if i.localidad != vivienda.localidad and i.vendido == False:
            lista_distancias[distancia(vivienda,i)] = i
        else:
            continue
    menor_distancia = min(lista_distancias.keys())
    mas_parecida = lista_distancias.get(menor_distancia)
    return mas_parecida
'''
Esta funcion simplemente nos devolverá la vivienda que más se parezca a la que hemos introducido como parametro de entre todas las que se encuentrasn en el archivo csv.
'''