import streamlit as st
import pandas as pd
from histograma_a1c import hba1c_histograma

st.title("Evolução de HbA1c ao longo dos trimestres")

data_a1c_path = "data/hba1c_por_trimestres.csv"

# data load
data_a1c = pd.read_csv(data_a1c_path)

# get unique trimesters
list_trimestres = data_a1c["trimeste"].unique().tolist()

# reverse sort trimesters
list_trimestres.sort(reverse=True)

# slider to select trimester
trimestre_selecionado = st.select_slider(
    "Selecione o trimestre", options=list_trimestres
)

# filter data for selected trimester
data_a1c_selecionado = data_a1c[data_a1c["trimeste"] == trimestre_selecionado]

# number of patients with HbA1c > 9
num_pacientes_acima_9 = data_a1c_selecionado[
    data_a1c_selecionado["Hemoglobina_A1c"] > 9
].shape[0]

# display selected trimester
st.subheader(f"Trimestre selecionado - {trimestre_selecionado}")

# display metrics in 4 columns
col1, col2, col3, col4 = st.columns(4)

# total patients with HbA1c measured
with col1:
    st.metric(
        label="Total utentes com HbA1c medido", value=data_a1c_selecionado.shape[0]
    )

# mean HbA1c
with col2:
    st.metric(
        label="Média HbA1c (%)",
        value=f"{data_a1c_selecionado['Hemoglobina_A1c'].mean():.2f}%",
    )

# patients with HbA1c >9%
with col3:
    st.metric(label="Nº utentes HbA1c >9%", value=num_pacientes_acima_9)

# percentage of patients with HbA1c >9%
with col4:
    st.metric(
        label="% Utentes HbA1c >9%",
        value=f"{(num_pacientes_acima_9 / data_a1c_selecionado.shape[0] * 100):.1f}%",
    )

# plot histogram
fig, ax = hba1c_histograma(
    data_a1c_selecionado,
    titulo=f"Hemoglobina A1c - {trimestre_selecionado}",
    max_y=50,
    max_x=16,
)

# display plot with streamlit
st.pyplot(fig)
