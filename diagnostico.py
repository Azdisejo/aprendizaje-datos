# %%
ventas = [120, -5, 340, 0, 89, -12, 410]
ventas_sin_iva = []

# %%
for x in ventas:
    if x>0:
        ventas_sin_iva.append(round(x*1.19, 2))
# %%
print(ventas_sin_iva)
print(len(ventas_sin_iva))
# %%
ventas_con_iva = [round(x*1.19, 2) for x in ventas if x > 0]
# %%
print(ventas_con_iva)
# %%
stock = {"Estufa A": 15, "Estufa B": 0, "Estufa C": 42, "Estufa D": 0, "Estufa E": 7}
con_stock={}
for nombre, cantidad in stock.items():
    if cantidad > 0:
        con_stock[nombre] = cantidad
print(con_stock)
# %%
con_stock = {nombre: cantidad for nombre, cantidad in stock.items() if cantidad > 0}
# %%
print(con_stock)

# %%
def precio_final(precio, descuento=0):
    resultado = (precio * (1 - descuento/100)) * 1.19
    return resultado

print(precio_final(100000))
print(precio_final(100000, 10))
print(precio_final(250000, 25))
# %%
def precio_promedio(total_ventas, unidades):
    try:
        promedio = total_ventas / unidades
    except ZeroDivisionError:
        print("No hay unidades")
        return 0
    
    return promedio
print(precio_promedio(500000, 4))
print(precio_promedio(500000, 0))
    
# %%
with open("ventas.csv", "w") as archivo:
    archivo.write("Producto,Unidades\n")
    archivo.write("Estufa A,15\n")
    archivo.write("Estufa C,42\n")
    archivo.write("Estufa E,7\n")
                  
# %%
with open("ventas.csv", "r") as archivo:
    for linea in archivo:
        print(linea, end="")
        
# %%
from utilidades import precio_final

print(precio_final(80000, 15))
# %%
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def valor_inventario(self):
        return self.precio * self.stock
    
estufa_a = Producto("Estufa A", 89990, 15)
estufa_c = Producto("Estufa C", 129990, 42)
print(estufa_a.nombre, estufa_a.valor_inventario())
print(estufa_c.nombre, estufa_c.valor_inventario())

# %%
