#Linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next



#Circular Linkedlist
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
    
    
#Circular Double LInkedlist
