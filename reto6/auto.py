
class auto:
    def __init__(self, marca, modelo, anio, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print("======== INFORMACION VEHICULO ========")
        print(f"Marca {self.marca}")
        print(f"Modelo {self.modelo}")
        print(f"Año {self.anio}")
    
    def actualizar_kilometraje(self,newKilometraje):
        if newKilometraje < self.kilometraje:
            print("No se puede reducir el kilometraje")
        else:
            self.kilometraje=newKilometraje
    
    def realizar_viaje(self,kilometros):
        if kilometros < 0:
            print("No ingrese kilometros negativos")
        else:
            self.kilometraje+= kilometros

    def estado_auto (self):
        print("======== INFORMACION VEHICULO ========")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Kilometraje: {self.kilometraje}")
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif self.kilometraje < 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

primerCarro = auto("Toyota", "Supra", "1998")

print("METODO MOSTRA INFORMACION ")
print(primerCarro.mostrar_informacion())
print("")
print("METODO ACTUALIZAR KILOMETRAJE ")
kilometraje = float(input("Ingrese el kilometraje actual del vehiculo: "))
primerCarro.actualizar_kilometraje(kilometraje)
print("")
print("METODO REALIZAR VIAJE ")
kilometrajeViaje = float(input("Ingrese el kilometraje del viaje: "))
primerCarro.realizar_viaje(kilometrajeViaje)
print("")
print("METODO ESTADO DEL AUTO ")
print(primerCarro.estado_auto())

