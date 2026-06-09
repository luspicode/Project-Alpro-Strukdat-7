import csv
import os

FILE_NAME = "data/buku.csv"


def load_buku():
    data = []

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
                "stok": row["stok"],
            })

    return data


def save_buku(data):

    os.makedirs("data", exist_ok=True)

    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["id", "judul", "penulis", "tahun", "stok"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for buku in data:
            writer.writerow(buku)


USER_FILE = "data/user.csv"

def simpan_user(nama):
    os.makedirs("data", exist_ok=True)

    # buat file kalau belum ada
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["nama"])

    # cek apakah user sudah pernah tercatat
    with open(USER_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row.get("nama", "").lower() == nama.lower():
                return

    # simpan user baru
    with open(USER_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([nama])


HISTORY_FILE = "data/histori.csv"

def simpan_histori(nama, judul, aksi):
    os.makedirs("data", exist_ok=True)

    # Buat file jika belum ada
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["nama", "judul", "status"]
            writer = csv.writer(file)
            writer.writerow(["nama", "judul", "aksi"])

    # Tambah histori
    with open(HISTORY_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([nama, judul, aksi])
        

def load_histori():
    data = []

    if not os.path.exists(FILE_NAME):
        return data

    with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append({
                "nama": row["nama"],
                "judul": row["judul"],
                "status": row["status"]
            })
    return data

FILE_AKUN = "data/admin.csv"


def load_admin(hashtable):

    if not os.path.exists(FILE_AKUN):
        return

    with open(FILE_AKUN, mode="r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            hashtable.insert(
                row["username"],
                row["password"],
                row["role"]
            )


def save_admin(hashtable):

    with open(FILE_AKUN, mode="w", newline="") as file:

        fieldnames = ["username", "password", "role"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for bucket in hashtable.table:

            for user in bucket:

                writer.writerow(user)