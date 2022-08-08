# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores
colores = ['rojo', 'naranja', 'verde', 'azul']
# Itere el "for" utilizando la lista como parámero
# y utilizar como elemento del "for" cada color
# for color ...

# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...
colores_len = len(colores)
for i in range (colores_len):
    if (i % 2) == 0:
        color = colores [i]
        print (color)
    else:
        color = colores [i]
        print (color)
for i in range (colores_len):
    print ('Primer palabra:', colores [0])
    print ('Segunda palabra:', colores [1])
    print ('Tercera palabra:', colores [2])
    print ('Cuarta palabra:', colores [3])
print("terminamos!")
# Fin del ejercicio