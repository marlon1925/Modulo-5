import random
from laptop import Laptop

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria,disco,conectividad,costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.disco=disco
        self.conectividad=conectividad

    def __str__(self):
        return f"Laptop Business: \n Marca={self.marca}\n Procesador={self.procesador}\n Memoria={self.memoria}\n Disco={self.disco}\n Conectividad={self.conectividad}\n Costo={self.costo}\n Impuesto={self.impuesto}\n"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico=super().realizar_diagnostico_sistema()
        resultado_oficina =self.realizar_diagnostico_oficina()
        resultado_diagnostico["Resultado oficina"]=resultado_oficina
        return resultado_diagnostico
    
    def realizar_diagnostico_oficina(self):
        resultado_diagnostico= super().realizar_diagnostico_sistema()
        resultado_conectividad=self.verificar_conectividad_red()
        resultado_diagnostico["Resultado conectividad"]=resultado_conectividad
        return resultado_diagnostico
    
    def verificar_conectividad_red(self):
        resultados_conectividad = {}
        resultados_conectividad["Disponibilidad de Wi-Fi"] = random.choice([True, False])
        resultados_conectividad["Acceso a servidores empresariales"] = random.choice([True, False])
        resultados_conectividad["Latencia de red"] = random.randint(1, 100)
        return resultados_conectividad


    pass