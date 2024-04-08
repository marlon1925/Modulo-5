from auto import Auto

primerCarro = Auto.toyota_autos()

# print("METODO MOSTRA INFORMACION ")
# print(primerCarro.mostrar_informacion())
# print("")
# print("METODO ACTUALIZAR KILOMETRAJE ")
# kilometraje = float(input("Ingrese el kilometraje actual del vehiculo: "))
# primerCarro.actualizar_kilometraje(kilometraje)
# print("")
# print("METODO REALIZAR VIAJE ")
# kilometrajeViaje = float(input("Ingrese el kilometraje del viaje: "))
# primerCarro.realizar_viaje(kilometrajeViaje)
# print("")
# print("METODO ESTADO DEL AUTO ")
# print(primerCarro.estado_auto())


segundoCarro = Auto.kia_autos()

segundoCarro.actualizar_kilometraje(25000)

print(primerCarro.__dict__)
print(segundoCarro.__dict__)

print("PRIMER METODO STATIC:")
print(Auto.comparar_autos(primerCarro.kilometraje, segundoCarro.kilometraje))

print("SEGUNDO METODO STATIC:")
print(Auto.comparar_autos(primerCarro.anio, segundoCarro.anio))

