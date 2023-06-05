import streamlit as st
import pandas as pd
from utils.utils import *

if check_connection():
    
    query = "SELECT starttime AS 'Start time', count(*) as n FROM Schedule GROUP BY starttime"
    result = execute_query(st.session_state["connection"], query)
    times = [r for r in result]

    df = pd.DataFrame(times)
    st.bar_chart(df, x = 'Start time', y = 'n')

    query = "SELECT day AS 'Day', count(*) as n FROM Schedule GROUP BY day"
    result = execute_query(st.session_state["connection"], query)
    days = [r for r in result]
    
    df = pd.DataFrame(days)
    st.line_chart(df, x="Day", y="n")