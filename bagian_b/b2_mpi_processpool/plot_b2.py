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

def plot_b2_results():
    if not os.path.exists('../../results_b2.csv'):
        print("results_b2.csv not found")
        return
        
    df = pd.read_csv('../../results_b2.csv')
    
    # Plot 1: Makespan vs Number of Workers (Grouped by Ranks)
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='max_workers', y='makespan', hue='mpi_ranks')
    plt.title('B2: Makespan vs Workers (Grouped by MPI Ranks)')
    plt.xlabel('Number of Max Workers per Rank')
    plt.ylabel('Makespan (seconds)')
    plt.savefig('../../results/graphs/b2_makespan.png')
    plt.close()
    
    # Plot 2: Speedup vs Total Workers
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x='total_workers', y='speedup', marker='o')
    plt.title('B2: Speedup vs Total Workers')
    plt.xlabel('Total Workers (Ranks x Max Workers)')
    plt.ylabel('Speedup')
    plt.grid(True)
    plt.savefig('../../results/graphs/b2_speedup.png')
    plt.close()

    # Plot 3: Efficiency vs Total Workers
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x='total_workers', y='efficiency', marker='o', color='orange')
    plt.title('B2: Efficiency vs Total Workers')
    plt.xlabel('Total Workers (Ranks x Max Workers)')
    plt.ylabel('Efficiency')
    plt.grid(True)
    plt.savefig('../../results/graphs/b2_efficiency.png')
    plt.close()
    
    print("Grafik B2 berhasil di-generate dan disimpan ke results/graphs/")
    
if __name__ == '__main__':
    plot_b2_results()
