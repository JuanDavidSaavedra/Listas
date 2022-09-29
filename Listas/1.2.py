from collections import Counter
lista = [8, 6, 8, 10, 8, 20, 10, 8, 8, 9, 4, 7, 6, 5, 6, 2, 3] 
conteo = Counter(lista)

resultado = {}
for clave in conteo:  
    valor = conteo[clave]
    if valor != 0:
        resultado[clave] = valor
print(resultado)