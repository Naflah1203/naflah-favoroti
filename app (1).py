import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Favoroti", layout="wide")

# =============================
# DATA (setara dengan React)
# =============================
data_harian = pd.DataFrame({
    "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"],
    "Penjualan": [420000, 380000, 450000, 500000, 620000, 710000, 680000]
})

data_produk = pd.DataFrame({
    "Produk": ["Roti Cokelat", "Roti Keju", "Roti Tawar"],
    "Jumlah": [320, 260, 180]
})

# =============================
# TAMPILAN DASHBOARD
# =============================
st.title("Dashboard Pilot Project – Cabang Favoroti Sudirman")
st.markdown("**Alamat:** Jl. Jenderal Sudirman No.22")

# =============================
# GRAFIK PENJUALAN HARIAN
# =============================
st.subheader("Penjualan Harian")

fig1, ax1 = plt.subplots()
ax1.plot(data_harian["Hari"], data_harian["Penjualan"])
ax1.set_xlabel("Hari")
ax1.set_ylabel("Penjualan (Rp)")
st.pyplot(fig1)

# =============================
# GRAFIK PRODUK TERLARIS
# =============================
st.subheader("Penjualan Berdasarkan Produk")

fig2, ax2 = plt.subplots()
ax2.bar(data_produk["Produk"], data_produk["Jumlah"])
ax2.set_ylabel("Jumlah Terjual")
st.pyplot(fig2)

# =============================
# INSIGHT
# =============================
st.subheader("Insight & Keputusan")
st.markdown("""
- Penjualan tertinggi terjadi di akhir pekan  
- Roti cokelat merupakan produk terlaris  
- Promo sore hari diterapkan pada hari kerja  
""")
