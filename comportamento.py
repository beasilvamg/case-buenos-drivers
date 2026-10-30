import pandas as pd
import pingouin as pg


df = pd.read_excel("base_buenos_drivers.xlsx", sheet_name="BASE_NUMERICA")


# Intenção de Usar Buenos Drivers
print("\nDistribuição das perguntas de Intenção:")

print("\nIntenção1:")
print(df["Intenção1"].value_counts().sort_index())

print("\nIntenção2:")
print(df["Intenção2"].value_counts().sort_index())

print("\nIntenção3:")
print(df["Intenção3"].value_counts().sort_index())


print("\nEstatísticas descritivas - Intenção:")

print("\nIntenção1:")
print(df["Intenção1"].describe())

print("\nIntenção2:")
print(df["Intenção2"].describe())

print("\nIntenção3:")
print(df["Intenção3"].describe())


print("\nCorrelação entre as perguntas de Intenção:")

itens_intencao = df[
    [
        "Intenção1",
        "Intenção2",
        "Intenção3"
    ]
]

print(itens_intencao.corr())


print("\nConsistência interna - Intenção:")

print(
    pg.cronbach_alpha(
        data=itens_intencao
    )
)


df["Intencao_media"] = df[
    ["Intenção1", "Intenção2", "Intenção3"]
].mean(axis=1)

print("\nIntenção média:")
print(df["Intencao_media"].describe())