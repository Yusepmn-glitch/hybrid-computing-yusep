# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# Dikerjakan secara individu.
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_results():
    if not os.path.exists('../../results_b1.csv'):
        print("results_b1.csv not found")
        return
        
    df = pd.read_csv('../../results_b1.csv')
    
    # Plot 1: Throughput vs Workers
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='workers', y='throughput', hue='loader_threads')
    plt.title('Throughput vs Number of Workers (Grouped by Loader Threads)')
    plt.xlabel('Number of Workers')
    plt.ylabel('Throughput (files/second)')
    plt.savefig('../../results/graphs/b1_throughput.png')
    plt.close()
    
    # Plot 2: Q_MAX comparison
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='q_max', y='throughput', hue='workers')
    plt.title('Impact of Backpressure (Q_MAX) on Throughput')
    plt.xlabel('Q_MAX Size')
    plt.ylabel('Throughput (files/second)')
    plt.savefig('../../results/graphs/b1_backpressure.png')
    plt.close()
    
if __name__ == '__main__':
    plot_results()
