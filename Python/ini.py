#comentario corto, run terminal ctrl + h. Inicio de datos simples

print("Hola mundo!")

''' 
    comentario
    en
    varias
    lineas
          '''

''' print("hola mundo")
print(3 + 8) 

x = 7
n = 3

pi = 3.14
respuesta = True #boolean

print(type(pi)) #float

nombre = "luciano" #se crea
nombre = "Rodriguez" #se re define
nombre = "Adrian"
print(nombre)
edad = 31

#Concatenar con .format (ant.)
print("mi nombre es {} y tengo {} años" .format(nombre, edad)) #imprime segun como acomodemos el format
print("buenas, tengo {} años y me llamo {}" .format(edad, nombre))

nombre = True 
#Concatenacion
preg = ("verdadero o falso? ", "...", nombre )
print(preg)
bienvenido = "Hola " + " como estas?" #concatenar con +
bienvenido = (f"Hola {nombre} como estas? tenes {edad} años?") #concatenar con f-string
del nombre
print(bienvenido)
#operadores de pertenencia
print("ola" in bienvenido) #true por formar parte de bienvenida, en not in daria false. Es case sensitive

#lista, siemmpre inicia con []
list_vac = []
gatos = ["Rufina", "Ruffo", "Adolfo", "Tati"]
print(gatos[1])
gatos.append("Neko")
print(gatos)
print(gatos[1:3]) #entre los corchetes [x:y], es la manera de trozar un array
gatos.pop() #elimina la ultima variable 
print(gatos)
gatos.pop(3)
print(gatos)

#tupla (snake_case) siempre inicia con ()
frutos_secos = ("mani", "nueces","datiles","pistachos","almendras", 2)
#frutos_secos[2] = "castañas de caju" #no se puede alterar por lo que da Typeerror
print(frutos_secos[3])
frutas = "manzana", "frutilla", "naranja", "piña", "banana"
frutas = frutas + ("arandanos",) #agrega arandanos al final
print(frutas[1:]) #slicing

#diccionario, siempre inicia con {}
dic_vac = {}
persona = {'nombre': "Dalia", 'edad': 17, 'altura': 1.80, 'usa_lentes': False}
persona['nombre'] = "Azalea"  #actualiza si el valor de la llave existia
persona['hobbies'] = ["jugar videojuegos", "programación"] #agrega esa clave-valor si no existía previamente

print(persona) #imprime {'nombre': 'Azalea', 'edad': 17, 'altura': 1.8, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}

altura = persona.pop('altura')  #elimina la clave indicada y devuelve el valor
print(altura) #imprime 1.8
print(persona) #salida {'nombre': 'Azalea', 'edad': 17, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 

estudiante = {'nombre' : "Camelia", "Curso" : "4to", 'Promedio' : "9"} #notacion literal
continentes = {}
continentes['AME'] = "América"
continentes['ASI'] = "Asia"
continentes['EUR'] = "Europa"
continentes['AFR'] = "África"
continentes['OCE'] = "Oceanía"
print(continentes)

if "ANT" in continentes: #preguntamos si existe la clave
   print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
   continentes["ANT"] = "Antártida"
   #diccionario anidado
escuela = {
   "nombre": "Coding Dojo LATAM",
   "profesores": [
       {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
       {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
       {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
   ]
}

#len
print(len(persona)) #imprime 4 (la cantidad de pares de clave-valor)
print(len("Me encanta programar")) #imprime 20

import random
num_aleatorio = random.randint(5,10) #se importo el modulo random, selecciona un num al azar entre 5 y 10
print(num_aleatorio)
#numero real considerado complejo(complex)
print(type(5j))

#conversion
ent_a_dec = float(453)
dec_a_ent = int(72.5)
ent_a_compl = complex(81)

print(ent_a_dec) #imprime 453.0
print(dec_a_ent) #imprime 72
print(ent_a_compl) #imprime (81+0j)

#conversion de num a str
#print("¿Cuántos dedos tengo en la mano? " + 5) #error Typeerror: can only concatenate str (not "int") to str
print("¿Cuántos dedos tengo en la mano? " + str(5)) #imprime ¿Cuántos dedos tengo en la mano? 5

tiempo_preparacion = 1
tiempo_horneado = "2"
#tiempo_total = tiempo_preparacion + tiempo_horneado #Error: TypeError: unsupported operand type(s) for +: 'int' and 'str'
tiempo_total = tiempo_preparacion + int(tiempo_horneado) # Imprime: 3, creo que quedo claro...

#concatenar con %formatting
nombre = "Romeo"
print("mi nombre es %s y tengo %d años de edad." % (nombre, edad)) #imprime mi nombre es Romeo y tengo 31 años de edad. Ya no aguanto el true xd

#OTROS, metodos de cadenas integrados
cadena_de_texto= "Para ser mas sincero y certero, mi signo de Cancer es muy vulnerable para un Leo"
print(str.upper(cadena_de_texto)) #mayusculas
print(str.lower(cadena_de_texto)) #minusculas
#print(str.count(cadena_de_texto("sincero"))) no se
#print(str.split(cadena_de_texto)) no se
#string.split(caracter) no se
#string.find(substring) nop, inv
#string.isalnum nop, a inv
#string.join(lista) a inv
cadena_de_texto.endswith(("eo")) #regresa True o False si los últimos caracteres de la cadena coinciden con la subcadena. no regresa nada...

#array/lista otro_ejemplo
verso1 = ["fiesta", "fiesta", "pluma"]
verso2 = ["pluma", "gay"]
cancion = verso1 + verso2
estribillo = cancion * 3
print(estribillo) #si func, para ver el acceso a los valores volver a la linea 42 hasta la 50

# Lista de temperaturas diarias
temperaturas = [28, 21.5, 23.3, 22.2, 24.5, 32.7]
temperatura_media = sum(temperaturas) / len(temperaturas)
print("Temperatura media:", temperatura_media)

#Almacena datos que no deben cambiar, como coordenadas geográficas o dimensiones de un objeto/ tupla de coodernadas
coordenadas = (19.4326, -99.1332)  # Latitud y longitud de Ciudad de México

def calcular_distancia(coord1, coord2):
    # Implementación ficticia para calcular la distancia
    distancia = 10  # Solo un valor de ejemplo
    return distancia

distancia = calcular_distancia(coordenadas, (34.0522, -118.2437))
print("Distancia:", distancia)

#funcion tupla y return
def suma_y_multiplicacion(x, y):
   suma = x + y
   multiplicacion = x * y
   return (suma, multiplicacion)
suma_y_multiplicacion(5, 4)

# Diccionario con información sobre un conjunto de datos, para manipular/organizar
dataset_info = {
    "nombre": "Datos de ventas",
    "columnas": ["fecha", "producto", "cantidad", "precio"],
    "filas": 1000,
    "fuente": "Sistema de ventas interno"
}

print("Nombre del conjunto de datos:", dataset_info["nombre"])
print("Número de filas:", dataset_info["filas"])
'''
# ----------------------------------------------------nueva sección-----------------------------------------------------------
#FUNCIONES BASICAS
#1, funcion de cantidad de vocales, en consola muestra 5 a la hora de llamar a la funcion
'''
def cantidad_de_vocales():
    return 5

print(cantidad_de_vocales())

#2, cantidad de glaciares argentina es definida pero cantidad de dias o meses no por lo que tirara un error en consola
def cantidad_de_glaciares_argentina():
    return 16968
print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())

#3, la funcion toma la primer definicion y la otra no la procesa
def anio_independencia_chile():
    return 1810
    return 1851
print(anio_independencia_chile())

#4, lo mismo que el anterior, toma la primer definicion
def cantidad_de_departamentos_colombia():
    return(32)
    print(33)
print(cantidad_de_departamentos_colombia())

#5, retorna el valor, la llamada a la funcion se guarda en x (aunque tambien se muestra en consola el valor "none"
def altura_machu_picchu():
    print(2438)
x = altura_machu_picchu()
print(x)

#6, funcion de suma, genera 2 sumas y en  consola muestra las sumas independientes, no del conjunto
def suma(a, b):
    print(a+b)
print(suma(10, 5) + suma(4, 3))

#7, vuelve string cualquier valor que le ingresen en los parametros e imprime "157", debido al orden del return
def concatenar(a, b):
    return str(b) + str(a)
print(concatenar(7, 15))

#8, la funcion imprime el valor de a y luego retorna el resultado de la condicion if que es 46 sin darle entidad al return 21 que no corresponde
def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21
print(paises_latinoamerica_o_lenguas_indigenas())

#9, la primera vez que es llamada nos retorna 365 porque la condicion se cumple, la segunda retorna 12 y la tercera suma los retornos (365 + 12) dando 377
def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52
print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))

#10, sumatoria imprime 7
def sumatoria(a, b):
    return a + b
    return 157
print(sumatoria(3, 4))

#11, se imprime 150 3 veces y la anteultima vez que se llama imprime 350
a = 150
print(a)
def funcion():
    a = 350
    print(a)
print(a)
funcion()
print(a)

#12, lo mismo que el anterior
a = 150
print(a)
def funcion():
    a = 350
    print(a)
    return a
print(a)
funcion()
print(a)

#13, es similar a la anterior hasta que en a se guarda la llamada de la funcion y la ultima vez que se imprime a devuelve el valor de 350
a = 150
print(a)
def funcion():
    a = 350
    print(a)
    return a
print(a)
a = funcion()
print(a)

#14, cunado se llama a la funcion1, se imprime el 3 de la funcion1 y luego se llama a funcion2 para imprimir 1, para segir con el resto de la funcion1
def funcion1():
    print(3)
    funcion2()
    print(2)
def funcion2():
    print(1)
funcion1()
'''
#15, cuando se imprime b(osea, el llamado funcion1()), la funcion imprime 3, luego cuando se imprime a con la llamada guardada de funcion2(), se imprime 1 y retorna 0 para seuir con el resto de la funcion 1, retornando 4 en consola al final
def funcion1():
    print(3)
    a = funcion2()
    print(a)
    return 4
def funcion2():
    print(1)
    return 0
b = funcion1()
print(b)

# Crear un diccionario
edades = {'Alice': 25, 'Bob': 30, 'Carol': 22}

# Recorrer pares clave-valor del diccionario
for nombre, edad in edades.items():
    print(nombre, edad)

countries_capital = {
    "USA": "Washington D.C.",
    "Australia": "Canberra",
    "France": "Paris",
    "Egypt": "Cairo",
    "Japan": "Tokyo"
}

for country, capital in countries_capital.items():
    print(country, ":", capital)

