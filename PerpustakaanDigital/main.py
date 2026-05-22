# ================================
# SISTEM PERPUSTAKAAN DIGITAL
# main.py
# ================================

from utils import tambah_buku, tampil_buku, cari_buku, sorting_buku, pinjam_buku, kembalikan_buku, undo_peminjaman

# ================================
# MENU
# ================================

while True:
    print("""
=================================
 SISTEM PERPUSTAKAAN DIGITAL
=================================

1. Tambah Buku
2. Tampilkan Buku
3. Cari Buku
4. Sorting Buku
5. Pinjam Buku
6. Kembalikan Buku
7. Undo Peminjaman
8. Exit
=================================""")

    pilihan = input("Masukkan pilihan : ")

    if pilihan == "1":
        tambah_buku()

    elif pilihan == "2":
        tampil_buku()

    elif pilihan == "3":
        cari_buku()

    elif pilihan == "4":
        sorting_buku()

    elif pilihan == "5":
        pinjam_buku()

    elif pilihan == "6":
        kembalikan_buku()

    elif pilihan == "7":
        undo_peminjaman()

    elif pilihan == "8":
        print("\nProgram selesai.")
        break

    else:
        print("\nPilihan tidak valid.")