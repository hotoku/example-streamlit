"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import seaborn as sns

from exst.mod import get_df

df = get_df()

option = st.selectbox("which column ?", ["x", "x2"])

plot = sns.lineplot(x=option, y="y", data=df)


st.pyplot(plot.get_figure())  # type: ignore

"st.write"
st.write(df)

"st.table"
st.table(df)
