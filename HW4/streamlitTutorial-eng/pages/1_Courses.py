import streamlit as st
import pandas as pd
from utils.utils import *

if check_connection():

    query = "SELECT count(*) as n FROM Course;"
    result = execute_query(st.session_state["connection"], query)
    n_courses = [r[0] for r in result]

    query = "SELECT count(distinct type) as n FROM Course;"
    result = execute_query(st.session_state["connection"], query)
    n_types = [r[0] for r in result]
    
    query = "SELECT * FROM Course;"
    result = execute_query(st.session_state["connection"], query)
    courses = [r for r in result]
    
    query = "SELECT distinct type FROM Course;"
    result = execute_query(st.session_state["connection"], query)
    types = [r[0] for r in result]

    query = "SELECT level FROM Course ORDER BY level;"
    result = execute_query(st.session_state["connection"], query)
    levels = [r[0] for r in result]

    st.metric("Courses available", n_courses[0])
    st.metric("Types available", n_types[0])
    type = st.multiselect("Type:", types)
    level = st.slider("Level:", levels[0], levels[-1], (levels[0], levels[-1]))

    for c in courses:
        if c[2] in type and c[3] >= level[0] and c[3] <= level[1]:
            with st.expander("ID: "+str(c[0])+" Name: "+str(c[1])+" Type: "+str(c[2])+" Level: "+str(c[3]), expanded=False):
                query = "SELECT * FROM Schedule WHERE Cid='"+c[0]+"';"
                result = execute_query(st.session_state["connection"], query)
                lessons = [r for r in result]
                df = pd.DataFrame(lessons)
                st.dataframe(df)