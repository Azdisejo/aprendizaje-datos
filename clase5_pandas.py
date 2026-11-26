# %%
import pandas as pd

df = pd.read_csv("ventas_estufas.csv")
df["ingreso"] = df["unidades"] * df["precio_unitario"]
df.head()
# %%
df.iloc[0]
# %%
df.iloc[0:3]
# %%
df.iloc[-1]
# %%
df.iloc[-4:]
# %%
df.tail(4)
# %%
df.loc[8, "ingreso"]
# %%
df.loc[df["region"] == "RM", ["mes", "producto", "unidades"]]
# %%
df.loc[(df["producto"] == "Estufa B") & (df["unidades"] > 200), ["mes", "region", "ingreso"]]
# %%
df["fecha"] = pd.to_datetime(df["mes"])
df.info()
# %%
df["num_mes"] = df["fecha"].dt.month
df["nombre_mes"] = df["fecha"].dt.month_name()
df.head()
# %%
meses = {4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre"}
df["nombre_mes"] = df["num_mes"].map(meses)
df.head()
# %%
df.tail(4)
# %%
df.groupby(["nombre_mes", "region"])["unidades"].sum()
# %%
pd.pivot_table(df, values="unidades", index="num_mes", columns="region", aggfunc="sum")
# %%
tabla = pd.pivot_table(df, values="ingreso", index="num_mes", columns="producto", aggfunc="sum")
tabla.sort_values("Estufa B", ascending=False)
# %%
