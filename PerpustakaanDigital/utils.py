# ================================
# SISTEM PERPUSTAKAAN DIGITAL
# utils.py
# DIPAKAI UNTUK MENYELESAIKAN SEMUA PROSES SEHINGGA "MAIN" TINGGAL PANGGIL
# ================================

from implementasi.stack import Stack 
from implementasi.queue import Queue
from filehandler import load_buku, save_buku, simpan_histori
from implementasi.searching import linear_search
from implementasi.sorting import bubble_sort_judul
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    clear()
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
    clear()
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
# FUNCTION HAPUS BUKU
# ================================
def hapus_buku():
    clear()
    pass


# ================================
# FUNCTION CARI BUKU
# ================================

def cari_buku():
    clear()
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
    clear()
    bubble_sort_judul(daftar_buku)

    print("\nBuku berhasil diurutkan berdasarkan judul!")


# ================================
# FUNCTION PINJAM BUKU
# ================================

def pinjam_buku(nama):
    clear()
    id_buku = input("\nMasukkan ID buku yang ingin dipinjam : ")

    for buku in daftar_buku:

        if buku["id"] == id_buku:

            if buku["status"] == "Dipinjam":
                print("\nBuku sedang dipinjam.")
                return

            antrian.enqueue(nama)

            buku["status"] = "Dipinjam"
            buku["peminjam"] = nama

            simpan_histori(nama, buku["judul"], "PINJAM")

            undo_stack.push(buku)

            save_buku(daftar_buku)

            # simpan histori
            simpan_histori(nama, buku["judul"], "PINJAM")

            print(f"\n{nama} berhasil meminjam buku.")

            return

    print("\nBuku tidak ditemukan.")
    
# ================================
# FUNCTION PENGEMBALIAN
# ================================

def kembalikan_buku():
    clear()
    id_buku = input("\nMasukkan ID buku yang dikembalikan : ")

    for buku in daftar_buku:

        if buku["id"] == id_buku:

            if buku["status"] == "Tersedia":
                print("\nBuku belum dipinjam.")
                return

            nama = buku["peminjam"]

            buku["status"] = "Tersedia"
            buku["peminjam"] = ""

            save_buku(daftar_buku)

            simpan_histori(nama, buku["judul"], "KEMBALI")

            print(f"\nBuku berhasil dikembalikan oleh {nama}.")

            return

    print("\nBuku tidak ditemukan.")


# ================================
# FUNCTION UNDO
# ================================

def undo_peminjaman():
    clear()
    if undo_stack.is_empty():
        print("\nTidak ada data undo.")
        return

    buku = undo_stack.pop()

    buku["status"] = "Tersedia"

    save_buku(daftar_buku)

    print(f"\nUndo berhasil untuk buku: {buku['judul']}")

