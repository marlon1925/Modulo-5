from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_Business import Laptop_Business

def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave}: {valor}")
    print("\n")
    

laptop_andres = Laptop("Lenovo", "i7", 32, 600)
laptop_marlon = Laptop_Gaming("MSI", "i7", 16, "RTX 8GB")
laptop_empresarial= Laptop_Business("ASUS", "I7", 4, 8, 10)

print("ANDRES:")
imprimir_informe(laptop_andres)
print("MARLON:")
imprimir_informe(laptop_marlon)

print("")
print("LAPTOP EMPRESARIAL: ")
print(laptop_empresarial.realizar_diagnostico_sistema())
