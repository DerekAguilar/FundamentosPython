# Funciones
# def name_function(params):
#    code

# Sin parámetros ni retorno
def saluda():
    print("Hola a Todos")

saluda()

# Con parámetros sin retorno
def duplica(num):
    print(num*2)

duplica(5)

def suma(num1,num2):
    print(f"La suma de los números es: {num1+num2}")

suma(23,45)
# Parámetros opcionales sin retorno
def getLista(al1="José",al2="Darlene"):
    return [al1,al2]

myList=getLista()
print(myList)
myList=getLista("Peter")
print(myList)
myList=getLista("Peter Parker","Tony Stark")
print(myList)
myList=getLista(al2="Peter Parker",al1="Tony Stark")
print(myList)