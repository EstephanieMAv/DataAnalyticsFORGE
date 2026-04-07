numero1 = 70 #tipo numero entero
numero2 = 3.14 #tipo numero natural/float
booleano = False #buleano, verdadero o falso
cadena = 'Hola Mundo' #cadena es de tipo string/texto
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] #una lista con 4 elementos de tipo texto
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} #es un objeto
frutas = ('guayaba', 'fresa', 'papaya') #elementos guardados en un tuple
print(type(frutas)) #imprime de que clase/tipo es
print(ingredientes_pastel[2]) #muestra en consola el producto de ave
ingredientes_pastel.append('Mantequilla') #agrega manteqilla al final de la lista
print(persona['nombre']) #imprime el nombre del objeto 
persona['nombre'] = 'Kevin' #re asigna nombre
persona['color_ojos'] = 'cafe' #agrega una caracteristica nueva
print(frutas[2]) #funcion que imprime papaya al ser la segunda variable almacenada

if numero1 > 45:
    print("Numero mayor")
else:
    print("Numero menor")
    #indica que num1 es mayor a 45

if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")
    #cuenta cuantas letras tiene el texto, al ser mayor de 5 y menor de 15 esuna cadena perfecta

for x in range(8): #funcion
    print(x) #imprime x hasta desde el 0 a 7
for x in range(2,8):
    print(x) #imprime x (2) hasta 7 
for x in range(2,8,2):
    print(x) #imprime x (2) hasta 7 de 2
x = 0 #reset
while(x < 8): #imprime los numeros iterando 8 veces
    print(x)
    x += 1

ingredientes_pastel.pop() #llama a la funcion
ingredientes_pastel.pop(1) #llama al string en posicion 1

print(persona) #imprime al obj
persona.pop('color_ojos') #elimina color_ojos
print(persona) #impr nuevamente persona, sin color_ojos

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break
    #lee la lista desde harina(0), imprimiendo "desp...", si ingrediente es chocolate el bucle se rompe

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')
    #funcion para imprimir hola en un rango de 10 veces

imprime_hola_10_veces() #se llama a la func

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')
    #funcion similar a la anterior sin designar n veces

imprime_hola_n_veces(5) #la llama 5 veces a imprimir

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces() #llama el numero de n veces
imprime_hola_n_o_diez_veces(5) #la llama 5


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)