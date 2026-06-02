from colorama import init, Fore, Style
from utils import tampil_buku, cari_buku, pinjam_buku, kembalikan_buku
from filehandler import simpan_user


init(autoreset=True)

def User(nama):
    while True:
        print(Fore.CYAN + "=" * 50)
        print(Fore.YELLOW + "   👤 USER MENU")
        print(Fore.CYAN + "=" * 50)

        print(Fore.BLUE + "[1]" + Fore.WHITE + " Tampilkan Buku")
        print(Fore.BLUE + "[2]" + Fore.WHITE + " Cari Buku")
        print(Fore.BLUE + "[3]" + Fore.WHITE + " Pinjam Buku")
        print(Fore.BLUE + "[4]" + Fore.WHITE + " Kembalikan Buku")
        print(Fore.RED  + "[5]" + Fore.WHITE + " Keluar")

        print(Fore.CYAN + "=" * 50)

        pilihan = input(Fore.YELLOW + "Masukkan pilihan : ")

        if pilihan == "1":
            tampil_buku()

        elif pilihan == "2":
            cari_buku()

        elif pilihan == "3":
            pinjam_buku(nama)

        elif pilihan == "4":
            kembalikan_buku(nama)

        elif pilihan == "5":
            print(Fore.GREEN + "\n✅ Terima kasih telah menggunakan sistem.")
            break

        else:
            print(Fore.RED + "\n❌ Pilihan tidak valid.")

        input(Fore.CYAN + "\nTekan ENTER untuk kembali ke menu...")




def login_user():
    nama = input("Masukkan nama Anda: ")

    if nama.strip() == "":
        print("Nama tidak boleh kosong!")
        return None

    simpan_user(nama)

    print(f"Selamat datang, {nama}!")
    return nama