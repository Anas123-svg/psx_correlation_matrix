import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

st.title("KSE-100 Stock Correlation Matrix")

conn = sqlite3.connect("psx_data.db")

corr_scaled_data = pd.read_sql("SELECT * FROM correlation_matrix", conn, index_col='index')
conn.close()

fig = px.imshow(
    corr_scaled_data,
    labels=dict(x="Stocks", y="Stocks", color="Correlation"),
    x=corr_scaled_data.columns,
    y=corr_scaled_data.index,
    color_continuous_scale='RdBu_r',
    zmin=-1,
    zmax=1,
    text_auto=".2f"
)

fig.update_layout(
    width=3000,
    height=3000,
    autosize=False
)

fig.update_traces(
    textfont_size=6,
    textfont_color="black"
)

st.plotly_chart(fig, use_container_width=True)
