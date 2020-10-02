import random
todas_notas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
nota = 0
cant_elegidas = 0
seleccionadas = 0
nota_central = " "
nota2elegida = " "
nota3elegida = " "
nota4elegida = " "

nota1subida = " "
nota1subidamas = " "
nota2subida = " "
nota2subidamas = " "
nota3subida = " "
nota3subidamas = " "
nota4subida = " "
nota4subidamas = " "


def NotasRandom():
    ###TOMA 3 NOTAS ALEATORIAS###
    nota = " "
    seleccionadas = ""
    nota = random.choice(todas_notas)
    seleccionadas += nota
    seleccionadas += " ,"
    nota = random.choice(todas_notas)
    seleccionadas += nota
    seleccionadas += " ,"
    nota = random.choice(todas_notas)
    seleccionadas += nota
    print(f"Las notas seleccionadas son: {nota_central}, {seleccionadas}")


def AcordesAlegre1():
    ###Realiza el primer acorde segun la nota central###
    nota1subida = ""
    nota1subidamas = ""
    if nota_central == "a":
        nota1subida += "c#"
        nota1subidamas += "e"
    if nota_central == "b":
        nota1subida += "d#"
        nota1subidamas += "f#"
    if nota_central == "c":
        nota1subida += "e"
        nota1subidamas += "g"
    if nota_central == "d":
        nota1subida += "f#"
        nota1subidamas += "a"
    if nota_central == "e":
        nota1subida += "g#"
        nota1subidamas += "b"
    if nota_central == "f":
        nota1subida += "a"
        nota1subidamas += "c"
    if nota_central == "g":
        nota1subida += "b"
        nota1subidamas += "d"

    print(
        f"En la primer semicorchea va este acorde: {nota_central}, {nota1subida}, {nota1subidamas} ")


def AcordesAlegre2():
    ###Realiza el primer acorde segun la nota central###
    nota2subida = ""
    nota2subidamas = ""
    if nota2elegida == "a":
        nota2subida += "c#"
        nota2subidamas += "e"
    if nota2elegida == "b":
        nota2subida += "d#"
        nota2subidamas += "f#"
    if nota2elegida == "c":
        nota2subida += "e"
        nota2subidamas += "g"
    if nota2elegida == "d":
        nota2subida += "f#"
        nota2subidamas += "a"
    if nota2elegida == "e":
        nota2subida += "g#"
        nota2subidamas += "b"
    if nota2elegida == "f":
        nota2subida += "a"
        nota2subidamas += "c"
    if nota2elegida == "g":
        nota2subida += "b"
        nota2subidamas += "d"

    print(
        f"En la segunda semicorchea va este acorde: {nota2elegida}, {nota2subida}, {nota2subidamas} ")


def AcordesAlegre3():
    ###Realiza el primer acorde segun la nota central###
    nota3subida = ""
    nota3subidamas = ""
    if nota3elegida == "a":
        nota3subida += "c#"
        nota3subidamas += "e"
    if nota3elegida == "b":
        nota3subida += "d#"
        nota3subidamas += "f#"
    if nota3elegida == "c":
        nota3subida += "e"
        nota3subidamas += "g"
    if nota3elegida == "d":
        nota3subida += "f#"
        nota3subidamas += "a"
    if nota3elegida == "e":
        nota3subida += "g#"
        nota3subidamas += "b"
    if nota3elegida == "f":
        nota3subida += "a"
        nota3subidamas += "c"
    if nota3elegida == "g":
        nota3subida += "b"
        nota3subidamas += "d"

    print(
        f"En la tercer semicorchea va este acorde: {nota3elegida}, {nota3subida}, {nota3subidamas} ")


def AcordesAlegre4():
    ###Realiza el primer acorde segun la nota central###
    nota4subida = ""
    nota4subidamas = ""
    if nota4elegida == "a":
        nota4subida += "c#"
        nota4subidamas += "e"
    if nota4elegida == "b":
        nota4subida += "d#"
        nota4subidamas += "f#"
    if nota4elegida == "c":
        nota4subida += "e"
        nota4subidamas += "g"
    if nota4elegida == "d":
        nota4subida += "f#"
        nota4subidamas += "a"
    if nota4elegida == "e":
        nota4subida += "g#"
        nota4subidamas += "b"
    if nota4elegida == "f":
        nota4subida += "a"
        nota4subidamas += "c"
    if nota4elegida == "g":
        nota4subida += "b"
        nota4subidamas += "d"

    print(
        f"En la cuarta y ultima semicorchea va este acorde: {nota4elegida}, {nota4subida}, {nota4subidamas} ")


def Acordetriste1():
    ###Realiza el primer acorde segun la nota central###
    nota1subida = ""
    nota1subidamas = ""
    if nota_central == "a":
        nota1subida += "c"
        nota1subidamas += "e"
    if nota_central == "b":
        nota1subida += "d"
        nota1subidamas += "f#"
    if nota_central == "c":
        nota1subida += "d#"
        nota1subidamas += "g"
    if nota_central == "d":
        nota1subida += "f"
        nota1subidamas += "a"
    if nota_central == "e":
        nota1subida += "g"
        nota1subidamas += "b"
    if nota_central == "f":
        nota1subida += "g#"
        nota1subidamas += "c"
    if nota_central == "g":
        nota1subida += "a#"
        nota1subidamas += "d"

    print(
        f"En la primer semicorchea va este acorde: {nota_central}, {nota1subida}, {nota1subidamas} ")


def Acordetriste2():
    ###Realiza el primer acorde segun la nota central###
    nota2subida = ""
    nota2subidamas = ""
    if nota2elegida == "a":
        nota2subida += "c"
        nota2subidamas += "e"
    if nota2elegida == "b":
        nota2subida += "d"
        nota2subidamas += "f#"
    if nota2elegida == "c":
        nota2subida += "d#"
        nota2subidamas += "g"
    if nota2elegida == "d":
        nota2subida += "f"
        nota2subidamas += "a"
    if nota2elegida == "e":
        nota2subida += "g"
        nota2subidamas += "b"
    if nota2elegida == "f":
        nota2subida += "g#"
        nota2subidamas += "c"
    if nota2elegida == "g":
        nota2subida += "a#"
        nota2subidamas += "d"

    print(
        f"En la segunda semicorchea va este acorde: {nota2elegida}, {nota2subida}, {nota2subidamas} ")


def Acordetriste3():
    ###Realiza el primer acorde segun la nota central###
    nota3subida = ""
    nota3subidamas = ""
    if nota3elegida == "a":
        nota3subida += "c"
        nota3subidamas += "e"
    if nota3elegida == "b":
        nota3subida += "d"
        nota3subidamas += "f#"
    if nota3elegida == "c":
        nota3subida += "d#"
        nota3subidamas += "g"
    if nota3elegida == "d":
        nota3subida += "f"
        nota3subidamas += "a"
    if nota3elegida == "e":
        nota3subida += "g"
        nota3subidamas += "b"
    if nota3elegida == "f":
        nota3subida += "g#"
        nota3subidamas += "c"
    if nota3elegida == "g":
        nota3subida += "a#"
        nota3subidamas += "d"

    print(
        f"En la tercera semicorchea va este acorde: {nota3elegida}, {nota3subida}, {nota3subidamas} ")


def Acordetriste4():
    ###Realiza el primer acorde segun la nota central###
    nota4subida = ""
    nota4subidamas = ""
    if nota4elegida == "a":
        nota4subida += "c"
        nota4subidamas += "e"
    if nota4elegida == "b":
        nota4subida += "d"
        nota4subidamas += "f#"
    if nota4elegida == "c":
        nota4subida += "d#"
        nota4subidamas += "g"
    if nota4elegida == "d":
        nota4subida += "f"
        nota4subidamas += "a"
    if nota4elegida == "e":
        nota4subida += "g"
        nota4subidamas += "b"
    if nota4elegida == "f":
        nota4subida += "g#"
        nota4subidamas += "c"
    if nota4elegida == "g":
        nota4subida += "a#"
        nota4subidamas += "d"

    print(
        f"En la la cuarta y ultima semicorchea va este acorde: {nota4elegida}, {nota4subida}, {nota4subidamas} ")


###PRINCIPAL####
while(True):
    print("Que tipo de acorde desea, alegre o triste?")
    tipo = input("> ")
    tipo.lower

    if(tipo == "alegre"):
        nota_central = input("Elija su nota central> ")
        nota_central.lower
        compases = int(input("Cuantos compases aleatorios desea? > "))
        for x in range(compases):
            NotasRandom()
        nota_central = input(
            "Ingrese la primer nota del compas que le gusta: ")
        AcordesAlegre1()
        nota2elegida = input(
            "Ingrese la segunda nota del compas que le gusta: ")
        AcordesAlegre2()
        nota3elegida = input(
            "Ingrese la tercera nota del compas que le gusta: ")
        AcordesAlegre3()
        nota4elegida = input(
            "Ingrese la cuarta y ultima nota del compas que le gusta: ")
        AcordesAlegre4()
        break

    if(tipo == "triste"):
        nota_central = input("Elija su nota central> ")
        nota_central.lower
        compases = int(input("Cuantos compases aleatorios desea? > "))
        for x in range(compases):
            NotasRandom()
        nota_central = input(
            "Ingrese la primer nota del compas que le gusta: ")
        Acordetriste1()
        nota2elegida = input(
            "Ingrese la segunda nota del compas que le gusta: ")
        Acordetriste2()
        nota3elegida = input(
            "Ingrese la tercera nota del compas que le gusta: ")
        Acordetriste3()
        nota4elegida = input(
            "Ingrese la cuarta y ultima nota del compas que le gusta: ")
        Acordetriste4()
        break

    else:
        salida = input(
            "Presione 's'  si desea salir o cualquier tecla para continuar: ")
        if (salida == 's'):
            break
        else:
            pass

print("Muchas gracias por usarme, hasta luego.")
