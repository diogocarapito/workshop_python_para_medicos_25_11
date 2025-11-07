import streamlit as st

# titles and headers e subheaders

st.title("Título com st.title()")

st.header("Header com st.header()")

st.subheader("Subheader com st.subheader()")

# st.write()

st.write("st.write() permite colocar qualquer coisa, desde texto simples a dataframes e gráficos.")

# st.markdown()

st.markdown("""
**negrito** com `st.markdown()`
""")

st.markdown("[link para API reference Streamlit](https://docs.streamlit.io/develop/api-reference)")

# st.text() e st.code()

st.text("Texto simples com st.text()")

st.code("""
# código em python com st.code()
import streamlit as st
st.title("Hello streamlit!")
""")

st.markdown("""Mas também dá mostrar código com markdown:
```python
# código em python com st.markdown
import streamlit as st
st.title("Hello streamlit!")
```""")

# st.divider()
st.divider()


import pandas as pd

# Simulated health data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May",
                "Jun"],
    "New Patients": [120, 135, 160, 180, 210, 190],
    "Follow-ups": [80, 95, 110, 120, 140
                , 130]
}
df = pd.DataFrame(data)

st.dataframe(df)

if st.button("Mostrar Gráfico de Linhas"):
    st.line_chart(df.set_index("Month"))