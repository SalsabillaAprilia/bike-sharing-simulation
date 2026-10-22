# Simulasi Monte Carlo Permintaan Penyewaan Sepeda

## 1. Deskripsi proyek

Proyek ini menerapkan pemodelan dan simulasi untuk memperkirakan variasi total permintaan penyewaan sepeda selama periode 30 hari berdasarkan pola permintaan historis per jam. Metode yang digunakan adalah **Monte Carlo berbasis empirical bootstrap**: nilai historis untuk setiap jam dipilih secara acak dengan pengembalian, lalu dijumlahkan menjadi satu periode simulasi.

Proyek ini tidak bertujuan memprediksi angka permintaan secara pasti dan tidak membuktikan hubungan sebab-akibat. Hasilnya menunjukkan rentang kemungkinan total permintaan jika pola historis per jam berulang.

## 2. Pertanyaan proyek

- Bagaimana rata-rata jumlah penyewaan berubah dari jam ke jam?
- Berapa perkiraan total penyewaan untuk periode simulasi 30 hari?
- Seberapa lebar variasi hasil total permintaan berdasarkan simulasi berulang?

## 3. Sumber data

**UCI Machine Learning Repository — Bike Sharing Dataset**

- Halaman dataset: https://archive.ics.uci.edu/dataset/275/bike%2Bsharing%2Bdataset
- Pembuat dataset: Hadi Fanaee-T
- Data mencakup catatan penyewaan per jam dan harian untuk Capital Bikeshare pada 2011–2012, beserta informasi waktu, musim, dan cuaca.
- File yang digunakan: `hour.csv`
- Kolom utama: `hr` (jam 0–23) dan `cnt` (jumlah total penyewaan pada jam tersebut).
- Lisensi dataset: CC BY 4.0. Cantumkan atribusi sumber jika membagikan atau mengadaptasi data.

Sitasi:
Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894

## 4. Bahasa dan pustaka

- **Bahasa pemrograman:** Python
- **NumPy:** pengambilan sampel acak dan perhitungan numerik
- **pandas:** membaca CSV dan meringkas data
- **Matplotlib:** membuat grafik

## 5. Model dan asumsi

Misalkan `D(h)` adalah kumpulan nilai penyewaan historis pada jam `h`.

Untuk satu simulasi 30 hari, program mengambil 30 sampel dari kumpulan historis masing-masing jam, dengan pengembalian. Total periode simulasi adalah:

`T = jumlah seluruh sampel untuk jam 0 sampai 23 selama 30 hari`

Proses diulang 1.000 kali dengan seed acak tetap (`42`) agar hasil dapat direproduksi.

Asumsi utama:
1. Pola historis penyewaan pada jam yang sama cukup representatif untuk simulasi.
2. Sampel historis dipilih dengan pengembalian.
3. Hubungan antarjam, hari kerja/libur, musim, dan cuaca tidak dimodelkan secara bersama. Karena itu, hasil adalah model sederhana untuk eksplorasi, bukan prediksi operasional yang pasti.

## 6. Cara menjalankan

1. Unduh dataset dari halaman UCI di atas.
2. Ekstrak berkas ZIP.
3. Salin `hour.csv` ke `data/raw/hour.csv` di dalam proyek ini.
4. Pastikan Python sudah terpasang.
5. Buka terminal di folder proyek, lalu jalankan:

```bash
python -m pip install -r requirements.txt
python main.py
```

## 7. Output

Program menghasilkan:
- `results/ringkasan_per_jam.csv` — jumlah catatan, rata-rata, median, dan simpangan baku per jam.
- `results/rata_rata_per_jam.png` — grafik rata-rata penyewaan berdasarkan jam.
- `results/hasil_simulasi.csv` — total permintaan pada setiap simulasi.
- `results/ringkasan_simulasi.json` — rata-rata, median, persentil ke-5 dan ke-95, serta simpangan baku hasil simulasi.
- `results/distribusi_total_simulasi.png` — histogram hasil simulasi.

## 8. Interpretasi

Gunakan `ringkasan_simulasi.json` untuk melaporkan hasil setelah program dijalankan. Persentil ke-5 dan ke-95 menggambarkan rentang tengah sekitar 90% dari hasil simulasi; angka tersebut bukan jaminan batas minimum/maksimum dan bukan interval prediksi yang tervalidasi.

Jangan menulis hasil angka sebelum menjalankan program menggunakan file data yang benar.

## 9. Struktur repositori

```text
bike-sharing-simulation/
├── data/
│   └── raw/
│       └── hour.csv             # diunduh dari UCI, belum disertakan
├── results/                     # hasil program
├── main.py
├── requirements.txt
├── REPORT_TEMPLATE.md
├── AI_USAGE.md
└── README.md
```

## 10. Catatan keterlibatan AI

Lihat `AI_USAGE.md`. Persentase keterlibatan AI harus dilaporkan berdasarkan definisi dosen dan bukti yang nyata. Jangan mengklaim angka di bawah 20% jika tidak dapat dibuktikan.
