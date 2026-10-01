# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_b3_results():
    if not os.path.exists('../../results_b3.csv'):
        print("results_b3.csv not found")
        return
        
    df = pd.read_csv('../../results_b3.csv')
    
    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='Executor', y='Time_Seconds', palette='viridis')
    plt.title('B3: Execution Time (Threads vs Processes)')
    plt.ylabel('Time (seconds)')
    plt.savefig('../../results/graphs/b3_threads_vs_processes.png')
    plt.close()
    
    print("Grafik B3 berhasil di-generate!")

if __name__ == '__main__':
    plot_b3_results()
