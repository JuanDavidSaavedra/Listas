from collections import Counter
vocales = ['a', 'e', 'i', 'o', 'u']
vocales.append('e')  # Añade un elemento
vocales.extend(['i', 'o', 'u'])  # Añade un grupo de elementos
conteo = Counter(vocales)
resultado = {}
for clave in conteo:  
    valor = conteo[clave]
    if valor != 0:
        resultado[clave] = valor
print(resultado)
vocales.pop()
print(vocales)