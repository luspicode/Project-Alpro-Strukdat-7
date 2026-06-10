import csv
import os

FILE_NAME = "data/buku.csv"
USER_FILE = "data/user.csv"
HISTORY_FILE = "data/histori.csv"
FILE_AKUN = "data/admin.csv"


# ================================
# BUKU
# ================================

def load_buku():
    data = []
    try:
        if not os.path.exists(FILE_NAME):
            return data
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    "id": row["id"],
                    "judul": row["judul"],
                    "penulis": row["penulis"],
                    "tahun": row["tahun"],
                    "stok": int(row["stok"]),
                    "kategori": row.get("kategori", "Umum"),
                })
    except FileNotFoundError:
        print("⚠️  File buku tidak ditemukan, memulai dengan data kosong.")
    except Exception as e:
        print(f"⚠️  Gagal memuat data buku: {e}")
    return data


def save_buku(data):
    try:
        os.makedirs("data", exist_ok=True)
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["id", "judul", "penulis", "tahun", "stok", "kategori"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for buku in data:
                writer.writerow(buku)
    except Exception as e:
        print(f"⚠️  Gagal menyimpan data buku: {e}")


# ================================
# USER
# ================================

def simpan_user(nama):
    try:
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(USER_FILE):
            with open(USER_FILE, mode="w", newline="", encoding="utf-8") as file:
                csv.writer(file).writerow(["nama"])

        with open(USER_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("nama", "").lower() == nama.lower():
                    return  # sudah ada

        with open(USER_FILE, mode="a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow([nama])

    except Exception as e:
        print(f"⚠️  Gagal menyimpan user: {e}")


# ================================
# HISTORI
# ================================

def simpan_histori(nama, judul, aksi):
    try:
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, mode="w", newline="", encoding="utf-8") as file:
                csv.writer(file).writerow(["nama", "judul", "aksi"])

        with open(HISTORY_FILE, mode="a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow([nama, judul, aksi])

    except Exception as e:
        print(f"⚠️  Gagal menyimpan histori: {e}")


def load_histori():
    data = []
    try:
        if not os.path.exists(HISTORY_FILE):
            return data
        with open(HISTORY_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("nama") and row.get("judul"):
                    data.append({
                        "nama": row["nama"],
                        "judul": row["judul"],
                        "aksi": row.get("aksi", "-")
                    })
    except Exception as e:
        print(f"⚠️  Gagal memuat histori: {e}")
    return data


# ================================
# ADMIN
# ================================

def load_admin(hashtable):
    try:
        if not os.path.exists(FILE_AKUN):
            return
        with open(FILE_AKUN, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                hashtable.insert(row["username"], row["password"], row["role"])
    except FileNotFoundError:
        print("⚠️  File admin tidak ditemukan.")
    except Exception as e:
        print(f"⚠️  Gagal memuat data admin: {e}")


def save_admin(hashtable):
    try:
        os.makedirs("data", exist_ok=True)
        with open(FILE_AKUN, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["username", "password", "role"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for bucket in hashtable.table:
                for user in bucket:
                    writer.writerow(user)
    except Exception as e:
        print(f"⚠️  Gagal menyimpan data admin: {e}")
