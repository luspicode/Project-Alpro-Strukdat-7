# ================================
# SISTEM PERPUSTAKAAN DIGITAL
# main.py
# ================================

from filehandler import load_buku, save_buku
from sorting import bubble_sort_judul
from searching import linear_search
from queue import Queue
from stack import Stack

# ================================
# DATA AWAL
# ================================

daftar_buku = load_buku()

antrian = Queue()
undo_stack = Stack()

# ================================
# FUNCTION TAMPIL BUKU
# ================================

def tampil_buku():
    if len(daftar_buku) == 0:
        print("\nBelum ada buku.")
        return

    print("\n========== DAFTAR BUKU ==========")

    for buku in daftar_buku:
        print(f"""
ID       : {buku['id']}
Judul    : {buku['judul']}
Penulis  : {buku['penulis']}
Tahun    : {buku['tahun']}
Status   : {buku['status']}
----------------------------------
""")


# ================================
# FUNCTION TAMBAH BUKU
# ================================

def tambah_buku():

    id_buku = input("Masukkan ID Buku      : ")
    judul = input("Masukkan Judul Buku   : ")
    penulis = input("Masukkan Penulis Buku : ")
    tahun = input("Masukkan Tahun Buku   : ")

    buku = {
        "id": id_buku,
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "status": "Tersedia"
    }

    daftar_buku.append(buku)

    save_buku(daftar_buku)

    print("\nBuku berhasil ditambahkan!")


# ================================
# FUNCTION CARI BUKU
# ================================

def cari_buku():

    keyword = input("\nMasukkan judul buku : ")

    hasil = linear_search(daftar_buku, keyword)

    if hasil:
        print("\n===== BUKU DITEMUKAN =====")
        print(f"ID       : {hasil['id']}")
        print(f"Judul    : {hasil['judul']}")
        print(f"Penulis  : {hasil['penulis']}")
        print(f"Tahun    : {hasil['tahun']}")
        print(f"Status   : {hasil['status']}")
    else:
        print("\nBuku tidak ditemukan.")


# ================================
# FUNCTION SORTING
# ================================

def sorting_buku():

    bubble_sort_judul(daftar_buku)

    print("\nBuku berhasil diurutkan berdasarkan judul!")


# ================================
# FUNCTION PINJAM BUKU
# ================================

def pinjam_buku():

    id_buku = input("\nMasukkan ID buku yang ingin dipinjam : ")

    for buku in daftar_buku:

        if buku["id"] == id_buku:

            if buku["status"] == "Dipinjam":
                print("\nBuku sedang dipinjam.")
                return

            nama = input("Masukkan nama peminjam : ")

            antrian.enqueue(nama)

            buku["status"] = "Dipinjam"

            undo_stack.push(buku)

            save_buku(daftar_buku)

            print(f"\n{nama} berhasil meminjam buku.")

            return

    print("\nBuku tidak ditemukan.")


# ================================
# FUNCTION PENGEMBALIAN
# ================================

def kembalikan_buku():

    id_buku = input("\nMasukkan ID buku yang dikembalikan : ")

    for buku in daftar_buku:

        if buku["id"] == id_buku:

            if buku["status"] == "Tersedia":
                print("\nBuku belum dipinjam.")
                return

            buku["status"] = "Tersedia"

            save_buku(daftar_buku)

            print("\nBuku berhasil dikembalikan.")

            return

    print("\nBuku tidak ditemukan.")


# ================================
# FUNCTION UNDO
# ================================

def undo_peminjaman():

    if undo_stack.is_empty():
        print("\nTidak ada data undo.")
        return

    buku = undo_stack.pop()

    buku["status"] = "Tersedia"

    save_buku(daftar_buku)

    print(f"\nUndo berhasil untuk buku: {buku['judul']}")


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
=================================
""")

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