class Empresa:
    lista1 = []
    lista2 = []
    n = int(input("\nDigite el número de conductores: "))

    for i in range(n):
        nombre = input("\nEscriba el nombre del conductor: ")
        viaje1 = int(input("Digite el kilometraje del primer viaje del conductor: "))
        viaje2 = int(input("Digite el kilometraje del segundo viaje del conductor: "))
        viaje3 = int(input("Digite el kilometraje del tercer viaje del conductor: "))
        promedio = (viaje1 + viaje2 + viaje3)/3
        lista1.append(nombre)
        lista2.append(promedio)

    print("\n", lista1, "\n")
    print("\n", lista2, "\n")
    print("El mayor es:", lista1[lista2.index(max(lista2))], "\n")





