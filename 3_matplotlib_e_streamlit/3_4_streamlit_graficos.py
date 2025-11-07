import streamlit as st
import matplotlib.pyplot as plt


st.title("Dashboard de Consultas Mensais")

st.divider()

# Dados de exemplo
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
new_patients = [120, 135, 160, 180, 210, 190]
follow_ups = [80, 95, 110, 120, 140, 130]

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(months, new_patients, marker="o", label="Novos Pacientes", color="royalblue")
ax.plot(
    months, follow_ups, marker="o", label="Follow-ups", color="orange", linestyle="--"
)

# definir títulos e etiquetas
ax.set_title("Consultas Mensais (Centro de Saúde Primária)")
ax.set_xlabel("Mês")
ax.set_ylabel("Número de Visitas")

# definir legenda e grelha
ax.legend(title="Tipo de Visita")
#ax.grid(True)

# exibir o gráfico no Streamlit
st.pyplot(fig)

st.markdown("Gráfico gerado com Matplotlib e exibido no Streamlit.")

# botão para gravar o gráfico como PNG
st.button(
    "Gravar Gráfico como PNG",
    key="gravar_matplotlib",
    on_click=lambda: fig.savefig("3_matplotlib_e_streamlit/consultas_mensais_matplotlib.png"),
)

st.divider()

# same graph with plotly
import plotly.express as px
import pandas as pd

# prepar dados em formato DataFrame
data = {"Month": months, "New Patients": new_patients, "Follow-ups": follow_ups}
df = pd.DataFrame(data)

# criar o gráfico de linhas com plotly express
fig2 = px.line(
    df,
    x="Month",
    y=["New Patients", "Follow-ups"],
    title="Consultas Mensais (Centro de Saúde Primária)",
    markers=True,
    labels={"value": "Número de Visitas", "variable": "Tipo de Visita"},
)

# Update layout and customize traces
fig2.update_layout(
    title_font=dict(size=20),
    xaxis_title="Mês",
    yaxis_title="Número de Visitas",
    legend_title="Tipo de Visita",
    template="plotly_white",
)

# Customize the "Follow-ups" line to be orange and dashed
fig2.update_traces(
    line=dict(color="orange", dash="dash"), selector=dict(name="Follow-ups")
)

st.plotly_chart(fig2)
st.markdown("Gráfico gerado com Plotly e exibido no Streamlit.")

st.button(
    "Gravar Gráfico como PNG",
    key="gravar_plotly",
    on_click=lambda: fig2.write_image(
        "3_matplotlib_e_streamlit/consultas_mensais_plotly.png",
        width=800,
        height=600
    ),
)


