import random

def lletgir_llista_enters():
    l = []
    a = ""
    while a != ".":
        a = input("Dime un numero, '.' para acabar. ")
        if a != ".":
            l.append(int(a))
    return l

def senars_llista(llista):
    r = []
    for e in llista:
        if e % 2 == 1:
            r.append(e)
    return r

def sumar_parells_llista(llista):
    b = 0
    for e in llista:
        if e % 2 == 0:
            b += e
    
    print("La suma de los pares de la lista es: {}".format(b))

def cercar_numero_llista(llista, numero):
    for i, e in enumerate(llista):  
        if e == numero:
            print("El numero {} está en la posición {}. ".format(numero, i+1))
            return i+1
    return -1 

def llegir_llista_paraules():
    l = []
    a = ""
    while a != ".":
        a = input("Dime una palabra, '.' para acabar. ")
        if a != ".":
            l.append(a)
    return l

def crear_paraula_llista(llista):
    r = []
    for e in llista:
        if e[0].lower() == "a":
            r.append("Avión")
        elif e[0].lower() == "b":
            r.append("Burro")
        elif e[0].lower() == "c":
            r.append("Casa")
        elif e[0].lower() == "d":
            r.append("Dedo")
        elif e[0].lower() == "e":
            r.append("Elefante")
        elif e[0].lower() == "f":
            r.append("Fealdad")
        elif e[0].lower() == "g":
            r.append("Gula")
        elif e[0].lower() == "h":
            r.append("Hierro")
        elif e[0].lower() == "i":
            r.append("IVA")
        elif e[0].lower() == "j":
            r.append("Jolines")
        elif e[0].lower() == "k":
            r.append("Kilo")
        elif e[0].lower() == "l":
            r.append("Luz")
        elif e[0].lower() == "m":
            r.append("Maria")
        elif e[0].lower() == "n":
            r.append("Nicolás")
        elif e[0].lower() == "o":
            r.append("Oso")
        elif e[0].lower() == "p":
            r.append("Perro")
        elif e[0].lower() == "q":
            r.append("Queso")
        elif e[0].lower() == "r":
            r.append("Raúl")
        elif e[0].lower() == "s":
            r.append("Solo")
        elif e[0].lower() == "t":
            r.append("Toni")
        elif e[0].lower() == "u":
            r.append("Uva")
        elif e[0].lower() == "v":
            r.append("Volar")
        elif e[0].lower() == "w":
            r.append("Wadie")
        elif e[0].lower() == "x":
            r.append("Xerneas")
        elif e[0].lower() == "y":
            r.append("Yo-yo")
        elif e[0].lower() == "z":
            r.append("Zorro")
        
    print(r)

def crear_llista_nums_aleatoris():
    r = []
    b = 0
    while b <= 4:
        a = random.randint(1,100)
        r.append(a)
        b += 1
    return r

def comparar_llistes(llista1, llista2):
    r = []
    for i in range(5):
            if llista2[i] not in llista1:
                r.append(0)  
            elif llista2[i] == llista1[i]:
                r.append(2) 
            else:
                r.append(1)  
    return r

def majors_edat(edat1, edat2):
    if int(edat1) >= 18 and int(edat2) >= 18:
        print("Las 2 edades son mayores a 18")
    elif int(edat1) >= 18 and int(edat2) < 18:
        print("La edad 1 ({}) es mayor o igual a 18 y la edad 2 ({}) es menor".format(edat1, edat2))
    elif int(edat2) >= 18 and int(edat1) < 18:
        print("La edad 2 ({}) es mayor o igual a 18 y la edad 1 ({}) es menor".format(edat2, edat1))
    else:
        print("Ninguna de las 2 edades es mayor a 18")

def menu():
    a = 0
    while a < 1 or a >10:
        print(""" Este es el menu de opciones:
                1- Leer lista de enteros
                2- Separar los impares de una lista
                3- Sumar los numeros pares de una lista
                4- Buscar un numero en una lista
                5- Leer lista de palabras
                6- Crear palabras a partir de una lista
                7- Crear lista de numeros aleatorios
                8- Comparar 2 listas
                9- Ver si una edad es mayor de edad 
                10- Salir
        """)
        a = int(input("Dime que quieres hacer (Numero): "))
    return a

#Programa principal

b = True
while b == True:
    x = menu()
    match x:
        case 1:
            print(lletgir_llista_enters())
        case 2:
            llista=lletgir_llista_enters()
            print(senars_llista(llista))
        case 3:
            llista=lletgir_llista_enters()
            sumar_parells_llista(llista)
        case 4:
            llista=lletgir_llista_enters()
            numero = int(input("¿Que numero quieres buscar? "))
            cercar_numero_llista(llista, numero)
        case 5:
            print(llegir_llista_paraules())
        case 6:
            llista = llegir_llista_paraules()
            crear_paraula_llista(llista)
        case 7:
            print(crear_llista_nums_aleatoris())
        case 8:
            llista1 = crear_llista_nums_aleatoris()
            print("Recuerda, solo 5 numeros.")
            llista2 = lletgir_llista_enters()
            print(comparar_llistes(llista1, llista2))
        case 9:
            edat1 = input("Dime la edad numero 1 ")
            edat2 = input("Dime la edad numero 2 ")
            majors_edat(edat1, edat2)
        case 10:
            print("Adioooos")
            b = False

