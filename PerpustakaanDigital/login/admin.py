from utils import (tambah_buku, hapus_buku, tampil_buku, cari_buku,
                   sorting_buku, undo_peminjaman, registrasi_admin,
                   tampilkan_admin, tampil_histori, tampil_buku_baru_sesi,
                   tampil_buku_unggulan, tampil_rekomendasi, statistik_buku,
                   tampil_buku_bst)
from implementasi.hashtable import HashTable
from filehandler import load_admin
from colorama import init, Fore, Style
import os

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

admin = HashTable()
load_admin(admin)

def Admin():
    clear()
    while True:
        print(Fore.CYAN + "=" * 55)
        print(Fore.YELLOW + Style.BRIGHT + "        📚 PERPUSTAKAAN DIGITAL — ADMIN")
        print(Fore.CYAN + "=" * 55)
        print(Fore.BLUE  + "[1]"  + Fore.WHITE + " Tambah Buku")
        print(Fore.BLUE  + "[2]"  + Fore.WHITE + " Hapus Buku")
        print(Fore.BLUE  + "[3]"  + Fore.WHITE + " Tampilkan Semua Buku")
        print(Fore.BLUE  + "[4]"  + Fore.WHITE + " Cari Buku")
        print(Fore.BLUE  + "[5]"  + Fore.WHITE + " Sorting Buku (Bubble Sort)")
        print(Fore.BLUE  + "[6]"  + Fore.WHITE + " Tampil Buku Terurut (BST)")
        print(Fore.BLUE  + "[7]"  + Fore.WHITE + " Undo Peminjaman (Stack)")
        print(Fore.BLUE  + "[8]"  + Fore.WHITE + " Buku Baru Sesi Ini (Single LL)")
        print(Fore.BLUE  + "[9]"  + Fore.WHITE + " Buku Unggulan (Circular LL)")
        print(Fore.BLUE  + "[10]" + Fore.WHITE + " Rekomendasi Kategori (Graph)")
        print(Fore.BLUE  + "[11]" + Fore.WHITE + " Statistik Perpustakaan")
        print(Fore.BLUE  + "[12]" + Fore.WHITE + " Histori Peminjaman (Double LL)")
        print(Fore.BLUE  + "[13]" + Fore.WHITE + " Tampilkan Daftar Admin")
        print(Fore.BLUE  + "[14]" + Fore.WHITE + " Registrasi Admin Cabang")
        print(Fore.RED   + "[0]"  + Fore.WHITE + " Keluar")
        print(Fore.CYAN + "=" * 55)

        pilihan = input(Fore.YELLOW + "Masukkan pilihan : ").strip()

        if   pilihan == "1":  tambah_buku()
        elif pilihan == "2":  hapus_buku()
        elif pilihan == "3":  tampil_buku()
        elif pilihan == "4":  cari_buku()
        elif pilihan == "5":  sorting_buku()
        elif pilihan == "6":  tampil_buku_bst()
        elif pilihan == "7":  undo_peminjaman()
        elif pilihan == "8":  tampil_buku_baru_sesi()
        elif pilihan == "9":  tampil_buku_unggulan()
        elif pilihan == "10": tampil_rekomendasi()
        elif pilihan == "11": statistik_buku()
        elif pilihan == "12": tampil_histori()
        elif pilihan == "13": tampilkan_admin(admin)
        elif pilihan == "14": registrasi_admin(admin)
        elif pilihan == "0":
            print(Fore.GREEN + "\n✅ Keluar dari menu admin.")
            input(Fore.CYAN + "\nTekan ENTER untuk kembali ke menu...")
            break
        else:
            print(Fore.RED + "\n❌ Pilihan tidak valid.")

        input(Fore.CYAN + "\nTekan ENTER untuk kembali ke menu...")


def login_admin():
    clear()
    try:
        print("\n===== LOGIN ADMIN =====")
        username = input("Username : ").strip()
        password = input("Password : ").strip()

        data = admin.login(username, password)
        if data and data["role"] == "admin":
            print("\n✅ Login berhasil!")
            return True

        print("\n❌ Username atau password salah.")
        input(Fore.CYAN + "\nTekan ENTER untuk kembali ke menu...")
        return False

    except Exception as e:
        print(f"\n❌ Terjadi kesalahan saat login: {e}")
        input(Fore.CYAN + "\nTekan ENTER untuk kembali ke menu...")
        return False
    
        

