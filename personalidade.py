import pandas as pd
import pingouin as pg

df = pd.read_excel("base_buenos_drivers.xlsx", sheet_name="BASE_NUMERICA")

"""print("\nAversão a risco:")

print("\nAversao1:")
print(df["Aversao1"].value_counts().sort_index())

print("\nAversao2:")
print(df["Aversao2"].value_counts().sort_index())

print("\nAversao3:")
print(df["Aversao3"].value_counts().sort_index())

print("\nAversao4:")
print(df["Aversao4"].value_counts().sort_index())


print("\nCorrelação entre as perguntas de Aversão a Risco:")
print(df[["Aversao1", "Aversao2", "Aversao3", "Aversao4"]].corr())


print("\nConsistência interna - Aversão a Risco:")

alfa = pg.cronbach_alpha(
    data=df[["Aversao1", "Aversao2", "Aversao3", "Aversao4"]]
)

print(alfa)"""

df["Aversao_media"] = df[
    ["Aversao1", "Aversao2", "Aversao3", "Aversao4"]
].mean(axis=1)

print("\nIndicador de Aversão a Risco:")
print(df["Aversao_media"].to_string())

#Agrupando os 200 em cada média
print("\nDistribuição da Aversao_media:")
print(df["Aversao_media"].value_counts().sort_index())
