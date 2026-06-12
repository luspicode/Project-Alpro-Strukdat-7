from colorama import init, Fore, Style
from utils import tampil_buku, cari_buku, pinjam_buku, kembalikan_buku, tampil_buku_unggulan, tampil_rekomendasi
from filehandler import simpan_user, load_histori
import os

init(autoreset=True) #bersihkan warna/format colorama setelah print

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #clear terminal

class User: #buat class user
    def __init__(self):
        self.nama = None

    def tampilkan_menu(self):
        while True:
            clear()
            print(Fore.CYAN + "=" * 55)
            print(Fore.YELLOW + Style.BRIGHT + f"        📚 PERPUSTAKAAN DIGITAL — {self.nama.upper()}")
            print(Fore.CYAN + "=" * 55)
            print(Fore.BLUE + "[1]" + Fore.WHITE + " Tampilkan Semua Buku")
            print(Fore.BLUE + "[2]" + Fore.WHITE + " Cari Buku")
            print(Fore.BLUE + "[3]" + Fore.WHITE + " Pinjam Buku")
            print(Fore.BLUE + "[4]" + Fore.WHITE + " Kembalikan Buku")
            print(Fore.BLUE + "[5]" + Fore.WHITE + " Riwayat Peminjaman Saya")
            print(Fore.BLUE + "[6]" + Fore.WHITE + " Buku Unggulan (Circular LL)")
            print(Fore.BLUE + "[7]" + Fore.WHITE + " Rekomendasi Kategori (Graph)")
            print(Fore.RED  + "[0]" + Fore.WHITE + " Keluar")
            print(Fore.CYAN + "=" * 55)

            pilihan = input(Fore.YELLOW + "Masukkan pilihan : ").strip()

            if   pilihan == "1": tampil_buku()
            elif pilihan == "2": cari_buku()
            elif pilihan == "3": pinjam_buku(self.nama)
            elif pilihan == "4": kembalikan_buku(self.nama)
            elif pilihan == "5": self.tampil_histori_user()
            elif pilihan == "6": tampil_buku_unggulan()
            elif pilihan == "7": tampil_rekomendasi()
            elif pilihan == "0":
                print(Fore.GREEN + "\n✅ Terima kasih, sampai jumpa!")
                input(Fore.CYAN + "\nTekan ENTER untuk kembali ke menu...")
                break
            else:
                print(Fore.RED + "\n❌ Pilihan tidak valid.")

            input(Fore.CYAN + "\nTekan ENTER untuk kembali ke menu...")

    def tampil_histori_user(self):
        clear()
        try:
            semua_histori = load_histori()
            # Filter hanya histori milik user ini (pakai list comprehension)
            histori_saya = [h for h in semua_histori if h["nama"].lower() == self.nama.lower()]

            if not histori_saya:
                print(f"\nBelum ada riwayat peminjaman untuk {self.nama}.")
                return

            print(f"\n===== RIWAYAT PEMINJAMAN — {self.nama.upper()} =====")
            for item in histori_saya:
                print(f"""
Judul    : {item['judul']}
Aksi     : {item['aksi']}
-----------------------------------------""")

        except Exception as e:
            print(f"\n❌ Terjadi kesalahan: {e}")

    def login_user(self):
        try:
            while True:
                self.nama = input("Masukkan Nama Anda : ").strip()
                if self.nama == "":
                    print("❌ Nama tidak boleh kosong!")
                else:
                    break
            simpan_user(self.nama) #nambah nama ke user.csv
            print(f"\n✅ Selamat datang, {self.nama}!")
            return self.nama

        except Exception as e:
            print(f"\n❌ Terjadi kesalahan saat login: {e}")
            return None
