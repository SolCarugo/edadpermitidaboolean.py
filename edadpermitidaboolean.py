edad = int(input("¿Cual es tu edad? : "))


if edad >= 18:
    status = True
else:
    status = False

if status == True:
    print("Vos sos mayor de edad.")
else:
    print("Vos sos menor de edad")
