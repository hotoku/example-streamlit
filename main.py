import streamlit as st
import seaborn as sns

from exst.data_source import get_df

df = get_df()

option = st.selectbox("which column ?", ["x", "x2"])

plot = sns.lineplot(x=option, y="y", data=df)


st.pyplot(plot.get_figure())  # type: ignore

"st.write"
st.write(df)

"st.table"
st.table(df)
