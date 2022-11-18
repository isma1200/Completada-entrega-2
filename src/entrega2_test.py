from entrega2 import *

hexadecimal_a_palabras("./data/codificado.txt","./data/dataset.csv")

Viviendas = lee_fichero("./data/dataset.csv")
print(Viviendas[:3])
print(Viviendas[-3:])


Distancia_temporal = num_años_meses_dias(Viviendas)
print(f"{Distancia_temporal[0]} años, {Distancia_temporal[1]} meses y {Distancia_temporal[2]} dias")


localidad = input("¿En que localidad desea buscar viviendas?: ")
calle = precios_superficies(Viviendas,localidad)
print(calle)


localidades = set({'Michaelshire','Spencerberg','Port Travismouth'})
Vivienda = buena_compra(Viviendas,localidades)
print(Vivienda)


vivienda = Viviendas[0]
vivienda_igual = vivienda_mas_parecida(Viviendas,vivienda)
print(vivienda_igual)