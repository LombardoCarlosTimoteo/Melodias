while(True):
    print("Que tipo de melodia desea? Alegre o triste?")

    tipo = input("> ")
    tipo.lower

    if(tipo == "alegre"):
        print("alegre")
        break

    if(tipo == "triste"):
        print("triste")
        break

    else:
        print("No entendi lo que desea. Reingrese su peticion")
        