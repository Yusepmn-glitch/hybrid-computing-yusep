# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# Dikerjakan secara individu.
# ==========================================
import os
import sys

def main():
    print("="*50)
    print("Tugas 4 - Hybrid Computing")
    print("Oleh: Yusep Muhamad N (247006111186)")
    print("Kelas: G")
    print("="*50)
    print("1. Environment check")
    print("2. Amdahl calculation (Drafted in Laporan)")
    print("3. Generate B1 dataset")
    print("4. Run B1 benchmark")
    print("5. Generate B3 dataset")
    print("6. Run B3 benchmark")
    print("7. Run B2 benchmark")
    print("8. Generate all graphs")
    print("9. Run everything")
    print("0. Exit")
    print("="*50)
    
    # As requested by the user, we should not run heavy benchmarks blindly.
    choice = input("Pilih menu (0-9): ")
    
    if choice == '1':
        os.system("python environment_info.py")
    elif choice == '3':
        os.system("python bagian_b/b1_hybrid_pipeline/generate_dataset.py")
    elif choice == '4':
        os.chdir("bagian_b/b1_hybrid_pipeline")
        os.system("python benchmark_b1.py")
    elif choice == '5':
        os.system("python bagian_b/b3_word_count/generate_dataset.py")
    elif choice == '6':
        print("Menjalankan Benchmark B3 (Threads vs Processes)...")
        os.chdir("bagian_b/b3_word_count")
        os.system("mpiexec -n 2 python benchmark_b3.py")
    elif choice == '7':
        print("Menjalankan Benchmark B2...")
        os.chdir("bagian_b/b2_mpi_processpool")
        os.system("python benchmark_b2.py")
    elif choice == '8':
        os.chdir("bagian_b/b1_hybrid_pipeline")
        os.system("python plot_b1.py")
        os.chdir("../../bagian_b/b2_mpi_processpool")
        os.system("python plot_b2.py")
        os.chdir("../../bagian_b/b3_word_count")
        os.system("python plot_b3.py")
        print("Semua grafik (B1, B2, B3) telah dibuat di results/graphs/")
    elif choice == '9':
        print("Menjalankan semuanya...")
        os.system("python environment_info.py")
        os.system("python bagian_b/b1_hybrid_pipeline/generate_dataset.py")
        os.system("python bagian_b/b3_word_count/generate_dataset.py")
        
        os.chdir("bagian_b/b1_hybrid_pipeline")
        os.system("python benchmark_b1.py")
        
        os.chdir("../../bagian_b/b2_mpi_processpool")
        os.system("python benchmark_b2.py")
        
        os.chdir("../../bagian_b/b3_word_count")
        os.system("mpiexec -n 2 python benchmark_b3.py")
        
        os.chdir("../../bagian_b/b1_hybrid_pipeline")
        os.system("python plot_b1.py")
        os.chdir("../../bagian_b/b2_mpi_processpool")
        os.system("python plot_b2.py")
        os.chdir("../../bagian_b/b3_word_count")
        os.system("python plot_b3.py")
    elif choice == '0':
        sys.exit(0)
    else:
        print("Pilihan belum diimplementasikan atau tidak valid.")

if __name__ == '__main__':
    main()
