import time

print("Voy a adivinar la letra de tu DNI.") 

respuesta="s"
while respuesta!="n":
    
    print("Introduce el número de tu DNI:") 
    numero = int(input())
    resto = numero % 23
    print("\n")
    if resto == 0:
        print("La letra de tu DNI es: T")
    if resto == 1:
        print("La letra de tu DNI es: R")
    if resto == 2:
        print("La letra de tu DNI es: W")
    if resto == 3:
        print("La letra de tu DNI es: A")    
    if resto == 4:
        print("La letra de tu DNI es: G") 
    if resto == 5:
        print("La letra de tu DNI es: M") 
    if resto == 6:
        print("La letra de tu DNI es: Y") 
    if resto == 7:
        print("La letra de tu DNI es: F") 
    if resto == 8:
        print("La letra de tu DNI es: P") 
    if resto == 9:
        print("La letra de tu DNI es: D") 
    if resto == 10:
        print("La letra de tu DNI es: X") 
    if resto == 11:
        print("La letra de tu DNI es: B")
    if resto == 12:
        print("La letra de tu DNI es: N") 
    if resto == 13:
        print("La letra de tu DNI es: J")  
    if resto == 14:
        print("La letra de tu DNI es: Z") 
    if resto == 15:
        print("La letra de tu DNI es: S") 
    if resto == 16:
        print("La letra de tu DNI es: Q") 
    if resto == 17:
        print("La letra de tu DNI es: V")
    if resto == 18:
        print("La letra de tu DNI es: H") 
    if resto == 19:
        print("La letra de tu DNI es: L")   
    if resto == 20:
        print("La letra de tu DNI es: C") 
    if resto == 21:
        print("La letra de tu DNI es: K") 
    if resto == 22:
        print("La letra de tu DNI es: E") 
    time.sleep(1)
    print("\n")
    print("¿Quieres probar con otro número? (s/n)") 
    respuesta = input()
    if respuesta == ("s"):
        print("\n")
        print("¡Vamos allá!")
        print("\n")
if respuesta == ("n"):
    print("\n")
    print("De acuerdo. ¡Hasta la próxima!")