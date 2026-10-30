import pandas as pd

df = pd.read_excel("base_buenos_drivers.xlsx", sheet_name="BASE_NUMERICA")

print("\nValores ausentes:")
print(df.isna().sum())

print(f"\nTamanho da amostra: {len(df)}")

print(f"\nGenero:")
print(df["Genero"].value_counts())

print("\nIdade:")
print("Mínima:", df["Idade"].min())
print("Máxima:", df["Idade"].max())

print("\nQuantidade de pessoas por idade:")
print(df["Idade"].value_counts().sort_index())


print("\nDistribuição por faixa etária:")

faixas = pd.cut(
    pd.to_numeric(df["Idade"].str.replace(" anos", "")),
    bins=[17, 24, 34, 44, 54, 62],
    labels=["18–24", "25–34", "35–44", "45–54", "55–62"]
)

print(faixas.value_counts().sort_index())

print("\nDistribuição por renda:")
print(df["Renda_Individual"].value_counts())

print("\nMorador de Buenos Aires:")
distribuicao = df["Cidade_é_buenos_aires"].value_counts().rename({1: "Sim", 0: "Não"})
print(distribuicao)
print("Total:", distribuicao.sum())


print("\nDistribuição de filhos:")
print(df["Filhos"].value_counts())