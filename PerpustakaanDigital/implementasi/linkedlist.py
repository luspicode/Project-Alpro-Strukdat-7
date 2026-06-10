# =====================================
# linkedlist.py
# =====================================

# ================================
# SINGLE LINKED LIST
# Untuk: Daftar Buku Baru (sesi admin)
# ================================

class NodeSLL:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def tambah_buku_baru(self, buku):
        """Tambah buku baru ke akhir list"""
        node_baru = NodeSLL(buku)
        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru
        self.size += 1

    def tampil_buku_baru(self):
        """Tampilkan semua buku yang ditambahkan di sesi ini"""
        if self.is_empty():
            print("\nBelum ada buku baru yang ditambahkan di sesi ini.")
            return

        print(f"\n===== BUKU BARU SESI INI ({self.size} buku) =====")
        current = self.head
        nomor = 1
        while current:
            buku = current.data
            print(f"""
[{nomor}] ID      : {buku['id']}
    Judul   : {buku['judul']}
    Penulis : {buku['penulis']}
    Tahun   : {buku['tahun']}
    Stok    : {buku['stok']}
----------------------------------""")
            nomor += 1
            current = current.next

    def hitung_rekursif(self, node):
        """Rekursif: hitung total buku baru di sesi ini"""
        if node is None:
            return 0
        return 1 + self.hitung_rekursif(node.next)

    def total_buku_baru(self):
        return self.hitung_rekursif(self.head)


# ================================
# CIRCULAR LINKED LIST
# Untuk: Rotasi Buku Unggulan
# ================================

class NodeCLL:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah_buku(self, data):
        node_baru = NodeCLL(data)
        if self.head is None:
            self.head = node_baru
            node_baru.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = node_baru
        node_baru.next = self.head

    def tampil_buku(self):
        if self.head is None:
            print("\nBelum ada buku unggulan.")
            return
        current = self.head
        print("\n===== DAFTAR BUKU UNGGULAN =====")
        while True:
            buku = current.data
            print(f"""
Judul    : {buku['judul']}
Penulis  : {buku['penulis']}
--------------------------------""")
            current = current.next
            if current == self.head:
                break

    def next_buku(self):
        if self.head is None:
            return None
        buku = self.head.data
        self.head = self.head.next
        return buku

    def jumlah_buku(self):
        if self.head is None:
            return 0
        total = 0
        current = self.head
        while True:
            total += 1
            current = current.next
            if current == self.head:
                break
        return total


# ================================
# DOUBLE LINKED LIST
# Untuk: Histori Peminjaman (navigasi maju-mundur)
# ================================

class NodeDLL:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def tambah_histori(self, nama, judul, aksi):
        """Tambah entri histori ke akhir list"""
        data = {"nama": nama, "judul": judul, "aksi": aksi}
        node_baru = NodeDLL(data)

        if self.is_empty():
            self.head = node_baru
            self.tail = node_baru
        else:
            node_baru.prev = self.tail
            self.tail.next = node_baru
            self.tail = node_baru

        self.size += 1

    def tampil_maju(self):
        """Tampilkan histori dari awal ke akhir (kronologis)"""
        if self.is_empty():
            print("\nBelum ada histori.")
            return

        print(f"\n===== HISTORI PEMINJAMAN — MAJU ({self.size} entri) =====")
        current = self.head
        nomor = 1
        while current:
            h = current.data
            print(f"[{nomor}] {h['nama']:15s} | {h['judul']:20s} | {h['aksi']}")
            current = current.next
            nomor += 1

    def tampil_mundur(self):
        """Tampilkan histori dari akhir ke awal (terbaru duluan)"""
        if self.is_empty():
            print("\nBelum ada histori.")
            return

        print(f"\n===== HISTORI TERBARU — MUNDUR ({self.size} entri) =====")
        current = self.tail
        nomor = 1
        while current:
            h = current.data
            print(f"[{nomor}] {h['nama']:15s} | {h['judul']:20s} | {h['aksi']}")
            current = current.prev
            nomor += 1

    def build_from_list(self, daftar_histori):
        """Bangun DLL dari list histori yang di-load dari CSV"""
        for item in daftar_histori:
            self.tambah_histori(item["nama"], item["judul"], item["aksi"])
