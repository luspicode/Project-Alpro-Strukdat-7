# ================================
# SISTEM PERPUSTAKAAN DIGITAL
# main.py
# ================================
import os
from implementasi.tampilan import menu_awal
from login.admin import Admin, login_admin
from login.user import User

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# login.py


while True:
    clear()
    pilihan = menu_awal()
    clear()
    if pilihan == "1":
        if login_admin():
            Admin()
        else:
            print("Username atau Password Salah")

    elif pilihan == "2":
        user = User()
        nama = user.login_user()
        user.tampilkan_menu()

    elif pilihan == "0":
        break