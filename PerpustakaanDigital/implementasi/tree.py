# =====================================
# tree.py
# Binary Search Tree (BST)
# Untuk: Pencarian Buku Berdasarkan Judul
# =====================================

class NodeBST:
    def __init__(self, buku):
        self.buku = buku          # data buku (dictionary)
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ================================
    # INSERT (rekursif)
    # ================================
    def _insert_rekursif(self, node, buku):
        if node is None:
            return NodeBST(buku)
        if buku["judul"].lower() < node.buku["judul"].lower():
            node.left = self._insert_rekursif(node.left, buku)
        elif buku["judul"].lower() > node.buku["judul"].lower():
            node.right = self._insert_rekursif(node.right, buku)
        return node

    def insert(self, buku):
        self.root = self._insert_rekursif(self.root, buku)

    # ================================
    # SEARCH (rekursif)
    # ================================
    def _search_rekursif(self, node, keyword):
        if node is None:
            return None
        judul = node.buku["judul"].lower()
        if keyword in judul:
            return node.buku
        # BST: cari ke kiri dan kanan karena pakai 'contains' bukan exact match
        hasil_kiri = self._search_rekursif(node.left, keyword)
        if hasil_kiri:
            return hasil_kiri
        return self._search_rekursif(node.right, keyword)

    def search(self, keyword):
        return self._search_rekursif(self.root, keyword.lower())

    # ================================
    # IN-ORDER TRAVERSAL (rekursif)
    # Menampilkan buku urut abjad
    # ================================
    def _inorder_rekursif(self, node, hasil):
        if node is None:
            return
        self._inorder_rekursif(node.left, hasil)
        hasil.append(node.buku)
        self._inorder_rekursif(node.right, hasil)

    def tampil_terurut(self):
        hasil = []
        self._inorder_rekursif(self.root, hasil)
        if not hasil:
            print("\nBelum ada buku di BST.")
            return
        print("\n===== BUKU TERURUT (BST In-Order) =====")
        for buku in hasil:
            print(f"""
Judul    : {buku['judul']}
Penulis  : {buku['penulis']}
Stok     : {buku['stok']}
--------------------------------------""")

    # ================================
    # HITUNG TOTAL NODE (rekursif)
    # ================================
    def _hitung_rekursif(self, node):
        if node is None:
            return 0
        return 1 + self._hitung_rekursif(node.left) + self._hitung_rekursif(node.right)

    def total_buku(self):
        return self._hitung_rekursif(self.root)

    def build_from_list(self, daftar_buku):
        """Bangun BST dari daftar buku yang ada"""
        for buku in daftar_buku:
            self.insert(buku)
