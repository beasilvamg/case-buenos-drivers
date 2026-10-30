import pandas as pd
import pingouin as pg


df = pd.read_excel("base_buenos_drivers.xlsx", sheet_name="BASE_NUMERICA")

#Confiança
print("\nDistribuição das perguntas de Confiança:")

print("\nConfianca1:")
print(df["Confianca1"].value_counts().sort_index())

print("\nConfianca2:")
print(df["Confianca2"].value_counts().sort_index())

print("\nConfianca3:")
print(df["Confianca3"].value_counts().sort_index())

print("\nConfianca4:")
print(df["Confianca4"].value_counts().sort_index())

print("\nConfianca5:")
print(df["Confianca5"].value_counts().sort_index())

print("\nConfianca6:")
print(df["Confianca6"].value_counts().sort_index())

print("\nConfianca7:")
print(df["Confianca7"].value_counts().sort_index())

print("\nConfianca8:")
print(df["Confianca8"].value_counts().sort_index())

print("\nConfianca9:")
print(df["Confianca9"].value_counts().sort_index())


print("\nCorrelação entre as perguntas de Confiança:")
print(
    df[
        [
            "Confianca1",
            "Confianca2",
            "Confianca3",
            "Confianca4",
            "Confianca5",
            "Confianca6",
            "Confianca7",
            "Confianca8",
            "Confianca9"
        ]
    ].corr()
)


itens_confianca = df[
    [
        "Confianca1",
        "Confianca2",
        "Confianca3",
        "Confianca4",
        "Confianca5",
        "Confianca6",
        "Confianca7",
        "Confianca8",
        "Confianca9"
    ]
]

print("\nConsistência interna - Confiança:")
print(pg.cronbach_alpha(data=itens_confianca))


df["Confianca_media"] = df[
    [
        "Confianca1",
        "Confianca2",
        "Confianca3",
        "Confianca4",
        "Confianca5",
        "Confianca6",
        "Confianca7",
        "Confianca8",
        "Confianca9"
    ]
].mean(axis=1)

print("\nConfianca_media:")
print(df["Confianca_media"].to_string())


print("\nEstatísticas da Confiança média:")

print("Média:", round(df["Confianca_media"].mean(), 2))
print("Mediana:", round(df["Confianca_media"].median(), 2))
print("Desvio-padrão:", round(df["Confianca_media"].std(), 2))
print("Mínimo:", round(df["Confianca_media"].min(), 2))
print("Máximo:", round(df["Confianca_media"].max(), 2))


#Segurança
print("\nDistribuição da Segurança1:")

frequencia_seguranca1 = (
    df["Segurança1"]
    .value_counts()
    .sort_index()
)

percentual_seguranca1 = (
    df["Segurança1"]
    .value_counts(normalize=True)
    .sort_index()
    .mul(100)
    .round(1)
)

tabela_seguranca1 = pd.DataFrame({
    "Pessoas": frequencia_seguranca1,
    "%": percentual_seguranca1
})

print(tabela_seguranca1)

print("\nEstatísticas descritivas da Segurança1:")
print(df["Segurança1"].describe())


# Segurança3
"""print("\nDistribuição da Segurança3:")

frequencia_seguranca3 = (
    df["Segurança3"]
    .value_counts()
    .sort_index()
)

percentual_seguranca3 = (
    df["Segurança3"]
    .value_counts(normalize=True)
    .sort_index()
    .mul(100)
    .round(1)
)

tabela_seguranca3 = pd.DataFrame({
    "Pessoas": frequencia_seguranca3,
    "%": percentual_seguranca3
})

print(tabela_seguranca3)

print("\nEstatísticas descritivas da Segurança3:")
print(df["Segurança3"].describe())"""


# Segurança3 — recodificação da escala
df["Seguranca3_invertida"] = 8 - df["Segurança3"]

print("\nSegurança3 original × Segurança3 invertida:")

print(
    df[
        ["Segurança3", "Seguranca3_invertida"]
    ].to_string()
)


print("\nSegurança1 × Segurança3 invertida:")

correlacao_seguranca = df[
    ["Segurança1", "Seguranca3_invertida"]
].corr()

print(correlacao_seguranca.round(3))