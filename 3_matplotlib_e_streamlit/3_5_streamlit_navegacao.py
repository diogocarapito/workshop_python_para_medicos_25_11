import streamlit as st


def page1():
    st.title("Piramide etária do RNU")

    st.image("3_matplotlib_e_streamlit/piramide_etaria_pt.png")


def page2():
    st.title("Piramide etária da Lista de utentes")

    st.image("3_matplotlib_e_streamlit/piramide_etaria_lista_medico.png")


pg = st.navigation([page1, page2])
pg.run()
