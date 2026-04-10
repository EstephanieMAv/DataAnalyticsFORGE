#Bucle For Basico
'''

Básico: imprime todos los números enteros del 0 al 100. CHECK

Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500. CHECK

Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”. CHECK

Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante). CHECK

Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3. CHECK

Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas). CHECK

#basic
for n in range(101):
    print(n)

#multiplos de 2
n = 0
while n <= 100 :
    n += n
    for n in range(2, 501, 2):
        print(n, "es multiplo")
    
#vainilla ice
for n in range(1, 101):
    if n%10 == 0:
        print("baby")
    elif n%5 == 0:
            print("ice ice")
    else:
        print(n)

#numero gigante a la vista
suma = 0
for n in range(1,500001, 2):
    suma+= n
print(f"La suma total es: {suma}.")

#regresame al 3 D:
for n in range(2024, 0, -3):
    print(n)
'''
#contador dinamico
num_inicial = int(input("Ingrese el numero inicial"))
num_final = int(input("Ingrese el numero final del recorrido"))
multiplo = int(input("¿De que multiplo?"))
for n in range(num_inicial, num_final, multiplo):
    if n%multiplo == 0:
       print(n)
    n += n

#probarlo de manera individual a cada ejercicio c: