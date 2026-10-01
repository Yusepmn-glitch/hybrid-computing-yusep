# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# Dikerjakan secara individu.
# ==========================================
import os
import random
import time

def generate_dataset(num_files, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    print(f"Generating {num_files} files in {output_dir}...")
    for i in range(num_files):
        filename = os.path.join(output_dir, f"data_{i}.txt")
        # generate random numbers
        lines = [str(random.randint(1, 100)) for _ in range(1000)]
        with open(filename, 'w') as f:
            f.write("\n".join(lines))
    print("Dataset generation complete.")

if __name__ == "__main__":
    A = 6
    num_files = 100 + 10 * A
    generate_dataset(num_files, 'dataset')
