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
