import subprocess, sys

files = [
    "environment_info.py",
    "run_all.py",
    "bagian_b/b1_hybrid_pipeline/generate_dataset.py",
    "bagian_b/b1_hybrid_pipeline/benchmark_b1.py",
    "bagian_b/b1_hybrid_pipeline/plot_b1.py",
    "bagian_b/b2_mpi_processpool/mpi_processpool_original.py",
    "bagian_b/b2_mpi_processpool/mpi_processpool_fixed.py",
    "bagian_b/b2_mpi_processpool/benchmark_b2.py",
    "bagian_b/b2_mpi_processpool/plot_b2.py",
    "bagian_b/b3_word_count/generate_dataset.py",
    "bagian_b/b3_word_count/benchmark_b3.py",
    "bagian_b/b3_word_count/plot_b3.py",
]

all_ok = True
for f in files:
    result = subprocess.run([sys.executable, "-m", "py_compile", f], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"[OK]   {f}")
    else:
        print(f"[FAIL] {f}")
        print(f"       {result.stderr.strip()}")
        all_ok = False

print()
if all_ok:
    print("Semua file Python: SYNTAX OK")
else:
    print("Ada file yang perlu diperbaiki!")
