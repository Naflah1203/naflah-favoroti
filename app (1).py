import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Pilot Project – Cabang Favoroti Sudirman")
st.write("Alamat: Jl. Jenderal Sudirman No.22")

# DATA
data_harian = pd.DataFrame({
    "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"],
    "Penjualan": [420000, 380000, 450000, 500000, 620000, 710000, 680000]
})

data_produk = pd.DataFrame({
    "Produk": ["Roti Cokelat", "Roti Keju", "Roti Tawar"],
    "Jumlah": [320, 260, 180]
})

# GRAFIK GARIS
st.subheader("Penjualan Harian")
st.line_chart(data_harian.set_index("Hari"))

# GRAFIK BATANG
st.subheader("Penjualan Berdasarkan Produk")
st.bar_chart(data_produk.set_index("Produk"))

# INSIGHT
st.subheader("Insight & Keputusan")
st.write("""
- Penjualan tertinggi terjadi di akhir pekan  
- Roti cokelat merupakan produk terlaris  
- Promo sore hari diterapkan pada hari kerja  
""")
