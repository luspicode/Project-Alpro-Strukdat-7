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
                "status": row["status"]
            })

    return data


def save_buku(data):

    os.makedirs("data", exist_ok=True)

    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["id", "judul", "penulis", "tahun", "status"]
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
