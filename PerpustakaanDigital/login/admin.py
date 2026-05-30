from utils import tambah_buku, hapus_buku, tampil_buku, cari_buku, sorting_buku, pinjam_buku, kembalikan_buku, undo_peminjaman
from colorama import init, Fore, Style
import os

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def Admin():
    clear()
    while True:
        print(Fore.CYAN + "=" * 50)
        print(Fore.YELLOW + Style.BRIGHT + "     👤 ADMIN MENU ")
        print(Fore.CYAN + "=" * 50)

        print(Fore.BLUE   + "[1]" + Fore.WHITE + " Tambah Buku")
        print(Fore.BLUE   + "[2]" + Fore.WHITE + " Hapus Buku")
        print(Fore.BLUE   + "[3]" + Fore.WHITE + " Tampilkan Buku")
        print(Fore.BLUE   + "[4]" + Fore.WHITE + " Cari Buku")
        print(Fore.BLUE   + "[5]" + Fore.WHITE + " Sorting Buku")
        print(Fore.BLUE   + "[6]" + Fore.WHITE + " Pinjam Buku")
        print(Fore.BLUE   + "[7]" + Fore.WHITE + " Kembalikan Buku")
        print(Fore.BLUE   + "[8]" + Fore.WHITE + " Undo Peminjaman")
        print(Fore.RED    + "[9]" + Fore.WHITE + " Keluar")

        print(Fore.CYAN + "=" * 50)

        pilihan = input(Fore.YELLOW + "Masukkan pilihan : ")

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
            print(Fore.GREEN + "\n✅ Program selesai.")
            break

        else:
            print(Fore.RED + "\n❌ Pilihan tidak valid.")

        input(Fore.CYAN + "\nTekan ENTER untuk kembali ke menu...")



def login_admin(ADMIN_USERNAME, ADMIN_PASSWORD):
    print("\n=== LOGIN ADMIN ===")

    username = input("Username : ")
    password = input("Password : ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\nLogin berhasil!")
        return True

    print("\nUsername atau password salah!")
    return False