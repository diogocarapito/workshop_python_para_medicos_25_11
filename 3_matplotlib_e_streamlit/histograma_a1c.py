import matplotlib.pyplot as plt
import numpy as np


def hba1c_histograma(
    dados, titulo="Histograma Hemoglobina A1c", max_y=None, max_x=None
):

    # Bins from 4 to the maximum value with a step of 0.5
    bins = np.arange(4, dados["Hemoglobina_A1c"].max() + 0.5, 0.5)

    colors = {"<6.5": "#009FFF", "6.5-8": "#77669D", ">8": "#ec2F4B"}

    fig, ax = plt.subplots(figsize=(8, 5))
    # Create the histogram
    n, bins, patches = ax.hist(dados["Hemoglobina_A1c"], bins=bins, edgecolor="black")

    # Apply colors based on the ranges
    for patch, left_edge in zip(patches, bins[:-1]):
        if left_edge < 6.5:
            patch.set_facecolor(colors["<6.5"])
        elif 6.5 <= left_edge < 8:
            patch.set_facecolor(colors["6.5-8"])
        else:
            patch.set_facecolor(colors[">8"])

    ax.set_title(titulo, fontsize=16)
    ax.set_xlabel("Hemoglobina A1c (%)", fontsize=14)
    ax.set_ylabel("Número de Pacientes", fontsize=14)
    ax.tick_params(labelsize=12)

    # Add a vertical line for the mean
    media_hba1c = dados["Hemoglobina_A1c"].mean()
    ax.axvline(media_hba1c, color="blue", linestyle="dashed", linewidth=1)
    ax.text(
        media_hba1c + 0.1,
        ax.get_ylim()[1] * 0.9,
        f"Média: {media_hba1c:.2f}%",
        color="blue",
        fontsize=12,
    )

    # numero de contagems por barra no topo de cada barra
    for i in range(len(n)):
        if n[i] > 0:
            ax.text(
                bins[i] + 0.25,
                n[i] + 0.5,
                f"{int(n[i])}",
                ha="center",
                va="bottom",
                fontsize=10,
            )

    # ajustar valor máximo do eixo y para 10% acima do maior valor de n
    if max_y is None:
        ax.set_ylim(0, max(n) * 1.1)
    else:
        ax.set_ylim(0, max_y)

    if max_x is not None:
        ax.set_xlim(0, max_x)

    # Add a vertical line for x=9
    ax.axvline(9, color="red", linestyle="dotted", linewidth=1)
    ax.text(
        9 + 0.1,
        ax.get_ylim()[1] * 0.4,
        "x=9",
        color="red",
        fontsize=12,
    )

    # Add the total number of patients at the top
    total_pacientes = dados.shape[0]
    ax.text(
        ax.get_xlim()[1] * 0.95,
        ax.get_ylim()[1] * 0.98,
        f"n={total_pacientes}",
        ha="right",
        va="top",
        fontsize=12,
        # bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
    )

    return fig, ax
