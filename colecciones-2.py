# Tuplas (Listas inmodificables)
myTuple=('Hola',12,1.53,True)
print(type(myTuple))
print(myTuple[0])
print(myTuple[-1])
# Error
# myTuple[0]="otro valor"

# Conjuntos (set) ; Listas en [], tuplas en (), conjuntos en {}. Los conjuntos no muestran valores duplicados
mySet={1,2,4,4,4,4,True,'hi'}
print(type(mySet))
print(mySet)

lista=[1,2,3,1,2,4,3,5,6]
print(lista)
print(set(lista)) # Convierte para esta operación la lista en un conjunto