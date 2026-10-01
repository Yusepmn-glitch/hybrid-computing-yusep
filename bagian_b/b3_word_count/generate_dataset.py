# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# ==========================================

import os
import random
from pathlib import Path

def generate_text_dataset(num_files=30):
    base_dir = Path(__file__).resolve().parent
    output_dir = base_dir / 'dataset'
    os.makedirs(output_dir, exist_ok=True)
    words = ["teknologi", "komputer", "paralel", "distribusi", "hybrid",
             "dan", "yang", "di", "the", "of", "and", "data", "sistem", "jaringan", "cepat"]
    
    print(f"Generating {num_files} files in {output_dir}...")
    for i in range(num_files):
        filename = output_dir / f"article_{i}.txt"
        # Generate random text
        content = " ".join(random.choices(words, k=5000))
        with open(filename, 'w') as f:
            f.write(content)
            
    print("B3 Dataset generation complete.")

if __name__ == "__main__":
    generate_text_dataset()
