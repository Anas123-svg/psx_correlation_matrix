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

num_rows = corr_scaled_data.shape[0]
num_cols = corr_scaled_data.shape[1]

params = st.query_params
screen_width = int(params.get("width", 1200)) if params.get("width") else 1200

base_font_size = max(6, min(12, screen_width // 120))
cell_size = max(20, min(40, screen_width // 40))

fig_width = num_cols * cell_size
fig_height = num_rows * cell_size

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
    autosize=False,
    width=fig_width,
    height=fig_height + 100,
    margin=dict(l=20, r=20, t=60, b=40),
    font=dict(family="Arial", size=base_font_size),
)

fig.update_traces(
    textfont_size=base_font_size,
    textfont_color="black",
    colorbar=dict(
        orientation="h",
        thickness=10,
        len=0.6,
        y=1.02,
        yanchor="bottom",
        x=0.5,
        xanchor="center",
        tickfont=dict(size=base_font_size),
        title=dict(
            text="Correlation",
            side="top",
            font=dict(size=base_font_size + 2)
        )
    )
)

st.plotly_chart(fig, use_container_width=True)
