import pandas as pd
import matplotlib.pyplot as plt

dados_distribuição_etária_pt = "../data/distribuicao_etaria_lista_medico.csv"
#dados_distribuição_etária_pt = "../data/distribuicao_etaria_RUN_2024_12.csv"

dados = pd.read_csv(dados_distribuição_etária_pt)

print(dados)

# inicir o plot
fig, ax = plt.subplots(figsize=(8, 8))

# calculo de metricas
total_mulheres = dados["Mulher"].sum()
total_homens = dados["Homem"].sum()
valor_maximo = max(dados["Mulher"].max(), dados["Homem"].max())

# plot das mulheres
ax.barh(
    y=dados["Faixa_etária_5"],
    width=dados["Mulher"],
    color="lightcoral",
    label=f"Mulher (n={total_mulheres:,})",
)

#plot dos homens
ax.barh(
    y=dados["Faixa_etária_5"],
    width=-dados["Homem"],
    color="steelblue",
    label=f"Homem (n={total_homens:,})",
)

# títulos e labels
ax.set_title("Pirâmide Etária - RNU dez 2024", fontsize=16)

ax.set_xlabel("Número de Inscritos", fontsize=14)
ax.set_ylabel("Faixa Etária", fontsize=14)

# ajustar tamanho dos labels dos eixos
ax.tick_params(axis="y", labelsize=12)

# localização da legenda
ax.legend(loc="upper left", fontsize=14)

# adicionar grid no eixo x
ax.grid(axis="x", linestyle="--", alpha=0.7)

# add number on top of each bar
for i, faixa in enumerate(dados["Faixa_etária_5"]):
    mulher_count = dados.loc[dados["Faixa_etária_5"] == faixa, "Mulher"].values[0]
    homem_count = dados.loc[dados["Faixa_etária_5"] == faixa, "Homem"].values[0]

    ax.text(
        mulher_count + 0.01 * valor_maximo,  # small offset to the right
        i,
        f"{mulher_count:,}",
        va="center",
        fontsize=10,
        color="black",
    )

    ax.text(
        -homem_count - 0.01 * valor_maximo,  # small offset to the left
        i,
        f"{homem_count:,}",
        va="center",
        fontsize=10,
        color="black",
        ha="right",
    )

# set min and max for x axis 20% grater than the max value
fator = 1.24

ax.set_xlim(-valor_maximo * fator, valor_maximo * fator)

# Remover o sinal de "-" dos rótulos do eixo x
# ir buscar os valores atuais dos ticks do eixo x
xticks = ax.get_xticks()

# Criar novos rótulos para os ticks, removendo o sinal de "-" e formatando os números grandes
xtick_labels = []
for x in xticks:
    xtick_labels.append(f"{abs(int(x)):,}")

# voltamos a definir os novos rótulos no eixo x
ax.set_xticklabels(xtick_labels)

# guardar
fig.savefig("piramide_etaria_pt.png", bbox_inches="tight")

# #dados_distribuição_etária_uls = "../data/bicsp_distribuicao_inscrições_csp_ULS_ASI_2024_12.csv"
