'''
Instrucciones Detalladas

Carga de Datos:
Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
«producto»: una cadena de texto que represente el nombre del producto vendido.
«cantidad»: un número entero que represente la cantidad de productos vendidos.
«precio»: un número flotante que represente el precio unitario del producto.

Cálculo de Ingresos Totales:
Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.

Análisis del Producto Más Vendido:
Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.

Promedio de Precio por Producto:
Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.

Ventas por Día:
Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.

Representación de Datos:
Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
«cantidad_total»: la cantidad total vendida del producto.
«ingresos_totales»: los ingresos totales generados por la venta del producto.
«precio_promedio»: el precio promedio de venta del producto.
 

Entrega: Presenta tus resultados en un archivo de texto o una hoja de cálculo. Detalla cada paso del análisis y los resultados obtenidos. Asegúrate de incluir:

La lista de ventas original.
Los ingresos totales generados.
El producto más vendido y su cantidad total vendida.
El precio promedio de venta por producto.
Los ingresos totales por día.
El resumen de ventas por producto.
''' 
#ventas del año, hasta el momento
lista_ventas = [
    {'fecha' : "2026-01-13", 'producto' : "Magdalenas", 'cantidad' : 6, 'precio' : 7500.50},
    {'fecha' : "2026-04-04", 'producto' : "Harina de avena", 'cantidad' : 25, 'precio' : 47590.89},
    {'fecha' : "2026-02-29", 'producto' : "Galletitas integrales", 'cantidad' : 1, 'precio' : 7700.50},
    {'fecha' : "2026-03-23", 'producto' : "Semillas de chia", 'cantidad' : 1, 'precio' : 5500.10},
    {'fecha' : "2026-04-15", 'producto' : "Porotos", 'cantidad' : 4, 'precio' : 5000.00},
    {'fecha' : "2026-02-13", 'producto' : "Almedras", 'cantidad' : 10, 'precio' : 17100.79},
    {'fecha' : "2026-02-11", 'producto' : "Galletitas SIN TACC", 'cantidad' : 3, 'precio' : 14999.05},
    {'fecha' : "2026-03-08", 'producto' : "Semillas de girasol", 'cantidad' : 5, 'precio' : 8420.64},
    {'fecha' : "2026-04-13", 'producto' : "Semillas de calabaza", 'cantidad' : 8, 'precio' : 9400.79},
    {'fecha' : "2026-01-17", 'producto' : "Palo azul", 'cantidad' : 1, 'precio' : 5100.51},
    {'fecha' : "2026-04-13", 'producto' : "Barrita de cereal", 'cantidad' : 12, 'precio' : 13000.00},
    {'fecha' : "2026-02-02", 'producto' : "Curcuma concentrada", 'cantidad' : 3, 'precio' : 66900.00},
    {'fecha' : "2026-01-03", 'producto' : "Frasco de magnesio", 'cantidad' : 1, 'precio' : 21569.01},
    {'fecha' : "2026-04-10", 'producto' : "Alfajor Chocolate Dubai", 'cantidad' : 30, 'precio' : 60000.00},
    {'fecha' : "2026-01-23", 'producto' : "Propoleo", 'cantidad' : 2, 'precio' : 30600.43},
    {'fecha' : "2026-03-31", 'producto' : "Omega 3 Vegetal", 'cantidad' : 5, 'precio' : 271535.99},
]

def analisis_ventas(ventas):
    suma_total = 0.0
    ventas_por_producto = {}
    precios_por_producto = {}
    ventas_por_dia = {}
    for venta in ventas:
        fecha = venta['fecha']
        producto = venta['producto']
        cantidad = venta['cantidad']
        precio = venta['precio']
        
        #El primero para la totalidad de cada uno en un mismo dia y la suma total para el ingreso total de ventas
        total = cantidad * precio
        suma_total += total 
        
        #Ventas por producto
        ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad #Busca el produco y la cantidad
        
        suma_promedio, total_unidades = precios_por_producto.get(producto, (0.0, 0)) #Recupero producto, cantidad y
        precios_por_producto[producto] = (suma_promedio + precio, total_unidades + cantidad) #Actualizamos el diccionario
        
        ventas_por_dia[fecha] = ventas_por_dia.get(fecha, 0.0) + total #Recupero las fechas
        
        resumen_de_ventas = {} #Pa rellenar
        producto_mas_comprado = None
        cantidad_maxima = 0
        
        #Precio promedio y si el hay mas de un producto
        for producto, (suma_promedio, total_unidades) in precios_por_producto.items():
            promedio = suma_promedio / total_unidades #promedio
            print(f"El precio promedio de {producto} es: {promedio}")
        
        resumen_de_ventas[producto] = {
            'cantidad_total' : total_unidades,
            'ingreso_total' : total_unidades * promedio,
            'precio_promedio' : promedio
        }
        #Mas vendido
        if total_unidades > cantidad_maxima:
            cantidad_maxima = total_unidades
            producto_mas_comprado = producto
    #Retorno del resumen
    return{
        'ingreso_total' : suma_total,
        'producto_mas_vendido' : producto_mas_comprado,
        'ventas_por_dia' : ventas_por_dia,
        'resumen' : resumen_de_ventas
    }

resultado = analisis_ventas(lista_ventas)
print(resultado) #Como me costo, no me andaba la llamada y toco imprimir