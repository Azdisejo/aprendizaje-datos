# %%
import pandas as pd
print(pd.__version__)
# %%
df = pd.read_csv("ventas_estufas.csv")
df.head()
# %%
df.shape
# %%
df.info()

# %%
df.describe()
# %%
df["unidades"]
# %%
df[["mes", "region", "unidades"]]
# %%
df[df["region"] == "RM"]
# %%
df[df["unidades"] > 300]
# %%
df["ingreso"] = df["unidades"] * df["precio_unitario"]
df.head()
# %%
df[(df["region"] == "Biobio") & (df["producto"] == "Estufa B")]
# %%
df.sort_values("ingreso", ascending=False).head(3)
# %%
df.groupby("region")["ingreso"].sum()
# %%
df.groupby("producto")["ingreso"].sum()
# %%
df.groupby("mes")["unidades"].sum().sort_values(ascending=False)
# %%

