
# Diccionarios
# {"clave":"valor"}

teacher={
    "name":"Francisco",
    "lName":"López",
    "phone":"2471234567",
    "groups":["3ADSM","3BDSM"]
}

print(type(teacher))
print(teacher)
print(teacher["name"])
print(teacher["groups"])
teacher["groups"].append("3CDSM")
teacher["phone"]="2471070644"
teacher["city"]="Huamantla"
print(teacher)