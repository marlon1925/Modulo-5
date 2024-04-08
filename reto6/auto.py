
class Auto:
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

    @classmethod
    def toyota_autos(cls):
        marca = "Toyota"
        modelo = "Yaris"
        anio = 2024
        return cls(marca,modelo,anio)
    
    @classmethod
    def kia_autos(cls):
        marca = "Kia"
        modelo = "Cerato"
        anio = 2024
        return cls(marca,modelo,anio)
    
    @staticmethod
    def comparar_autos(kilometraje,kilometraje2):
        if kilometraje == kilometraje2:
            return "Tienen el mismo kilometraje"
        return "No tienen el mismo kilometraje"
    
    @staticmethod
    def anio_autos(anio,anio2):
        if anio == anio2:
            return "Tienen el mismo anio"
        return "No tienen el mismo anio"
