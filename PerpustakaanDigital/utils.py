# ================================
# SISTEM PERPUSTAKAAN DIGITAL
# utils.py
# DIPAKAI UNTUK MENYELESAIKAN SEMUA PROSES SEHINGGA "MAIN" TINGGAL PANGGIL
# ================================

from implementasi.stack import Stack 
from filehandler import load_buku, save_buku, simpan_histori, save_admin, load_histori
from implementasi.searching import linear_search
from implementasi.sorting import bubble_sort_judul
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ================================
# DATA AWAL
# ================================

daftar_buku = load_buku()
daftar_histori = load_histori()
undo_stack = Stack()


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
Stok     : {buku['stok']}
----------------------------------""")


# ================================
# FUNCTION TAMBAH BUKU
# ================================

def tambah_buku():
    clear()

    id_buku = input("Masukkan ID Buku : ")
    judul = input("Masukkan Judul Buku : ")
    stok_tambah = int(input("Masukkan Stok Buku : "))

    for buku in daftar_buku:
        if buku["id"] == id_buku or buku["judul"] == judul:
            buku["stok"] = int(buku["stok"]) + stok_tambah
            save_buku(daftar_buku)
            print("\nBuku sudah ada, stok berhasil ditambahkan!")
            return

    penulis = input("Masukkan Penulis Buku : ")
    tahun = input("Masukkan Tahun Buku : ")

    buku_baru = {
        "id": id_buku,
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "stok": stok_tambah
    }

    daftar_buku.append(buku_baru)
    save_buku(daftar_buku)

    print("\nBuku baru berhasil ditambahkan!")

# ================================
# FUNCTION HAPUS BUKU
# ================================
def hapus_buku():
    clear()

    id_buku = input("Masukkan ID Buku yang akan dihapus : ")

    for buku in daftar_buku:
        if buku["id"] == id_buku:

            print("\nData Buku:")
            print(f"ID      : {buku['id']}")
            print(f"Judul   : {buku['judul']}")
            print(f"Penulis : {buku['penulis']}")
            print(f"Tahun   : {buku['tahun']}")
            print(f"Stok    : {buku['stok']}")

            konfirmasi = input("\nYakin ingin menghapus? (y/n): ")

            if konfirmasi.lower() == "y":
                daftar_buku.remove(buku)
                save_buku(daftar_buku)
                print("\nBuku berhasil dihapus!")
            else:
                print("\nPenghapusan dibatalkan.")

            return

    print("\nBuku tidak ditemukan!")


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
        print(f"Stok     : {hasil['stok']}")
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

            if buku["stok"] == "0":
                print("\nBuku sedang dipinjam (Stok Habis).")
                return

            buku["stok"] = int(buku["stok"]) - 1
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

def kembalikan_buku(nama):
    clear()
    for buku in daftar_buku:
        id_buku = input("\nMasukkan ID buku yang dikembalikan : ")
        if buku["id"] == id_buku:

            buku["stok"] = int(buku["stok"]) + 1

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

    buku["stok"] = int(buku["stok"]) + 1

    save_buku(daftar_buku)
    simpan_histori("admin", buku["judul"], "KEMBALI")

    print(f"\nUndo berhasil untuk buku: {buku['judul']}")

def tampilkan_admin(admin):
    admin.tampil_admin()

def registrasi_admin(admin):

    clear()
    username = input("\nBuat Username : ")
    password = input("Buat Password : ")

    berhasil = admin.insert(
        username,
        password,
        "admin"
    )

    if berhasil:
        save_admin(admin)