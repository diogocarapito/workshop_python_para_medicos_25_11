import streamlit as st

def page1():
    st.title("Página 1")
    
    with st.sidebar:
        if st.button("mostrar dados"):
            st.write("Aqui estão os dados...")

def page2():
    st.title("Página 2")

pg = st.navigation([page1, page2])
pg.run()