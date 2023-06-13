# Listas (como los arrays en otros lenguajes)
# Entre corchetes []
myList=[123,True,3.1415926,"Hi!"]
print(type(myList))
print(myList)

# Indexing
print(myList[0])
# Slicing
print(myList[2:])

students = ["Guadalupe","Alicia","Alin"]
print(students)
students.append("Paco")
students.append("Nacho")
students.append("Gaby")
print(students)
students.remove("Guadalupe")
print(students)
students[1]="Vero"
print(students)