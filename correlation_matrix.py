import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
st.title("KSE-100 Stock Correlation Matrix")

def optimize_sqlite(conn):
    conn.execute("PRAGMA cache_size = -10000")     
    conn.execute("PRAGMA temp_store = MEMORY")     
    conn.execute("PRAGMA journal_mode = OFF")      

conn = sqlite3.connect("psx_data.db")
optimize_sqlite(conn)

corr_scaled_data = pd.read_sql("SELECT * FROM correlation_matrix", conn, index_col='index')
conn.close()

corr_scaled_data = corr_scaled_data.iloc[:100, :100]

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
    autosize=True,
    height=3000,
    width=3000,
    margin=dict(l=50, r=50, t=50, b=50)
)

fig.update_traces(
    textfont_size=8,
    textfont_color="black",
    colorbar=dict(
        thickness=15,
        len=0.18,
        xpad=10
    )
)

st.plotly_chart(fig, use_container_width=True)
