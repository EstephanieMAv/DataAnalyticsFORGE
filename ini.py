#comentario corto, run terminal ctrl + h. Inicio de datos simples

''' 
    comentario
    en
    varias
    lineas
          '''

''' print("hola mundo")
print(3 + 8) '''

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

#tupla (snake_case)
frutos_secos = ("mani", "nueces","datiles","pistachos","almendras", 2)
#frutos_secos[2] = "castañas de caju" #no se puede alterar por lo que da Typeerror
print(frutos_secos[3])
frutas = "manzana", "frutilla", "naranja", "piña", "banana"
futras = frutas + "arandanos" #agrega arandanos al final
print(frutas[1:]) #slicing

#diccionario
dic_vac = {}
persona = {'nombre': "Dalia", 'edad': 17, 'altura': 1.80, 'usa_lentes': False}
persona['nombre'] = "Azalea"  #actualiza si el valor de la llave existe
persona['hobbies'] = ["jugar videojuegos", "programación"] #agrega esa clave-valor si no existía previamente

print(persona) #imprime {'nombre': 'Azalea', 'edad': 17, 'altura': 1.8, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}

altura = persona.pop('altura')  #elimina la clave indicada y devuelve el valor
print(altura) #imprime 1.8
print(persona) #salida {'nombre': 'Azalea', 'edad': 17, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 

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



