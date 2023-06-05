import streamlit as st
import pandas as pd
from utils.utils import *

if check_connection():
    with st.form("New course"):
        cid = st.text_input("CId: ")
        name = st.text_input("Name: ")
        type = st.text_input("Type: ")
        level = st.number_input("Level: ", 1, 4)
        submitted = st.form_submit_button("Create")


    if submitted:

        if not cid or not name or not type or not level:
            st.error("Incomplete form")
        else:
            st.success("Done")
            query = f"INSERT INTO Course VALUES ('{cid}', '{name}', '{type}', {level})"
            execute_query(st.session_state["connection"], query)
