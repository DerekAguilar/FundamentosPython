students = []

def show_students():
    for student in students:
        print("Alumno->",student)

def add_student(student):
    students.append(student)

def remove_student(student):
    try:
        students.remove(student)
    except Exception:
        print("No existe")

choiceTxt='''
Elija una opción:
    1 - Insertar
    2 - Mostrar
    3 - Eliminar
    4 - Salir
'''
while True:
    choice=int(input(choiceTxt))
    if choice==1:
        student=input("Ingresa student: ")
        add_student(student)
    elif choice==2:
        show_students()
    elif choice==3:
        student=input("Ingresa student a eliminar: ")
        remove_student(student)
    elif choice==4:
        break
    else:
        print('ERROR: Argumento inválido')
