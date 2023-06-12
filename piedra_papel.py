import random
rng=random.randint(0,2)

if rng == 0:
    mchoice="Piedra"
elif rng == 1:
    mchoice="Papel"
else:
    mchoice="Tijeras"


# Elige usuario
txtchoice='''
Elige una opción:
    Piedra
    Papel
    Tijeras
'''
pchoice=input(txtchoice)

print("Máquina ->", mchoice)
print("Usuario ->", pchoice)

if mchoice==pchoice:
    print("Empate")
else:
    if mchoice=="Piedra" and pchoice=="Papel":
        print("¡Gana Usuario!")
    elif mchoice=="Piedra" and pchoice=="Tijeras":
        print("¡Gana Máquina!")
    elif mchoice=="Papel" and pchoice=="Piedra":
        print("¡Gana Máquina!")
    elif mchoice=="Papel" and pchoice=="Tijeras":
        print("¡Gana Usuario!")
    elif mchoice=="Tijeras" and pchoice=="Piedra":
        print("¡Gana Usuario!")
    elif mchoice=="Tijeras" and pchoice=="Papel":
         print("¡Gana Máquina!")
    else:
         print("ERROR. Argumento inválido")