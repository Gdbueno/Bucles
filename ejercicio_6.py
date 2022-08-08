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
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior
max = None
lista = []

cantidad_numeros_positivos = 0  # Inicializo el contador en 0
cant_num_neg = 0
while True:
    inicio = int(input('Ingrese el primer número de la secuencia\n'))
    lista.append (inicio)
    fin = int(input('Ingrese el último número de la secuencia\n'))
    lista.append (fin)
    break
# for ... in range(....)
for lista in range (inicio, fin+1):
    if lista >= 0:
        cantidad_numeros_positivos +=1
    else:
        cant_num_neg +=1
# Imprimir el valor de la cantidad de números positivos y negativos
print ('Numeros Positivos:', cantidad_numeros_positivos)
print ('Numeros negativos:', cant_num_neg)
print ("terminamos!")
# Fin del ejercicio
