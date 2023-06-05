import streamlit as st
import pandas as pd
from utils.utils import *

if check_connection():
    query = "SELECT ssn FROM Trainer;"
    result = execute_query(st.session_state["connection"], query)
    ssns = [r[0] for r in result]

    query = "SELECT distinct cid FROM Course;"
    result = execute_query(st.session_state["connection"], query)
    cids = [r[0] for r in result]

    with st.form("New lesson"):
        ssn = st.selectbox("SSN:", ssns)
        day = st.selectbox("Day: ", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        time = st.text_input("Start time:")
        durantion = st.number_input("Durantiom: ", 1, 60)
        cid = st.selectbox("CId: ", cids)
        gym = st.text_input("Gym room:")

        submitted = st.form_submit_button("Create")


    if submitted:

        query = "SELECT count(*) as n FROM Schedule WHERE day='"+day+"' AND cid='"+cid+"';"
        result = execute_query(st.session_state["connection"], query)
        n = [r[0] for r in result]

        if not ssn or not day or not time or not durantion or not cid or not gym:
            st.error("Incomplete form")

        elif n[0] != 0:
            st.error("The course is already scheduled for that day.") 

        else:
            st.success("Done")
            query = f"INSERT INTO Schedule VALUES ('{ssn}', '{day}', '{time}', {durantion}, '{cid}', '{gym}')"
            execute_query(st.session_state["connection"], query)
