from utils import tambah_buku, hapus_buku, tampil_buku, cari_buku, sorting_buku, pinjam_buku, kembalikan_buku, undo_peminjaman

def Admin():
    while True:
        print("""
=================================
 SISTEM PERPUSTAKAAN DIGITAL
=================================

1. Tambah Buku
2. Hapus Buku
3. Tampilkan Buku
4. Cari Buku
5. Sorting Buku
6. Pinjam Buku
7. Kembalikan Buku
8. Undo Peminjaman
9. Exit
=================================""")

        pilihan = input("Masukkan pilihan : ")

        if pilihan == "1":
            tambah_buku()
            
        elif pilihan == "2":
            hapus_buku()

        elif pilihan == "3":
            tampil_buku()

        elif pilihan == "4":
            cari_buku()

        elif pilihan == "5":
            sorting_buku()

        elif pilihan == "6":
            pinjam_buku()

        elif pilihan == "7":
            kembalikan_buku()

        elif pilihan == "8":
            undo_peminjaman()

        elif pilihan == "9":
            print("\nProgram selesai.")
            break

        else:
            print("\nPilihan tidak valid.")
