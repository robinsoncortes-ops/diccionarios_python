

agenda = {}

# Agregar contactos
for i in range(3):
    nombre =input("nombre: ").upper()
    telefono = input("telefono: ")
    agenda[nombre] = telefono

# consultar
bucar = input("buscar nombre: ").upper()
print(agenda.get(bucar,"no existe"))


# eliminar
eliminar = input("eliminar nombre: ").upper()
agenda.pop(eliminar,None)

# mostrar agenda final 
print(agenda)