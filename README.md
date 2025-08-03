# 📊 PSX KSE-100 Correlation Matrix Visualization

This project provides an interactive **correlation matrix heatmap** of stocks listed in the **KSE-100 index** of the **Pakistan Stock Exchange (PSX)**.

The visualization is built using `Plotly` and deployed using `Streamlit`. It shows the degree of correlation between daily **closing prices** of top KSE-100 stocks based on historical data.

---
URL: https://psxcorrelationmatrix-7pijj7zbriv6z8aebwgede.streamlit.app/
## 🔍 What Is It?

- A heatmap displaying **pairwise Pearson correlations** between stocks.
- Values range from **-1 (perfect inverse)** to **+1 (perfect correlation)**.
- Computed using **z-score normalized closing prices**.
- Data is preprocessed and stored in **SQLite** to avoid recomputation.

---

## 🏦 Dataset

- Stocks from the **KSE-100 index** (2014–2024)
- Source: Historical CSV files per symbol (not included for licensing reasons)
- Cleaned for duplicates and missing values

---

## 🛠 Technologies Used

- Python (pandas, numpy, plotly)
- Streamlit for interactive frontend
- SQLite for lightweight persistent storage

---

## 🧠 Use Cases

This tool is useful for:

- 📈 **Portfolio diversification** — Identify uncorrelated or negatively correlated stocks.
- 📊 **Market structure analysis** — Understand which sectors or companies move together.
- 🧪 **Quantitative research** — Use as a base for factor modeling or PCA.
- 🧠 **Educational purposes** — Great for teaching how correlation works in finance.
- 🧮 **Input for risk models** — e.g., use in building covariance matrices.

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/psx-heatmap.git
cd psx-heatmap
streamlit run correlation_matrix.py
