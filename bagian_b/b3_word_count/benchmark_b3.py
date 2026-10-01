# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# ==========================================

import os
import time
import re
import csv
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from pathlib import Path

STOPWORDS = {"dan", "yang", "di", "the", "of", "and"}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read().lower()
    
    # Tokenisasi & Regex
    tokens = re.findall(r'\b\w+\b', text)
    
    # Normalisasi & Stopword filtering
    filtered_words = [w for w in tokens if w not in STOPWORDS]
    
    # Local word count
    return Counter(filtered_words)

def run_benchmark(executor_class, files, num_workers):
    start = time.time()
    total_counter = Counter()
    
    with executor_class(max_workers=num_workers) as executor:
        counters = list(executor.map(process_file, files))
        
    for c in counters:
        total_counter.update(c)
        
    return total_counter, time.time() - start

if __name__ == "__main__":
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    base_dir = Path(__file__).resolve().parent
    dataset_dir = base_dir / 'dataset'
    
    if rank == 0:
        print(f"Path dataset B3: {dataset_dir}")
        
    all_files = [str(f) for f in dataset_dir.glob('*.txt')]
    
    if rank == 0:
        print(f"Total file ditemukan sebelum di-split: {len(all_files)}")
    
    # Simple chunking
    chunk_size = len(all_files) // size
    start_idx = rank * chunk_size
    end_idx = start_idx + chunk_size if rank != size - 1 else len(all_files)
    my_files = all_files[start_idx:end_idx]
    
    print(f"Rank {rank} memproses {len(my_files)} file...")
    
    num_workers = 4
    
    # ThreadPool
    count_thread, time_thread = run_benchmark(ThreadPoolExecutor, my_files, num_workers)
    
    # ProcessPool
    count_process, time_process = run_benchmark(ProcessPoolExecutor, my_files, num_workers)
    
    # Global aggregation
    global_thread = comm.gather(count_thread, root=0)
    global_process = comm.gather(count_process, root=0)
    
    if rank == 0:
        final_thread = Counter()
        for c in global_thread: final_thread.update(c)
            
        final_process = Counter()
        for c in global_process: final_process.update(c)
            
        print("=== Top 10 Words ===")
        print(final_thread.most_common(10))
        
        print(f"Waktu ThreadPoolExecutor: {time_thread:.3f}s")
        print(f"Waktu ProcessPoolExecutor: {time_process:.3f}s")
        
        with open('../../results_b3.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Executor', 'Time_Seconds'])
            writer.writerow(['ThreadPoolExecutor', time_thread])
            writer.writerow(['ProcessPoolExecutor', time_process])
        print("Hasil B3 tersimpan di results_b3.csv")
