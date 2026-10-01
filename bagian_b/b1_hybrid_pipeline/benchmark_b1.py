# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# Dikerjakan secara individu.
# ==========================================
import os
import time
import glob
import csv
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from queue import Queue

def process_file(filepath):
    start = time.time()
    with open(filepath, 'r') as f:
        data = f.readlines()
    
    # Simulate CPU intensive work
    total = 0
    for line in data:
        if line.strip():
            total += int(line.strip()) ** 2
    
    # Add a small sleep to simulate longer processing if needed
    time.sleep(0.01)
            
    latency = time.time() - start
    return latency

def hybrid_pipeline(num_loader_threads, num_workers, q_max, dataset_dir):
    files = glob.glob(os.path.join(dataset_dir, '*.txt'))
    if not files:
        print("No files found!")
        return 0, 0, 0
        
    task_queue = Queue(maxsize=q_max)
    result_queue = Queue()
    
    # Loader
    def loader():
        with ThreadPoolExecutor(max_workers=num_loader_threads) as executor:
            for f in files:
                task_queue.put(f) # this blocks if queue is full (backpressure)
        for _ in range(num_workers):
            task_queue.put(None)
            
    loader_thread = threading.Thread(target=loader)
    
    start_time = time.time()
    loader_thread.start()
    
    latencies = []
    
    # Workers
    def worker():
        while True:
            item = task_queue.get()
            if item is None:
                break
            lat = process_file(item)
            result_queue.put(lat)
            
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for _ in range(num_workers):
            executor.submit(worker)
            
    loader_thread.join()
    
    while not result_queue.empty():
        latencies.append(result_queue.get())
        
    total_time = time.time() - start_time
    throughput = len(files) / total_time if total_time > 0 else 0
    avg_latency = sum(latencies) / len(latencies) if latencies else 0
    
    return total_time, throughput, avg_latency

if __name__ == "__main__":
    A = 6
    import multiprocessing
    max_cores = multiprocessing.cpu_count()
    
    loader_threads_list = [1, 2, 4]
    workers_list = [1, 2, 4, max_cores]
    q_max_list = [4, 32]
    
    dataset_dir = 'dataset'
    
    results = []
    
    print("Starting B1 Benchmark...")
    for q_max in q_max_list:
        for loader_threads in loader_threads_list:
            for workers in workers_list:
                print(f"Running: loaders={loader_threads}, workers={workers}, q_max={q_max}")
                t_time, throughput, avg_lat = hybrid_pipeline(loader_threads, workers, q_max, dataset_dir)
                results.append([loader_threads, workers, q_max, t_time, throughput, avg_lat])
                
    with open('../../results_b1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['loader_threads', 'workers', 'q_max', 'total_time', 'throughput', 'avg_latency'])
        writer.writerows(results)
    
    print("Benchmark B1 Complete.")
