
import pandas as pd
import pingouin as pg

df = pd.read_excel("base_buenos_drivers.xlsx", sheet_name="BASE_NUMERICA")

#Média da Confiança
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


#Média da Intenção
df["Intencao_media"] = df[
    ["Intenção1", "Intenção2", "Intenção3"]
].mean(axis=1)

#Vizualizando as duas unidas
print(
    df[
        ["Confianca_media", "Intencao_media"]
    ].head(20)
)


print("\nConfiança × Intenção:")

print(
    df[
        ["Confianca_media", "Intencao_media"]
    ].head(20)
)

#Correlação
correlacao = df[
    ["Confianca_media", "Intencao_media"]
].corr()

print("\nCorrelação entre Confiança e Intenção:")
print(correlacao.round(3))


#Intenção e Comunicação
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


print("\nComunicação × Intenção — dados dos participantes:")

print(
    df[
        ["Comunicacao_media", "Intencao_media"]
    ].to_string()
)


print("\nCorrelação entre Comunicação e Intenção:")

correlacao = df[
    ["Comunicacao_media", "Intencao_media"]
].corr()

print(correlacao.round(3))


#Segurança e Intenção
print("\nSegurança1 × Intenção — dados dos participantes:")

print(
    df[
        ["Segurança1", "Intencao_media"]
    ].to_string()
)

print("\nCorrelação entre Segurança1 e Intenção:")

correlacao = df[
    ["Segurança1", "Intencao_media"]
].corr()

print(correlacao.round(3))


#Intenção e Aversão
df["Aversao_media"] = df[
    ["Aversao1", "Aversao2", "Aversao3", "Aversao4"]
].mean(axis=1)


print("\nTabela Aversão a Risco × Intenção:")

print(
    df[
        ["Aversao_media", "Intencao_media"]
    ].to_string()
)


print("\nCorrelação entre Aversão a Risco e Intenção:")

cor_risco_intencao = df[
    ["Aversao_media", "Intencao_media"]
].corr()

print(
    cor_risco_intencao.round(3)
)

#Idade e Itenção
# Média da intenção
df["Intencao_media"] = df[
    ["Intenção1", "Intenção2", "Intenção3"]
].mean(axis=1)

# Transformar idade em número
df["Idade_num"] = (
    df["Idade"]
    .astype(str)
    .str.replace(" anos", "", regex=False)
    .astype(int)
)

# Criar as mesmas faixas etárias
df["Faixa_etaria"] = pd.cut(
    df["Idade_num"],
    bins=[17, 24, 34, 44, 54, 62],
    labels=["18–24", "25–34", "35–44", "45–54", "55–62"]
)

# Intenção média por faixa etária
resultado = df.groupby(
    "Faixa_etaria",
    observed=False
)["Intencao_media"].mean()

print("Intenção média por faixa etária:")
print(resultado.round(2))


#Renda e Intenção
resultado = df.groupby(
    "Renda_Individual",
    observed=False
)["Intencao_media"].agg(["count", "mean"])

resultado["mean"] = resultado["mean"].round(2)

print(resultado)

#Genero e Intenção
resultado = df.groupby(
    "Genero"
)["Intencao_media"].agg(["count", "mean"])

resultado["mean"] = resultado["mean"].round(2)

print("Intenção média por gênero:")
print(resultado)

#Filhoa e Itenção
resultado = df.groupby(
    "Filhos"
)["Intencao_media"].agg(["count", "mean"])

resultado["mean"] = resultado["mean"].round(2)

print("Intenção média por número de filhos:")
print(resultado)

#MoradoresxIntenção
resultado = df.groupby(
    "Cidade_é_buenos_aires"
)["Intencao_media"].agg(["count", "mean"])

resultado["mean"] = resultado["mean"].round(2)

print("Intenção média por morador de Buenos Aires:")
print(resultado)

for coluna in ['Confianca1', 'Confianca2', 'Confianca3',
               'Confianca4', 'Confianca5', 'Confianca6',
               'Confianca7', 'Confianca8', 'Confianca9']:

    r = df[coluna].corr(df['Intencao_media'])
    print(coluna, round(r, 3))