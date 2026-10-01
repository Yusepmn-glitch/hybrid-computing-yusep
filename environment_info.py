# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# Dikerjakan secara individu.
# ==========================================
import platform
import psutil
import sys
import subprocess

def get_pip_version():
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
        return result.stdout.strip().split()[1] if result.returncode == 0 else "Unknown"
    except Exception:
        return "Not installed/accessible"

def get_mpi_version():
    try:
        import mpi4py
        from mpi4py import MPI
        vendor = MPI.get_vendor()
        return f"mpi4py {mpi4py.__version__} ({vendor[0]} {vendor[1]})"
    except ImportError:
        return "mpi4py is not installed"
    except Exception as e:
        return f"Error detecting MPI: {e}"

def main():
    print("=" * 50)
    print("ENVIRONMENT INFO")
    print("=" * 50)
    print(f"OS: {platform.system()} {platform.release()} ({platform.version()})")
    print(f"CPU: {platform.processor()}")
    print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    print(f"Logical Cores / Threads: {psutil.cpu_count(logical=True)}")
    ram = psutil.virtual_memory().total / (1024 ** 3)
    print(f"RAM: {ram:.2f} GB")
    print("-" * 50)
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"pip Version: {get_pip_version()}")
    print(f"MPI Info: {get_mpi_version()}")
    print("=" * 50)

if __name__ == "__main__":
    main()
