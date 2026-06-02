# ================================
# SISTEM PERPUSTAKAAN DIGITAL
# main.py
# ================================
import os
from implementasi.tampilan import menu_awal
from login.admin import Admin, login_admin
from login.user import User, login_user

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# login.py

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

while True:
    clear()
    pilihan = menu_awal()
    clear()
    if pilihan == "1":
        if login_admin(ADMIN_USERNAME, ADMIN_PASSWORD):
            Admin()
        else:
            print("Username atau Password Salah")

    elif pilihan == "2":
        nama = login_user()
        User(nama)

    elif pilihan == "0":
        break