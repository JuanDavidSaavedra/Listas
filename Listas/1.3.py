from collections import Counter
lista = []
vocales = "esta es mi frase para este ejercicicio el dia de hoy"
x = vocales.split()
lista.append(vocales)
def respuesta():
    for list in x:
        # este es par
        if list % 2 == 0:
            lista.append(1)
        else: 
            lista.append(0)
    return lista
def agregarX():
    if x.__len__ >=9:
        
print(x)
print(lista)