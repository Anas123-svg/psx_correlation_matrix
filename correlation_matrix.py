import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
st.title("📊 KSE-100 Stock Correlation Matrix")

def optimize_sqlite(conn):
    conn.execute("PRAGMA cache_size = -10000")
    conn.execute("PRAGMA temp_store = MEMORY")
    conn.execute("PRAGMA journal_mode = OFF")

conn = sqlite3.connect("psx_data.db")
optimize_sqlite(conn)

corr_scaled_data = pd.read_sql("SELECT * FROM correlation_matrix", conn, index_col='index')
conn.close()
corr_scaled_data = corr_scaled_data.iloc[:50, :50]  

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
    height=2000,     
    width=2000,     
    margin=dict(l=40, r=40, t=40, b=40),
    font=dict(family="Arial", size=12),
)

fig.update_traces(
    textfont_size=6,
    textfont_color="black",
    colorbar=dict(
        orientation="h",        # Horizontal bar
        thickness=10,            # Thin height of colorbar
        len=0.01,                # Short length (relative to full width)
        y=1.1,                  # Push it above the matrix
        yanchor="bottom",
        x=0.5,
        xanchor="center",
        tickfont=dict(size=8),
        title=dict(
            text="Correlation",
            side="top",
            font=dict(size=10)
        )
    )
)



st.plotly_chart(fig, use_container_width=True)
