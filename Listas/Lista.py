#Problema 2
# A partir de una frase si el numero de sus palabras (letras) es superior a 9, convertir a X
# las letras ubicadas en las posiciones pares y volver a mostrar la nueva frase


palabra = input("Ingrese una frase: ")
nuevaFrase = []
miPalabra = ""

if(len(palabra)<=9):
    miPalabra = palabra
else:
    for i in range(len(palabra)):
        if((i)%2==0):
            nuevaFrase.append("x")
        else:   
            nuevaFrase.append(palabra[i])
    for i in range(len(nuevaFrase)):
        miPalabra += nuevaFrase[i]


print( palabra)
print( miPalabra)