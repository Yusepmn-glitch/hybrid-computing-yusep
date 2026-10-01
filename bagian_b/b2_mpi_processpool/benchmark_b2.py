# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# ==========================================

import os
import subprocess
import time
import csv

def run_benchmark():
    A = 6
    results = []
    
    ranks_list = [1, 2, 4]
    workers_list = [1, 2, 4]
    
    print("Mulai B2 Benchmark (MPI + ProcessPool)...")
    
    for ranks in ranks_list:
        for workers in workers_list:
            print(f"Menguji ranks={ranks}, workers={workers}...")
            
            # Catat waktu mulai
            start_time = time.time()
            
            # Panggil script melalui subprocess dengan mpiexec
            try:
                cmd = ["mpiexec", "-n", str(ranks), "python", "mpi_processpool_fixed.py", str(workers)]
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                
                # Catat waktu selesai (makespan)
                makespan = time.time() - start_time
                
                total_workers = ranks * workers
                results.append([ranks, workers, total_workers, makespan])
            except subprocess.CalledProcessError as e:
                print(f"Error pada ranks={ranks}, workers={workers}: mpiexec tidak tersedia atau error.")
                print(e.stderr)
                return
            except FileNotFoundError:
                print("Error: mpiexec tidak ditemukan di sistem. Pastikan Microsoft MPI terinstall.")
                return
                
    # Hitung Speedup dan Efficiency
    # T1 adalah makespan dari rank=1, worker=1
    T1 = results[0][3]
    
    final_results = []
    for r in results:
        ranks, workers, total_workers, makespan = r
        speedup = T1 / makespan if makespan > 0 else 0
        # Efficiency dihitung dari Speedup / Total Pekerja aktif
        efficiency = speedup / total_workers if total_workers > 0 else 0
        final_results.append([ranks, workers, total_workers, makespan, speedup, efficiency])
        
    # Simpan ke CSV
    csv_path = '../../results_b2.csv'
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['mpi_ranks', 'max_workers', 'total_workers', 'makespan', 'speedup', 'efficiency'])
        writer.writerows(final_results)
        
    print(f"Benchmark selesai. Hasil disimpan di {csv_path}")

if __name__ == '__main__':
    run_benchmark()
