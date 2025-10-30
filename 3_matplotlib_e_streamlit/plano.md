# Plano

1. **Introdução (15 min)**

    - Por que a visualização é importante na prática clínica e na investigação.
    - Exemplo: tendência de pacientes por mês, valores laboratoriais ou uso de medicação.
    - O que torna uma boa visualização: clareza, simplicidade, narrativa.

    **Demonstração**: Mostrar um exemplo de dashboard (previamente construído no Streamlit).

2. **Fundamentos de Visualização (55 min)**

    **Objetivo**: Criar gráficos significativos usando Python.

    **Tópicos**:
    - Importar dados com `pandas`.
    - Noções básicas de gráficos com `matplotlib`.
    - Gráficos estatísticos simples com `seaborn`.
    - Gráficos de linha (tendências ao longo do tempo).
    - Gráficos de barras (comparação por categoria).
    - Box plots (distribuição entre grupos).
    - Gráficos de dispersão (correlação).

    **Exemplo de Conjunto de Dados**:

    ```python
    import seaborn as sns
    df = sns.load_dataset("tips")  # ou um pequeno conjunto de dados clínicos anonimizados
    ```

    Ou pode preparar um pequeno ficheiro CSV como:
    - Data, Clínica, Pacientes Atendidos, Tempo Médio de Espera, etc.

    **Exercício**: Representar tendências no volume de pacientes e comparar clínicas.

3. **Pausa & Q&A (10 min)**

4. **Introdução ao Streamlit (50 min)**

    **Conceitos**:
    - O que é o Streamlit e por que é útil para dashboards de dados em saúde.
    - Instalação e primeira execução.
    - Estrutura básica:

    ```python
    import streamlit as st
    st.title("Dashboard de Dados da Clínica")
    st.write("Bem-vindo ao seu relatório interativo!")
    ```

    - Widgets: sliders, dropdowns, seletores de data.
    - Exibir gráficos com `st.pyplot()` ou `st.line_chart()`.

    **Exibir DataFrames e Gráficos**:
    - Widgets (selectbox, slider, checkbox).
    - Layout (colunas, abas, barra lateral).

    **Exercício**: Construir uma mini aplicação que:
    - Exibe um conjunto de dados.
    - Permite ao utilizador filtrar por data ou categoria.
    - Atualiza um gráfico matplotlib/seaborn de forma interativa.

5. **Mãos na Massa: Construção da Aplicação (45 min)**

    Os participantes expandem o que construíram anteriormente.

    **Exemplo**:

    ```python
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    st.title("Dashboard de Atividade da Clínica")

    uploaded_file = st.file_uploader("Carregue os seus dados (CSV)", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())

        clinic = st.selectbox("Selecione a clínica", df["Clinic"].unique())
        filtered = df[df["Clinic"] == clinic]

        fig, ax = plt.subplots()
        sns.lineplot(data=filtered, x="Date", y="Patients", ax=ax)
        st.pyplot(fig)
    ```

    **Resultado**: Cada participante terá uma aplicação funcional.

6. **Encerramento (5 min)**

    - Recapitulação: “Hoje aprendemos como ir de dados → insights → aplicação.”
    - Incentivar a partilha de aplicações Streamlit (ex.: Streamlit Cloud).
    - Partilhar recursos de aprendizagem:
        - Documentação do Streamlit.
        - Tutoriais do Seaborn.
        - Guias de visualização do Real Python.
