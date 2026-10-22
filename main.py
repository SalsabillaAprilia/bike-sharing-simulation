"""
Simulasi Monte Carlo Permintaan Penyewaan Sepeda per Jam
Dataset: UCI Bike Sharing Dataset (hour.csv)

Cara kerja:
1. Membaca data historis.
2. Menghitung rata-rata permintaan untuk setiap jam (0-23).
3. Membuat simulasi 30 hari dengan mengambil sampel historis per jam.
4. Mengulang simulasi 1.000 kali dan merangkum ketidakpastian total permintaan.
"""

from pathlib import Path
import json
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "raw" / "hour.csv"
RESULTS_DIR = BASE_DIR / "results"

JUMLAH_HARI = 30
JUMLAH_SIMULASI = 1000
RANDOM_SEED = 42


def baca_data():
    """Membaca dan memvalidasi file hour.csv."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            "File data belum ditemukan.\n"
            "Unduh Bike Sharing Dataset dari UCI, ekstrak ZIP, lalu letakkan "
            "hour.csv di folder data/raw/hour.csv."
        )

    data = pd.read_csv(DATA_PATH)
    data.columns = [kolom.strip() for kolom in data.columns]

    kolom_wajib = {"hr", "cnt"}
    if not kolom_wajib.issubset(data.columns):
        raise ValueError(
            f"Kolom wajib {kolom_wajib} tidak ditemukan. "
            f"Kolom yang tersedia: {list(data.columns)}"
        )

    data = data.dropna(subset=["hr", "cnt"]).copy()
    data["hr"] = pd.to_numeric(data["hr"], errors="coerce")
    data["cnt"] = pd.to_numeric(data["cnt"], errors="coerce")
    data = data.dropna(subset=["hr", "cnt"])
    data["hr"] = data["hr"].astype(int)
    data["cnt"] = data["cnt"].astype(int)
    data = data[data["hr"].between(0, 23)]

    if data.empty:
        raise ValueError("Data kosong setelah pemeriksaan.")

    jam_tersedia = set(data["hr"].unique())
    jam_wajib = set(range(24))
    if jam_tersedia != jam_wajib:
        raise ValueError(
            "Data harus memiliki catatan untuk seluruh jam 0 sampai 23. "
            f"Jam yang ditemukan: {sorted(jam_tersedia)}"
        )

    return data


def buat_ringkasan_per_jam(data):
    """Menghitung statistik permintaan untuk setiap jam."""
    ringkasan = (
        data.groupby("hr")["cnt"]
        .agg(jumlah_data="count", rata_rata="mean", median="median", simpangan_baku="std")
        .reset_index()
        .sort_values("hr")
    )
    ringkasan.to_csv(RESULTS_DIR / "ringkasan_per_jam.csv", index=False)

    plt.figure(figsize=(10, 5))
    plt.plot(ringkasan["hr"], ringkasan["rata_rata"], marker="o")
    plt.title("Rata-rata Penyewaan Sepeda berdasarkan Jam")
    plt.xlabel("Jam dalam sehari")
    plt.ylabel("Rata-rata jumlah penyewaan")
    plt.xticks(range(0, 24))
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "rata_rata_per_jam.png", dpi=160)
    plt.close()

    return ringkasan


def simulasikan_total_bulanan(data, jumlah_hari, jumlah_simulasi, seed):
    """
    Monte Carlo berbasis bootstrap empiris.
    Untuk setiap jam, sampel jumlah penyewaan historis pada jam yang sama,
    dengan pengembalian (replacement), sebanyak jumlah_hari kali.
    """
    rng = np.random.default_rng(seed)
    data_per_jam = {
        int(jam): kelompok["cnt"].to_numpy()
        for jam, kelompok in data.groupby("hr")
    }

    total_simulasi = []

    for nomor in range(1, jumlah_simulasi + 1):
        total = 0
        for jam in range(24):
            sampel = rng.choice(
                data_per_jam[jam],
                size=jumlah_hari,
                replace=True
            )
            total += int(sampel.sum())
        total_simulasi.append(total)

    return np.asarray(total_simulasi, dtype=int)


def simpan_hasil(total_simulasi, jumlah_hari):
    """Menyimpan hasil simulasi dan grafik distribusinya."""
    tabel = pd.DataFrame({
        "simulasi_ke": np.arange(1, len(total_simulasi) + 1),
        "total_permintaan_30_hari": total_simulasi
    })
    tabel.to_csv(RESULTS_DIR / "hasil_simulasi.csv", index=False)

    ringkasan = {
        "jumlah_simulasi": int(len(total_simulasi)),
        "jumlah_hari_per_simulasi": int(jumlah_hari),
        "rata_rata_total": float(np.mean(total_simulasi)),
        "median_total": float(np.median(total_simulasi)),
        "persentil_5": float(np.percentile(total_simulasi, 5)),
        "persentil_95": float(np.percentile(total_simulasi, 95)),
        "simpangan_baku_total": float(np.std(total_simulasi, ddof=1)),
        "random_seed": RANDOM_SEED,
    }

    with open(RESULTS_DIR / "ringkasan_simulasi.json", "w", encoding="utf-8") as file:
        json.dump(ringkasan, file, indent=2, ensure_ascii=False)

    plt.figure(figsize=(10, 5))
    plt.hist(total_simulasi, bins=30, edgecolor="black")
    plt.title(f"Distribusi Total Permintaan pada Simulasi {jumlah_hari} Hari")
    plt.xlabel("Total penyewaan selama periode simulasi")
    plt.ylabel("Frekuensi hasil simulasi")
    plt.grid(axis="y", alpha=0.25)
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "distribusi_total_simulasi.png", dpi=160)
    plt.close()

    return ringkasan


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    try:
        data = baca_data()
    except (FileNotFoundError, ValueError) as error:
        print(f"Kesalahan: {error}")
        sys.exit(1)

    print(f"Jumlah baris data yang digunakan: {len(data):,}")
    print("Membuat ringkasan permintaan per jam...")
    buat_ringkasan_per_jam(data)

    print(f"Menjalankan {JUMLAH_SIMULASI} simulasi untuk periode {JUMLAH_HARI} hari...")
    total_simulasi = simulasikan_total_bulanan(
        data, JUMLAH_HARI, JUMLAH_SIMULASI, RANDOM_SEED
    )
    ringkasan = simpan_hasil(total_simulasi, JUMLAH_HARI)

    print("\n=== RINGKASAN HASIL SIMULASI ===")
    for nama, nilai in ringkasan.items():
        if isinstance(nilai, float):
            print(f"{nama}: {nilai:,.2f}")
        else:
            print(f"{nama}: {nilai}")
    print(f"\nHasil tersimpan di folder: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
