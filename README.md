# Entrega 2 #
Siga los siguientes pasos:

1. Cree dos módulos en el directorio `src` de su proyecto: `entrega2.py` y `entrega2_test.py`. En el primero irán las funciones que usted implemente, y en el segundo irán las pruebas correspondientes. 

2. Implemente una función con la siguiente cabecera:
```
def hexadecimal_a_palabras(origen, destino) :
    """Lee un fichero en formato hexadecimal, y devuelve otro fichero con las palabras que hay en él.
    Para ello, divida cada línea considerando el espacio como separador, y luego convierta cada
    trozo de hexadecimal a palabra usando chr(int(trozo, 16)).

    Args:
        origen (str): Ruta hacia el fichero de origen.
        destino (str): Ruta hacia el fichero de destino.
    """  
```
3. Una vez realizado el paso anterior, aplique la función al fichero `codificado.txt` y guarde el resultado en el fichero `dataset.csv` (ambos en la carpeta `data`). A partir de aquí, trabajaremos con el fichero `dataset.csv`.
4. Cree la namedtuple: 
```
Vivienda=namedtuple('Vivienda', 'fecha_construccion precio superficie habitaciones baños localidad vendido')
```	
donde `fecha_construccion` es un objeto `date`, `precio` es un `int`, `superficie` es un `int`, `habitaciones` es un `int`, `baños` es un `int`, `localidad` es un `str`, y `vendido` es un `bool`.
***
**IMPORTANTE:** El acceso a los elementos de toda variable o parámetro de tipo `Vivienda`, debe hacerse con el operador punto, es decir, `vivienda.fecha_construccion` en lugar de `vivienda[0]`. 

**IGNORAR ESTE AVISO, CONLLEVARÁ EL SUPENSO DE ESTA ENTREGA**
***
5. Implemente las siguientes funciones:
```
def lee_fichero(fichero):
    """Devuelve una lista de tuplas con nombre, con los datos del fichero.

    Args:
        fichero (str): Ruta hacia el fichero csv.

    Returns:
        list[Vivienda]: Lista de tuplas con los datos del fichero.
    """
```   
```  
def num_años_meses_dias(vivendas):
    """Devuelve el número de años, meses y días que han pasado desde la construcción 
    de la vivienda más antigua hasta la construcción de la vivienda más reciente.

    Args:
        vivendas (list[Vivienda]): Lista de viviendas.

    Returns:
        tuple[int, int, int]: Número de años, meses y días que han pasado desde la construcción de la vivienda más antigua hasta la construcción de la vivienda más reciente.
    """
```
``` 
def precios_superficies(viviendas, localidad):
    """ Devuelve una lista de tuplas (precio, superficie) de las viviendas de la localidad que se
    pasa como parámetro. Suponemos que los precios del dataset están en dólares. Queremos que los
    precios estén en euros. Suponga que un dólar equivale a 1.01 euros.

    Args:
        viviendas (list[Vivienda]): Lista de viviendas.
        localidad (str): Localidad.
    Returns:
        list[tuple[float, int]]: lista de tuplas (precio, superficie) de las viviendas de la localidad que se pasa como parámetro.
    """
```
```
precios={'Michaelshire': 1000, 'Spencerberg': 1200, 'Port Travismouth': 1500, 'Knightview': 1800, 'Mistyville': 1900, 'Shawnfurt': 900}

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
```
```
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
```
```
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
```
A continuación, se muestra la salida esperada de las funciones implementadas:
```
los 3 primeros registros:

Vivienda(fecha_construccion=datetime.date(2019, 2, 12), precio=380484, superficie=285, habitaciones=5, baños=2, localidad='Michaelshire', vendido=False)
Vivienda(fecha_construccion=datetime.date(2019, 6, 19), precio=131637, superficie=250, habitaciones=2, baños=2, localidad='Spencerberg', vendido=False)
Vivienda(fecha_construccion=datetime.date(2015, 7, 15), precio=990501, superficie=276, habitaciones=2, baños=2, localidad='Port Travismouth', vendido=False)

los 3 últimos registros:

Vivienda(fecha_construccion=datetime.date(2018, 6, 1), precio=327631, superficie=348, habitaciones=2, baños=3, localidad='Whitetown', vendido=False)
Vivienda(fecha_construccion=datetime.date(2015, 3, 26), precio=203233, superficie=128, habitaciones=4, baños=2, localidad='Brandyville', vendido=False)
Vivienda(fecha_construccion=datetime.date(2019, 12, 24), precio=726134, superficie=58, habitaciones=1, baños=2, localidad='Laurieshire', vendido=False)
#############################################################################################################

Probando num_años_meses_dias

8 años, 12 meses y 1 días
#############################################################################################################

Probando precios_superficies de la localidad 'Michaelshire' (en €)

[(384288.84, 285), (847862.68, 118)]
#############################################################################################################

Probando buena_compra de las localidades 'Michaelshire', 'Spencerberg', 'Port Travismouth'

Vivienda(fecha_construccion=datetime.date(2019, 6, 19), precio=131637, superficie=250, habitaciones=2, baños=2, localidad='Spencerberg', vendido=False)
#############################################################################################################

Probando vivienda_mas_parecida de la vivienda  Vivienda(fecha_construccion=datetime.date(2019, 2, 12), precio=380484, superficie=285, habitaciones=5, baños=2, localidad='Michaelshire', vendido=False)

Vivienda(fecha_construccion=datetime.date(2021, 10, 10), precio=380352, superficie=491, habitaciones=3, baños=1, localidad='Smithport', vendido=False)
```	






