# Tugas 4 - Hybrid Computing

## Identitas
- **Nama:** Yusep Muhamad N
- **NPM:** 247006111186
- **Kelas:** G
- **Parameter A:** 6

## Environment
- **OS:** Windows 11
- **CPU:** Intel Core i7 (Contoh, silakan cek output script)
- **RAM:** 4GB
- **Python:** 3.x
- **MPI:** mpi4py tersedia (Microsoft MPI)

## Struktur Project
- `bagian_a/`: Berisi draft/jawaban teori.
- `bagian_b/`:
  - `b1_hybrid_pipeline/`: Script eksperimen pipeline, generate dataset, benchmark, dan plot.
  - `b2_mpi_processpool/`: Script MPI dengan process pool original (sengaja error) dan fixed, beserta benchmark.
  - `b3_word_count/`: Global word count dan komparasi multithreading vs multiprocessing.
- `results/`: Output CSV dan grafik plot matplotlib.
- `report/`: Outline laporan lengkap.
- `run_all.py`: Master script interaktif.

## Bagian A
Mencakup jawaban teoretis seputar Amdahl's Law, limitasi Shared/Distributed memory, perbedaan kegunaan ProcessPool dan ThreadPool, dan contoh deadlock.

## Bagian B1 (Hybrid Pipeline)
- **Cara Menjalankan:** `python run_all.py` lalu pilih opsi 4.
- **Parameter:** Loaders=[1,2,4], Workers=[1,2,4,max], Q_MAX=[4,32]
- **Hasil:** CSV dan PNG akan disimpan di folder `results`. Dapat dilihat bahwa Thread cocok untuk loader dan Worker untuk komputasi. Backpressure Q_MAX mencegah antrian terlalu besar.

## Bagian B2 (Strong Scaling MPI + ProcessPool)
- **Cara Menjalankan:** `python run_all.py` lalu pilih opsi 7.
- **Bug Original:** Terjadi eksekusi inisialisasi MPI berulang di child proses yang dibentuk ProcessPoolExecutor karena tidak diamankan dari import mpi4py di global scope.
- **Perbaikan:** Memindahkan `import mpi4py` dan inisialisasi ke dalam block `if __name__ == '__main__':`
- **Oversubscription:** Terjadi saat jumlah worker x rank lebih dari total physical cores, menyebabkan performa menurun karena context switching.

## Bagian B3 (Global Word Count)
- **Dataset:** 30 file text random words.
- **Perbandingan:** ProcessPool umumnya lebih unggul dari ThreadPool pada operasi reguler (regex dan stopwords) yang CPU bound.

## Bagian C
Arsitektur untuk Deteksi Fraud E-Wallet Real-Time. Menggunakan Thread untuk koneksi IO dan ProcessPool/MPI untuk evaluasi model deteksi fraud berskala besar di backend.

## Cara Menjalankan
1. Pastikan dependencies diinstall: `pip install -r requirements.txt` (serta `seaborn`).
2. Jalankan master script interaktif:
   ```bash
   python run_all.py
   ```
3. Ikuti menu interaktif yang tersedia untuk menjalankan tiap bagian eksperimen.
