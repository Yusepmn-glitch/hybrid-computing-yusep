# ==========================================
# Tugas 4 - Hybrid Computing
# Nama: Yusep Muhamad N
# NPM: 247006111186
# Kelas: G
# Script: Download 30 buku teks nyata dari Project Gutenberg
# ==========================================

import requests
import os
import time
from pathlib import Path

# 30 buku domain publik dari Project Gutenberg (ID buku)
# Format URL: https://www.gutenberg.org/cache/epub/{ID}/pg{ID}.txt
BOOKS = [
    (1342, "pride_and_prejudice"),
    (84,   "frankenstein"),
    (2701, "moby_dick"),
    (1661, "sherlock_holmes"),
    (98,   "tale_of_two_cities"),
    (1952, "yellow_wallpaper"),
    (174,  "picture_of_dorian_gray"),
    (345,  "dracula"),
    (768,  "wuthering_heights"),
    (2591, "grimms_fairy_tales"),
    (11,   "alice_in_wonderland"),
    (74,   "tom_sawyer"),
    (76,   "huckleberry_finn"),
    (16,   "peter_pan"),
    (1080, "modest_proposal"),
    (46,   "christmas_carol"),
    (2554, "crime_and_punishment"),
    (2600, "war_and_peace"),
    (1400, "great_expectations"),
    (4300, "ulysses"),
    (1232, "the_prince"),
    (2542, "beyond_good_and_evil"),
    (5200, "metamorphosis"),
    (1184, "count_of_monte_cristo"),
    (2852, "the_island_of_doctor_moreau"),
    (36,   "war_of_the_worlds"),
    (103,  "time_machine"),
    (1260, "jane_eyre"),
    (244,  "scarlet_letter"),
    (2489, "call_of_the_wild"),
]

def download_book(book_id, name, output_dir):
    """Download satu buku dari Project Gutenberg."""
    url = f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
    filepath = output_dir / f"{name}.txt"

    if filepath.exists():
        print(f"  [SKIP] {name}.txt sudah ada")
        return True

    try:
        print(f"  [DL]   Downloading: {name} (ID: {book_id})...")
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            with open(filepath, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(response.text)
            size_kb = filepath.stat().st_size // 1024
            print(f"  [OK]   {name}.txt ({size_kb} KB)")
            return True
        else:
            print(f"  [ERR]  {name} - HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"  [ERR]  {name} - {e}")
        return False

def main():
    base_dir = Path(__file__).resolve().parent
    output_dir = base_dir / "bagian_b" / "b3_word_count" / "dataset"
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 55)
    print("Download 30 Buku Teks Nyata - Project Gutenberg")
    print(f"Output folder: {output_dir}")
    print("=" * 55)

    success = 0
    for book_id, name in BOOKS:
        ok = download_book(book_id, name, output_dir)
        if ok:
            success += 1
        time.sleep(0.5)  # jeda agar tidak diblokir server

    print()
    print("=" * 55)
    print(f"Selesai: {success}/{len(BOOKS)} buku berhasil didownload")
    print(f"Folder: {output_dir}")
    print("=" * 55)

if __name__ == "__main__":
    main()
