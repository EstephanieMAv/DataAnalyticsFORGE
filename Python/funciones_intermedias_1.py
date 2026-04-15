'''
1. Actualizar valores en diccionarios y listas
Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ] LISTO
Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales” LISTO
En ciudades, cambia “Cancún” por “Monterrey” LISTO
En las coordenadas, cambia el valor de “latitud” por 9.9355431 LISTO
 

2. Iterar a través de una lista de diccionarios LISTO
Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente.
 

3. Obtener valores de una lista de diccionarios LISTO

Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:

4. Iterar a través de un diccionario con valores de lista

Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave. 
Crea el archivo un Python llamado funciones_intermedias_1.py
Actualiza los valores en diccionarios y listas
Crea la función iterarDiccionario(lista)
Crea la función iterarDiccionario2(llave, lista)
Crea la función imprimirInformacion(diccionario)

#1
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1][0]= 6 #+1
print(matriz)

cantantes[0]['nombre'] = "Enrique Martin Morales" #+1
print(cantantes)

ciudades['México'][2] = "Monterrey"
print(ciudades)

coordenadas[0]['latitud'] = 9.9355431
print(coordenadas)

cantantes = [
    {'nombre': "Ricky Martin", 'pais': "Puerto Rico"},
    {'nombre': "Chayanne", 'pais': "Puerto Rico"},
    {'nombre': "José José", 'pais': "México"},
    {'nombre': "Juan Luis Guerra", 'pais': "República Dominicana"}
]

def iterarDiccionario(cantantes):
    veces_recorridas = 0
    for cantante in cantantes:
        veces_recorridas += 1
        print(f"{veces_recorridas} - Nombre ", cantante['nombre'], " - PAIS ", cantante['pais'])

iterarDiccionario(cantantes)
#BONUS: Que aparezcan en este formato:
#nombre - Ricky Martin, pais - Puerto Rico
#nombre - Chayanne, pais - Puerto Rico
#nombre - José José, pais - México
#nombre - Juan Luis Guerra, pais - República Dominicana

for cantante in cantantes:
    print(cantante['nombre'])

for cantante in cantantes:
    print(cantante['pais'])
'''
costa_rica = {
    'ciudades': ["San José", "Limón", "Cartago", "Puntarenas"],
    'comidas' : ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimir_informacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}") #saca la cantidad/tamaño y la clave recorrida convirtiendola es mayusculas
        #para imprimir cada elemento, como me costo uuu
        for elemento in lista:
            print(elemento)
        print(" ") #separacion
        
imprimir_informacion(costa_rica)
#esto lo hago pa' divertirme pa' divertirme y para conseguir la beca por supuesto
'''
#imprime:
4 CIUDADES
San José
Limón
Cartago
Puntarenas

5 COMIDAS
gallo pinto
casado
tamales
chifrijo
olla de carne
'''
