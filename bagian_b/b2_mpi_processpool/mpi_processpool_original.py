# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# ==========================================
# VERSI ORIGINAL (BUGGY - untuk demonstrasi error)
# Bug: import mpi4py dan inisialisasi MPI dilakukan di global scope.
# Ketika ProcessPoolExecutor membuat child process di Windows (spawn),
# child process ikut meng-import file ini dari awal,
# sehingga MPI diinisialisasi ulang dan menyebabkan crash.
# ==========================================

from mpi4py import MPI           # <-- posisi import ini yang menyebabkan masalah
from concurrent.futures import ProcessPoolExecutor
import time
import math

def compute_task(x):
    return sum(math.sin(i) for i in range(x))

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    A = 6
    SAMPLES = 200000 + 10000 * A    # = 260.000

    print(f"Rank {rank} starting...")
    start = time.time()

    # BUG: child process yang dibuat oleh ProcessPoolExecutor
    # akan meng-import mpi4py dari global scope di atas,
    # menyebabkan MPI diinisialisasi ulang dan crash.
    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(compute_task, SAMPLES // 10) for _ in range(10)]
        results = [f.result() for f in futures]

    end = time.time()
    print(f"Rank {rank} finished in {end - start:.2f}s")
