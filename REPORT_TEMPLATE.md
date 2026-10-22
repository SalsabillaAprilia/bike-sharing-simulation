# Report: Simulasi Monte Carlo Permintaan Penyewaan Sepeda

## 1. Pendahuluan

Layanan penyewaan sepeda perlu memahami perubahan permintaan dari waktu ke waktu. Permintaan dapat berbeda pada setiap jam, sehingga satu nilai rata-rata saja tidak cukup untuk menggambarkan ketidakpastian. Proyek ini menggunakan data historis untuk membuat model sederhana dan menjalankan simulasi berulang guna mengamati variasi total penyewaan selama 30 hari.

## 2. Tujuan

1. Mendeskripsikan rata-rata permintaan penyewaan berdasarkan jam.
2. Membangun simulasi Monte Carlo sederhana menggunakan pengambilan sampel dari data historis.
3. Mengamati variasi total permintaan pada 1.000 simulasi periode 30 hari.

## 3. Sumber data

Data bersumber dari UCI Machine Learning Repository, *Bike Sharing Dataset*, oleh Hadi Fanaee-T (2013). Dataset berisi catatan penyewaan sepeda per jam dan informasi pendukung untuk Capital Bikeshare pada 2011–2012. File yang digunakan adalah `hour.csv`, dengan kolom `hr` sebagai jam dan `cnt` sebagai jumlah penyewaan.

Sumber: https://archive.ics.uci.edu/dataset/275/bike%2Bsharing%2Bdataset  
DOI: https://doi.org/10.24432/C5W894

## 4. Metode pemodelan dan simulasi

Bahasa yang digunakan adalah Python dengan pustaka pandas, NumPy, dan Matplotlib. Pertama, data dibaca dan diperiksa agar kolom jam dan jumlah penyewaan tersedia. Kedua, rata-rata penyewaan dihitung untuk setiap jam. Ketiga, program melakukan simulasi 30 hari dengan mengambil sampel acak dari nilai historis pada jam yang sama. Setiap sampel dijumlahkan untuk memperoleh total penyewaan dalam satu periode simulasi. Proses ini diulang sebanyak 1.000 kali.

Metode pengambilan sampel dengan pengembalian ini disebut *empirical bootstrap*. Seed acak ditetapkan sebesar 42 agar hasil dapat direproduksi.

## 5. Hasil dan pembahasan

### 5.1 Pola permintaan per jam

![Rata-rata Penyewaan per Jam](results/rata_rata_per_jam.png)

**Temuan utama dari grafik:**  
Berdasarkan file ringkasan_per_jam.csv, permintaan penyewaan tertinggi terjadi pada jam pulang kantor yaitu pukul 17:00 (rata-rata 461,45 penyewaan) dan pukul 18:00 (rata-rata 425,51 penyewaan), serta jam berangkat kerja pada pukul 08:00 (rata-rata 359,01 penyewaan). Sebaliknya, permintaan paling rendah terjadi pada dini hari, dengan titik terendah pada pukul 04:00 (rata-rata 6,35 penyewaan).

### 5.2 Hasil simulasi

Berdasarkan `results/ringkasan_simulasi.json`, isi tabel berikut.

| Indikator | Hasil |
|---|---:|
| Jumlah simulasi | 1.000 |
| Lama setiap simulasi | 30 hari |
| Rata-rata total permintaan | 135.815,20 |
| Median total permintaan | 135.653,50 |
| Persentil ke-5 | 130.630,50 |
| Persentil ke-95 | 141.332,00 |
| Simpangan baku | 3.365,40 |

![Distribusi Total Simulasi](results/distribusi_total_simulasi.png)

**Interpretasi:**  
Distribusi hasil simulasi 1.000 kali berpusat di sekitar rata-rata 135.815 sepeda dengan bentuk kurva menyerupai lonceng (distribusi normal). Sekitar 90% hasil simulasi berada pada rentang tengah antara 130.630 (persentil ke-5) hingga 141.332 (persentil ke-95). Nilai simpangan baku sebesar 3.365 mencerminkan rentang variasi ketidakpastian yang wajar terjadi jika pola penyewaan historis per jam berulang selama periode 30 hari.

## 6. Keterbatasan

Model mengambil sampel berdasarkan jam dan tidak mempertahankan hubungan antarjam dalam satu hari. Model juga tidak mengondisikan sampel pada hari kerja, libur, musim, atau cuaca. Data historis berasal dari Capital Bikeshare pada 2011–2012, sehingga hasilnya tidak otomatis berlaku untuk lokasi atau periode saat ini. Oleh karena itu, model lebih tepat dipandang sebagai demonstrasi simulasi daripada prediksi operasional.

## 7. Kesimpulan

Simulasi Monte Carlo dengan metode empirical bootstrap berhasil memodelkan ketidakpastian permintaan penyewaan sepeda selama 30 hari dengan rata-rata total permintaan 135.815 sepeda dan rentang 90% tengah di kisaran 130.630–141.332 unit. Permintaan sangat dipengaruhi oleh waktu dalam sehari, dengan lonjakan tajam pada jam sibuk (08:00 dan 17:00–18:00). Keterbatasan model ini adalah belum memperhitungkan interaksi faktor cuaca, musim, dan hari libur secara bersamaan.

## Daftar pustaka

Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894
