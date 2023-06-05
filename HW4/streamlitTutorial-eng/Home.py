import streamlit as st
from utils.utils import *

st.set_page_config(
    page_title="Homepage",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Homework s4"
    }
)

st.markdown("# :red[Homework] 4")
st.markdown("**GOAL**: Create a web application in Python (Streamlit) that can interact with a MySQL database to perform queries based on user interactions.")

if "connection" not in st.session_state.keys():
    st.session_state["connection"]=False

check_connection()