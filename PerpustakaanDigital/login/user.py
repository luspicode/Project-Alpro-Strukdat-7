from utils import tambah_buku, hapus_buku, tampil_buku, cari_buku, sorting_buku, pinjam_buku, kembalikan_buku, undo_peminjaman

def Admin():
    while True:
        print("""
=================================
 SISTEM PERPUSTAKAAN DIGITAL
=================================

1. Tampilkan Buku
2. Cari Buku
3. Pinjam Buku
4. Kembalikan Buku
5. Exit
=================================""")

        pilihan = input("Masukkan pilihan : ")

        if pilihan == "1":
            tampil_buku()

        elif pilihan == "2":
            cari_buku()

        elif pilihan == "3":
            pinjam_buku()

        elif pilihan == "4":
            kembalikan_buku()

        elif pilihan == "5":
            print("\nProgram selesai.")
            break

        else:
            print("\nPilihan tidak valid.")
