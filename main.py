"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import seaborn as sns

df = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "x2": [11, 12, 13, 14],
    "y": [10, 20, 30, 40]
})


option = st.selectbox("which column ?", ["x", "x2"])

plot = sns.lineplot(x=option, y="y", data=df)


st.pyplot(plot.get_figure())

"st.write"
st.write(df)

"st.table"
st.table(df)
