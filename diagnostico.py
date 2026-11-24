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
