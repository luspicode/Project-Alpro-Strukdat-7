# structures/circularlinkedlist.py
# Circular Linked List untuk rotasi buku unggulan.

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None


    def tambah_buku(self, data):
        # Menambah buku ke circular linked list
        node_baru = Node(data)

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
        # Menampilkan semua buku unggulan
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
Kategori : {buku['kategori']}
Status   : {buku['status']}
--------------------------------
""")

            current = current.next

            if current == self.head:
                break


    def next_buku(self):
        # Mengambil buku unggulan lalu berpindah ke buku berikutnya
        if self.head is None:
            print("\nBelum ada buku unggulan.")
            return None

        buku = self.head.data
        self.head = self.head.next

        return buku


    def jumlah_buku(self):
        # Menghitung jumlah node
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