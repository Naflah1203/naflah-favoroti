import {
  LineChart, Line, BarChart, Bar,
  XAxis, YAxis, Tooltip, ResponsiveContainer
} from "recharts";

const dataHarian = [
  { hari: "Senin", penjualan: 420000 },
  { hari: "Selasa", penjualan: 380000 },
  { hari: "Rabu", penjualan: 450000 },
  { hari: "Kamis", penjualan: 500000 },
  { hari: "Jumat", penjualan: 620000 },
  { hari: "Sabtu", penjualan: 710000 },
  { hari: "Minggu", penjualan: 680000 },
];

const dataProduk = [
  { produk: "Roti Cokelat", jumlah: 320 },
  { produk: "Roti Keju", jumlah: 260 },
  { produk: "Roti Tawar", jumlah: 180 },
];

export default function DashboardCabang() {
  return (
    <div style={{ padding: 20 }}>
      <h2>Dashboard Pilot Project_Cabang Favoroti Sudirman</h2>

      <p><b>Alamat:</b> Jl. Jenderal Sudirman No.22</p>

      <h3>Penjualan Harian</h3>
      <div style={{ height: 300 }}>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={dataHarian}>
            <XAxis dataKey="hari" />
            <YAxis />
            <Tooltip />
            <Line dataKey="penjualan" />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <h3>Penjualan Berdasarkan Produk</h3>
      <div style={{ height: 300 }}>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={dataProduk}>
            <XAxis dataKey="produk" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="jumlah" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <h3>Insight & Keputusan</h3>
      <ul>
        <li>Penjualan tertinggi terjadi di akhir pekan</li>
        <li>Roti cokelat merupakan produk terlaris</li>
        <li>Promo sore hari diterapkan pada hari kerja</li>
      </ul>
    </div>
  );
}

