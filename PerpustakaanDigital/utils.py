# ================================
# SISTEM PERPUSTAKAAN DIGITAL
# utils.py
# DIPAKAI UNTUK MENYELESAIKAN SEMUA PROSES SEHINGGA "MAIN" TINGGAL PANGGIL
# ================================

from stack import Stack
from queue import Queue
from filehandler import load_buku, save_buku
from searching import linear_search
from sorting import bubble_sort_judul


# ================================
# DATA AWAL
# ================================

daftar_buku = load_buku()
undo_stack = Stack()
antrian = Queue()

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
----------------------------------""")


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

