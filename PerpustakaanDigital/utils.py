# ================================
# SISTEM PERPUSTAKAAN DIGITAL
# utils.py
# ================================

import os
from implementasi.stack import Stack
from implementasi.linkedlist import SingleLinkedList, CircularLinkedList, DoubleLinkedList
from implementasi.tree import BinarySearchTree
from implementasi.graph import Graph
from filehandler import load_buku, save_buku, simpan_histori, save_admin, load_histori
from implementasi.searching import linear_search, binary_search
from implementasi.sorting import bubble_sort_judul

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ================================
# INISIALISASI STRUKTUR DATA
# ================================

# List: daftar utama buku
daftar_buku = load_buku()

# Stack: untuk undo peminjaman
undo_stack = Stack()

# Single Linked List: buku baru yang ditambahkan di sesi ini
buku_baru_sesi = SingleLinkedList()

# Circular Linked List: buku unggulan (diisi otomatis dari data)
buku_unggulan = CircularLinkedList()

# BST: untuk pencarian cepat
bst = BinarySearchTree()
bst.build_from_list(daftar_buku)

# Double Linked List: histori peminjaman (navigasi maju-mundur)
dll_histori = DoubleLinkedList()
dll_histori.build_from_list(load_histori())

# Graph: relasi kategori buku
graph_kategori = Graph()
# Tuple: pasangan relasi kategori default (immutable — tidak berubah)
RELASI_KATEGORI = (
    ("Pemrograman", "Algoritma"),
    ("Pemrograman", "Basis Data"),
    ("Algoritma", "Matematika"),
    ("Jaringan", "Keamanan"),
    ("Basis Data", "Sistem Informasi"),
)
for k1, k2 in RELASI_KATEGORI:
    graph_kategori.tambah_relasi(k1, k2)


# ================================
# TAMPIL BUKU
# ================================

def tampil_buku():
    clear()
    if not daftar_buku:
        print("\nBelum ada buku.")
        return

    print("\n========== DAFTAR BUKU ==========")
    for buku in daftar_buku:
        # Tuple: ringkasan buku sebagai tuple (read-only display)
        info = (buku['id'], buku['judul'], buku['penulis'], buku['tahun'], buku['stok'])
        print(f"""
ID       : {info[0]}
Judul    : {info[1]}
Penulis  : {info[2]}
Tahun    : {info[3]}
Stok     : {info[4]}
----------------------------------""")


# ================================
# TAMBAH BUKU
# ================================

def tambah_buku():
    clear()
    try:
        id_buku = input("Masukkan ID Buku : ").strip()
        if not id_buku:
            raise ValueError("ID buku tidak boleh kosong!")

        judul = input("Masukkan Judul Buku : ").strip()
        if not judul:
            raise ValueError("Judul tidak boleh kosong!")

        stok_tambah = int(input("Masukkan Stok Buku : "))
        if stok_tambah < 0:
            raise ValueError("Stok tidak boleh negatif!")

        # Cek apakah buku sudah ada
        for buku in daftar_buku:
            if buku["id"] == id_buku or buku["judul"].lower() == judul.lower():
                buku["stok"] = int(buku["stok"]) + stok_tambah
                save_buku(daftar_buku)
                print("\nBuku sudah ada, stok berhasil ditambahkan!")
                return

        penulis = input("Masukkan Penulis Buku : ").strip()

        tahun = input("Masukkan Tahun Buku : ").strip()
        if not tahun.isdigit():
            raise ValueError("Tahun harus berupa angka!")

        kategori = input("Masukkan Kategori Buku : ").strip()
        if not kategori:
            kategori = "Umum"

        buku_baru = {
            "id": id_buku,
            "judul": judul,
            "penulis": penulis,
            "tahun": tahun,
            "stok": stok_tambah,
            "kategori": kategori
        }

        daftar_buku.append(buku_baru)
        save_buku(daftar_buku)

        # Single Linked List: catat ke daftar buku baru sesi ini
        buku_baru_sesi.tambah_buku_baru(buku_baru)

        # BST: tambah ke tree juga
        bst.insert(buku_baru)

        # Graph: tambahkan kategori buku baru ke graph
        graph_kategori.tambah_kategori(kategori)

        # Circular Linked List: buku baru otomatis jadi buku unggulan
        buku_unggulan.tambah_buku(buku_baru)

        print(f"\nBuku '{judul}' berhasil ditambahkan!")

    except ValueError as e:
        print(f"\n❌ Input tidak valid: {e}")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# HAPUS BUKU
# ================================

def hapus_buku():
    clear()
    try:
        id_buku = input("Masukkan ID Buku yang akan dihapus : ").strip()
        if not id_buku:
            raise ValueError("ID tidak boleh kosong!")

        for buku in daftar_buku:
            if buku["id"] == id_buku:
                print(f"\nID      : {buku['id']}")
                print(f"Judul   : {buku['judul']}")
                print(f"Penulis : {buku['penulis']}")
                print(f"Stok    : {buku['stok']}")

                konfirmasi = input("\nYakin ingin menghapus? (y/n): ")
                if konfirmasi.lower() == "y":
                    daftar_buku.remove(buku)
                    save_buku(daftar_buku)

                    # FIX 1: Rebuild BST agar tidak ada ghost data
                    bst.root = None
                    bst.build_from_list(daftar_buku)

                    # FIX 1: Rebuild CLL buku_unggulan agar sinkron
                    buku_unggulan.head = None
                    for b in daftar_buku:
                        buku_unggulan.tambah_buku(b)

                    print("\n✅ Buku berhasil dihapus!")
                else:
                    print("\nPenghapusan dibatalkan.")
                return

        print("\nBuku tidak ditemukan!")

    except ValueError as e:
        print(f"\n❌ Input tidak valid: {e}")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# CARI BUKU (BST + Linear fallback)
# ================================

def cari_buku():
    clear()
    try:
        keyword = input("\nMasukkan judul buku : ").strip()
        if not keyword:
            raise ValueError("Keyword tidak boleh kosong!")

        # Coba BST dulu
        hasil = bst.search(keyword)

        # Fallback ke linear search kalau BST tidak ketemu
        if not hasil:
            hasil = linear_search(daftar_buku, keyword)

        if hasil:
            print("\n===== BUKU DITEMUKAN =====")
            print(f"ID       : {hasil['id']}")
            print(f"Judul    : {hasil['judul']}")
            print(f"Penulis  : {hasil['penulis']}")
            print(f"Tahun    : {hasil['tahun']}")
            print(f"Stok     : {hasil['stok']}")

            # Graph: tampilkan rekomendasi kategori terkait
            kategori = hasil.get("kategori", "")
            if kategori:
                rekomendasi = graph_kategori.rekomendasi(kategori)
                if rekomendasi:
                    print(f"\n📚 Kategori terkait: {', '.join(rekomendasi)}")
        else:
            print("\nBuku tidak ditemukan.")

    except ValueError as e:
        print(f"\n❌ {e}")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# STATISTIK BUKU
# ================================

def statistik_buku():
    clear()
    try:
        if not daftar_buku:
            print("\nBelum ada buku.")
            return

        # Set: kumpulkan penulis unik
        penulis_unik = set(b["penulis"] for b in daftar_buku)

        # Set: kumpulkan tahun terbit unik
        tahun_unik = set(b["tahun"] for b in daftar_buku)

        # Rekursif lewat BST: total buku di tree
        total_bst = bst.total_buku()

        # Rekursif lewat SLL: total buku baru sesi ini
        total_baru = buku_baru_sesi.total_buku_baru()

        total_stok = sum(int(b["stok"]) for b in daftar_buku)

        print("\n========== STATISTIK PERPUSTAKAAN ==========")
        print(f"Total judul buku     : {len(daftar_buku)}")
        print(f"Total stok buku      : {total_stok}")
        print(f"Jumlah penulis unik  : {len(penulis_unik)}")
        print(f"Tahun terbit ada     : {sorted(tahun_unik)}")
        print(f"Node di BST          : {total_bst}")
        print(f"Buku baru sesi ini   : {total_baru}")
        print(f"\nDaftar Penulis (unik):")
        for p in sorted(penulis_unik):
            print(f"  - {p}")

    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# SORTING BUKU
# ================================

def sorting_buku():
    clear()
    try:
        bubble_sort_judul(daftar_buku)
        save_buku(daftar_buku)  # FIX 3: simpan urutan baru ke CSV
        print("\n✅ Buku berhasil diurutkan berdasarkan judul!")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# PINJAM BUKU
# ================================

def pinjam_buku(nama):
    clear()
    try:
        id_buku = input("\nMasukkan ID buku yang ingin dipinjam : ").strip()
        if not id_buku:
            raise ValueError("ID tidak boleh kosong!")

        for buku in daftar_buku:
            if buku["id"] == id_buku:
                if int(buku["stok"]) == 0:
                    print("\nBuku sedang habis dipinjam.")
                    return

                buku["stok"] = int(buku["stok"]) - 1
                # FIX 2: simpan nama user ke stack agar undo bisa lacak siapa peminjamnya
                undo_stack.push({"id": buku["id"], "judul": buku["judul"], "nama": nama})
                save_buku(daftar_buku)
                simpan_histori(nama, buku["judul"], "PINJAM")
                dll_histori.tambah_histori(nama, buku["judul"], "PINJAM")
                print(f"\n✅ {nama} berhasil meminjam '{buku['judul']}'.")
                return

        print("\nBuku tidak ditemukan.")

    except ValueError as e:
        print(f"\n❌ {e}")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# KEMBALIKAN BUKU
# ================================

def kembalikan_buku(nama):
    clear()
    try:
        id_buku = input("\nMasukkan ID buku yang dikembalikan : ").strip()
        if not id_buku:
            raise ValueError("ID tidak boleh kosong!")

        # Cek histori: hitung berapa kali user PINJAM dan KEMBALI buku ini
        semua_histori = load_histori()
        judul_target = None

        for buku in daftar_buku:
            if buku["id"] == id_buku:
                judul_target = buku["judul"]
                break

        if judul_target is None:
            print("\nBuku tidak ditemukan.")
            return

        # Hitung saldo pinjam user untuk buku ini
        jumlah_pinjam = sum(
            1 for h in semua_histori
            if h["nama"].lower() == nama.lower()
            and h["judul"].lower() == judul_target.lower()
            and h["aksi"] == "PINJAM"
        )
        jumlah_kembali = sum(
            1 for h in semua_histori
            if h["nama"].lower() == nama.lower()
            and h["judul"].lower() == judul_target.lower()
            and h["aksi"] == "KEMBALI"
        )

        saldo_pinjam = jumlah_pinjam - jumlah_kembali

        if saldo_pinjam <= 0:
            print(f"\n❌ Kamu tidak sedang meminjam buku '{judul_target}'.")
            return

        # Sah — proses pengembalian
        for buku in daftar_buku:
            if buku["id"] == id_buku:
                buku["stok"] = int(buku["stok"]) + 1
                save_buku(daftar_buku)
                simpan_histori(nama, buku["judul"], "KEMBALI")
                dll_histori.tambah_histori(nama, buku["judul"], "KEMBALI")
                print(f"\n✅ Buku '{buku['judul']}' berhasil dikembalikan oleh {nama}.")
                return

    except ValueError as e:
        print(f"\n❌ {e}")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# UNDO PEMINJAMAN
# ================================

def undo_peminjaman():
    clear()
    try:
        if undo_stack.is_empty():
            print("\nTidak ada data undo.")
            return

        buku_undo = undo_stack.pop()
        nama_peminjam = buku_undo.get("nama", "unknown")  # FIX 2: ambil nama user asli

        for buku in daftar_buku:
            if buku["id"] == buku_undo["id"]:
                buku["stok"] = int(buku["stok"]) + 1
                save_buku(daftar_buku)

                # FIX 2: catat KEMBALI atas nama user asli, saldo pinjam jadi netral
                simpan_histori(nama_peminjam, buku["judul"], "KEMBALI")
                dll_histori.tambah_histori(nama_peminjam, buku["judul"], "KEMBALI")

                print(f"\n✅ Undo berhasil — peminjaman '{buku['judul']}' oleh {nama_peminjam} dibatalkan.")
                return

        print("\nBuku tidak ditemukan di daftar.")

    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# BUKU BARU SESI INI (Single LL)
# ================================

def tampil_buku_baru_sesi():
    clear()
    total = buku_baru_sesi.total_buku_baru()  # rekursif
    print(f"\nTotal buku ditambahkan sesi ini (rekursif): {total}")
    buku_baru_sesi.tampil_buku_baru()


# ================================
# BUKU UNGGULAN (Circular LL)
# ================================

def tampil_buku_unggulan():
    clear()
    buku_unggulan.tampil_buku()


# ================================
# REKOMENDASI BUKU (Graph)
# ================================

def tampil_rekomendasi():
    clear()
    try:
        graph_kategori.tampil_graph()

        kategori = input("\nMasukkan kategori untuk lihat rekomendasi: ").strip()
        if not kategori:
            raise ValueError("Kategori tidak boleh kosong!")

        # Kumpulkan semua kategori yang relevan: input + kategori terkait
        kategori_terkait = graph_kategori.rekomendasi(kategori)
        if not kategori_terkait and kategori not in graph_kategori.semua_kategori():
            print(f"\nKategori '{kategori}' tidak ditemukan.")
            return

        semua_kategori_relevan = {kategori} | kategori_terkait  # SET union

        # Filter buku yang masuk ke salah satu kategori relevan
        buku_rekomendasi = [
            b for b in daftar_buku
            if b.get("kategori", "").lower() in {k.lower() for k in semua_kategori_relevan}
        ]

        print(f"\n📚 Rekomendasi buku untuk kategori '{kategori}'")
        print(f"   (mencakup: {', '.join(sorted(semua_kategori_relevan))})")
        print("=" * 50)

        if buku_rekomendasi:
            for buku in buku_rekomendasi:
                print(f"""
Judul    : {buku['judul']}
Penulis  : {buku['penulis']}
Kategori : {buku.get('kategori', '-')}
Stok     : {buku['stok']}
--------------------------------------------------""")
        else:
            print("\nBelum ada buku untuk kategori-kategori tersebut.")

    except ValueError as e:
        print(f"\n❌ {e}")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# TAMPIL & REGISTRASI ADMIN
# ================================

def tampilkan_admin(admin):
    admin.tampil_admin()


def registrasi_admin(admin):
    clear()
    try:
        username = input("\nBuat Username : ").strip()
        if not username:
            raise ValueError("Username tidak boleh kosong!")

        password = input("Buat Password : ").strip()
        if not password:
            raise ValueError("Password tidak boleh kosong!")

        berhasil = admin.insert(username, password, "admin")
        if berhasil:
            save_admin(admin)
            print("\n✅ Admin cabang berhasil didaftarkan!")
        else:
            print("\n❌ Gagal: username sudah digunakan.")

    except ValueError as e:
        print(f"\n❌ {e}")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# TAMPIL HISTORI (Double Linked List)
# ================================

def tampil_histori():
    clear()
    try:
        print("\nTampilkan histori:")
        print("[1] Kronologis (maju)")
        print("[2] Terbaru duluan (mundur)")
        pilihan = input("Pilihan : ").strip()

        if pilihan == "1":
            dll_histori.tampil_maju()
        elif pilihan == "2":
            dll_histori.tampil_mundur()
        else:
            print("❌ Pilihan tidak valid.")

    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")


# ================================
# BST: TAMPIL BUKU TERURUT
# ================================

def tampil_buku_bst():
    clear()
    bst.tampil_terurut()
