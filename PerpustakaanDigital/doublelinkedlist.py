# structures/doublelinkedlist.py
# Double Linked List untuk menyimpan histori peminjaman.

class Node:
    # Node punya next dan prev
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def tambah_histori(self, data):
        # Menambah histori ke akhir list
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
            return

        self.tail.next = node_baru
        node_baru.prev = self.tail
        self.tail = node_baru


    def tampil_maju(self):
        # Menampilkan histori dari awal ke akhir
        if self.head is None:
            print("\nHistori kosong.")
            return

        current = self.head

        print("\n========== HISTORI PEMINJAMAN ==========")

        while current:
            data = current.data

            print(f"""
Username : {data['username']}
Aksi     : {data['aksi']}
ID Buku  : {data['id_buku']}
Judul    : {data['judul']}
-----------------------------------------
""")

            current = current.next


    def tampil_mundur(self):
        # Menampilkan histori dari terbaru ke awal
        if self.tail is None:
            print("\nHistori kosong.")
            return

        current = self.tail

        print("\n========== HISTORI TERBARU ==========")

        while current:
            data = current.data
            print(f"{data['username']} - {data['aksi']} - {data['judul']}")
            current = current.prev