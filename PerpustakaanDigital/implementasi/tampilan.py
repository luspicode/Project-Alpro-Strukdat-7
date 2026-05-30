from colorama import init, Fore, Style

init(autoreset=True)

def header():
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + Style.BRIGHT +
          "📚 SISTEM MANAJEMEN PERPUSTAKAAN DIGITAL")
    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + "Proyek Alpro - Strukdat")
    print(Fore.CYAN + "-" * 60)


def menu_awal():
    header()

    print(Fore.BLUE + "[1]" + Fore.WHITE + " Masuk Sebagai Admin")
    print(Fore.BLUE + "[2]" + Fore.WHITE + " Masuk Sebagai User")
    print(Fore.RED + "[0]" + Fore.WHITE + " Keluar")

    print(Fore.CYAN + "=" * 60)

    pilihan = input(Fore.YELLOW + "Pilih menu : ")
    return pilihan

