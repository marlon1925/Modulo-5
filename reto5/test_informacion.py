import informacion

print("============== PANCIENTES ==============")

numero = int(input("Ingrese el número de pacientes: "))

for i in range(numero):
    count=+i+1
    print(" ")
    print(f"Paciente {count}")
    nombre_paciente= input("Ingrese el nombre y apellido: ")
    informacion.agregar_nombre(nombre_paciente)
    edad= int(input("Ingrese el año de nacimiento: "))
    informacion.agregar_edad(edad)

print("============== DATOS DE LOS PACIENTE ==============")
print("NOMBRES: ")
print(informacion.nombre_paciente)
print(" ")
print("EDAD: ")
print(informacion.edad)
print("===================================================")

mayor=max(informacion.edad)
menor=min(informacion.edad)
nombre_mayor=informacion.nombre_paciente[informacion.edad.index(mayor)]
nombre_menor=informacion.nombre_paciente[informacion.edad.index(menor)]


print("============== MAYOR Y MENOR EDAD ==============")
print(f"PACIENTE {nombre_mayor} {mayor}")
print(f"PACIENTE {nombre_menor} {edad}")
