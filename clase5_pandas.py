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
