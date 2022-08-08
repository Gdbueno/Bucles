# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

lista = []

while True: 
    inicio = int(input('Ingrese el primer número de la secuencia\n'))
    lista.append (inicio)
    fin = int(input('Ingrese el último número de la secuencia\n'))
    if fin > inicio:
        lista.append (fin)
        break
    else:
        print ('ingrese un numero mayor al ingresado')
        fin = int(input('Ingrese el último número de la secuencia\n'))
        break
sumatoria = 0  # Inicializo el contador en 0
for (inicio) in range (fin+1):
    for suma in lista:
        sumatoria += suma
        print ('el valor final es:', sumatoria)

# for ... in range(....)

# Imprimir el valor de la sumatoria


print("terminamos!")
# Fin del ejercicio