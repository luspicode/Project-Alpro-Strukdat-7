
# =====================================
# stack.py
# Stack untuk Undo Peminjaman
# LIFO (Last In First Out)
# =====================================

class Stack:

    def __init__(self):
        self.data = []

    # =========================
    # PUSH
    # MENAMBAHKAN DATA
    # =========================
    def push(self, item):

        self.data.append(item)

        print("\nData berhasil masuk ke stack.")

    # =========================
    # POP
    # MENGAMBIL DATA TERAKHIR
    # =========================
    def pop(self):

        if self.is_empty():
            print("\nStack kosong.")
            return None

        return self.data.pop()

    # =========================
    # MELIHAT DATA PALING ATAS
    # =========================
    def peek(self):

        if self.is_empty():
            return None

        return self.data[-1]

    # =========================
    # CEK APAKAH STACK KOSONG
    # =========================
    def is_empty(self):

        return len(self.data) == 0

    # =========================
    # JUMLAH DATA STACK
    # =========================
    def size(self):

        return len(self.data)

    # =========================
    # TAMPILKAN STACK
    # =========================
    def tampil_stack(self):

        if self.is_empty():
            print("\nStack kosong.")
            return

        print("\n========== ISI STACK ==========")

        # tampil dari atas
        for item in reversed(self.data):

            # kalau item dictionary buku
            if isinstance(item, dict):

                print(f"""
Judul Buku : {item['judul']}
Status     : {item['status']}
----------------------------------
""")

            else:
                print(item)

    # =========================
    # CLEAR STACK
    # =========================
    def clear(self):

        self.data.clear()

        print("\nStack berhasil dikosongkan.")

