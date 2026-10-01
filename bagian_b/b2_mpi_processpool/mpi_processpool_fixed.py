# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# Dikerjakan secara individu.
# ==========================================
import multiprocessing
# PERBAIKAN: Set start method ke 'spawn' sebelum inisialisasi MPI jika memungkinkan.
# Namun di Windows defaultnya sudah 'spawn'. Error biasanya terjadi karena import mpi4py dieksekusi lagi di child process.
# Solusinya adalah memindahkan import mpi4py ke dalam guard __main__ atau function.
import sys
from concurrent.futures import ProcessPoolExecutor
import time
import math

def compute_task(x):
    return sum(math.sin(i) for i in range(x))

if __name__ == '__main__':
    # PERBAIKAN: Import mpi4py hanya di main process untuk menghindari inisialisasi berulang di child processes
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    A = 6
    SAMPLES = 200000 + 10000 * A
    
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    
    print(f"Rank {rank} starting dengan {workers} workers...")
    start = time.time()
    
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(compute_task, SAMPLES//10) for _ in range(10)]
        results = [f.result() for f in futures]
        
    end = time.time()
    print(f"Rank {rank} finished in {end-start:.2f}s")
