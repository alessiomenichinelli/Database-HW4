import streamlit as st
import pandas as pd
from utils.utils import *
import datetime

if check_connection():

    surname = st.text_input("Last name: ")
    birth = st.date_input("Date of birt: ", value=(datetime.date(1970,1,1), datetime.date(1990,1,1)))

    query = "SELECT * FROM Trainer WHERE surname LIKE '"+surname+"%' AND dateofbirth>'"+str(birth[0])+"' AND dateofbirth<'"+str(birth[1])+"';"
    result = execute_query(st.session_state["connection"], query)
    trainers = [r for r in result]

    df = pd.DataFrame(trainers)
    
    for index, row in df.iterrows():
        st.dataframe(row)