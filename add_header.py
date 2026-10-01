import glob
import os

header = """# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# Dikerjakan secara individu.
# ==========================================
"""

# Modify all python files
for filepath in glob.glob('**/*.py', recursive=True):
    # skip this script itself
    if os.path.basename(filepath) == 'add_header.py':
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # prepend header if not already there
    if '# Tugas 4 - Hybrid Computing' not in content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(header + content)
            
print("Header added to all python files.")
