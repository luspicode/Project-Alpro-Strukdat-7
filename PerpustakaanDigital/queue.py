# =====================================
# queue.py
# Queue untuk Antrian Peminjaman Buku
# FIFO (First In First Out)
# =====================================

class Queue:

    def __init__(self):
        self.data = []

    # =========================
    # TAMBAH ANTRIAN
    # =========================
    def enqueue(self, item):

        self.data.append(item)

        print(f"\n{item} masuk ke antrian.")

    # =========================
    # HAPUS ANTRIAN
    # =========================
    def dequeue(self):

        if self.is_empty():
            print("\nAntrian kosong.")
            return None

        return self.data.pop(0)

    # =========================
    # LIHAT ANTRIAN DEPAN
    # =========================
    def front(self):

        if self.is_empty():
            return None

        return self.data[0]

    # =========================
    # CEK APAKAH KOSONG
    # =========================
    def is_empty(self):

        return len(self.data) == 0

    # =========================
    # JUMLAH ANTRIAN
    # =========================
    def size(self):

        return len(self.data)

    # =========================
    # TAMPILKAN ANTRIAN
    # =========================
    def tampil_antrian(self):

        if self.is_empty():
            print("\nAntrian kosong.")
            return

        print("\n========== ANTRIAN PEMINJAMAN ==========")

        nomor = 1

        for item in self.data:
            print(f"{nomor}. {item}")
            nomor += 1

    # =========================
    # CLEAR ANTRIAN
    # =========================
    def clear(self):

        self.data.clear()

        print("\nAntrian berhasil dikosongkan.")