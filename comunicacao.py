import pandas as pd
import pingouin as pg


df = pd.read_excel("base_buenos_drivers.xlsx", sheet_name="BASE_NUMERICA")


print("\nDistribuição das perguntas de Comunicação:")

itens_comunicacao = [
    "Comunicação1",
    "Comunicação2",
    "Comunicação3",
    "Comunicação4",
    "Comunicação5",
    "Comunicação6",
    "Comunicação7"
]

for item in itens_comunicacao:
    print(f"\n{item}:")
    print(df[item].value_counts().sort_index())


print("\nEstatísticas descritivas - Comunicação:")

for item in itens_comunicacao:
    print(f"\n{item}:")
    print(df[item].describe())


print("\nCorrelação entre as perguntas de Comunicação:")

itens_comunicacao = df[
    [
        "Comunicação1",
        "Comunicação2",
        "Comunicação3",
        "Comunicação4",
        "Comunicação5",
        "Comunicação6",
        "Comunicação7"
    ]
]

print(itens_comunicacao.corr())


print("\nConsistência interna - Comunicação:")

alpha_comunicacao = pg.cronbach_alpha(
    data=itens_comunicacao
)

print(alpha_comunicacao)


df["Comunicacao_media"] = df[
    [
        "Comunicação1",
        "Comunicação2",
        "Comunicação3",
        "Comunicação4",
        "Comunicação5",
        "Comunicação6",
        "Comunicação7"
    ]
].mean(axis=1)

print("\nEstatísticas da Comunicação média:")
print(df["Comunicacao_media"].describe())


# Criar média de Intenção
df["Intencao_media"] = df[
    ["Intenção1", "Intenção2", "Intenção3"]
].mean(axis=1)

# Correlação entre Comunicação5 e Intenção
correlacao = df["Comunicação5"].corr(df["Intencao_media"])

print(
    f"\nCorrelação entre Comunicação5 e Intenção de Uso: "
    f"{correlacao:.3f}"
)

