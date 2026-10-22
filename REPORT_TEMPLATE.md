# Report: Simulasi Monte Carlo Permintaan Penyewaan Sepeda

> **Penting:** Lengkapi bagian hasil setelah mengunduh dataset, menjalankan program, dan memeriksa output. Jangan mengisi angka berdasarkan perkiraan.

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

Masukkan gambar `results/rata_rata_per_jam.png`.

**Temuan utama dari grafik:**  
[Tulis jam dengan rata-rata tertinggi dan terendah berdasarkan `results/ringkasan_per_jam.csv`. Jangan menebak; baca nilai pada file hasil.]

### 5.2 Hasil simulasi

Berdasarkan `results/ringkasan_simulasi.json`, isi tabel berikut.

| Indikator | Hasil |
|---|---:|
| Jumlah simulasi | 1.000 |
| Lama setiap simulasi | 30 hari |
| Rata-rata total permintaan | [isi hasil program] |
| Median total permintaan | [isi hasil program] |
| Persentil ke-5 | [isi hasil program] |
| Persentil ke-95 | [isi hasil program] |
| Simpangan baku | [isi hasil program] |

Masukkan gambar `results/distribusi_total_simulasi.png`.

**Interpretasi:**  
[Jelaskan pusat distribusi dan rentang variasi. Terangkan bahwa persentil ke-5 hingga ke-95 menunjukkan rentang tengah sekitar 90% hasil simulasi, bukan jaminan hasil di masa depan.]

## 6. Keterbatasan

Model mengambil sampel berdasarkan jam dan tidak mempertahankan hubungan antarjam dalam satu hari. Model juga tidak mengondisikan sampel pada hari kerja, libur, musim, atau cuaca. Data historis berasal dari Capital Bikeshare pada 2011–2012, sehingga hasilnya tidak otomatis berlaku untuk lokasi atau periode saat ini. Oleh karena itu, model lebih tepat dipandang sebagai demonstrasi simulasi daripada prediksi operasional.

## 7. Kesimpulan

[Tulis 2–4 kalimat berdasarkan output yang benar-benar dihasilkan. Ringkas pola per jam, variasi total simulasi, dan satu keterbatasan utama.]

## Daftar pustaka

Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894
