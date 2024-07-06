#ej 5

def cumple_condicion(numero):
    #define la función
    
    """
    Verifica si un número entero de cuatro cifras cumple la condición de que la
    suma de las unidades y las centenas es igual a la suma de las decenas y las
    unidades de mil.

    Parámetro:
        numero: int - El número entero de cuatro cifras a verificar.

    Retorna:
        bool: True si el número cumple la condición, False en caso contrario.
    """
    # Extraer las unidades, decenas, centenas y unidades de mil del número
    u = numero % 10
    d = (numero // 10) % 10
    c = (numero // 100) % 10
    m = (numero // 1000) % 10
    
    # Calcular la suma de las unidades y las centenas
    suma_unidades_centenas = u + c
    
    # Calcular la suma de las decenas y las unidades de mil
    suma_decenas_miles = d + m
    
    # Comparar ambas sumas
    return suma_unidades_centenas == suma_decenas_miles

# Lista para almacenar los números de cuatro cifras que cumplen la condición
numeros_cumplen_condicion = []

# Iterar a través de todos los números de cuatro cifras (de 1000 a 9999)
for numero in range(1000, 10000):
    # Verificar si el número cumple la condición
    if cumple_condicion(numero):
        # Añadir el número a la lista si cumple la condición
        numeros_cumplen_condicion.append(numero)

# Imprimir todos los números que cumplen la condición
print("Números de cuatro cifras que cumplen la condición de que la suma de las unidades y las centenas es igual a la suma de las decenas y las unidades de mil:")
for numero in numeros_cumplen_condicion:
    print(numero)