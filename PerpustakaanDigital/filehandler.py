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
                "status": row["status"],
                "peminjam" : row.get("peminjam", "")
            })

    return data


def save_buku(data):

    os.makedirs("data", exist_ok=True)

    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["id", "judul", "penulis", "tahun", "status", "peminjam"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for buku in data:
            writer.writerow(buku)


def edit_buku(data, id_buku, data_baru):

    for i in range(len(data)):
        if data[i]["id"] == id_buku:
            data[i].update(data_baru)
            save_buku(data)
            return True

    return False


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
            writer = csv.writer(file)
            writer.writerow(["nama", "judul", "aksi"])

    # Tambah histori
    with open(HISTORY_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([nama, judul, aksi])