# =====================================
# graph.py
# Graph - Rekomendasi Buku Berdasarkan Kategori
# Adjacency List (Dictionary)
# =====================================

class Graph:
    def __init__(self):
        # dictionary: key=kategori, value=set of kategori terkait
        # SET dipakai di sini untuk menghindari duplikat relasi
        self.adjacency_list = {}

    def tambah_kategori(self, kategori):
        if kategori not in self.adjacency_list:
            self.adjacency_list[kategori] = set()   # <-- SET
        else:
            print(f"\nKategori '{kategori}' sudah ada.")

    def tambah_relasi(self, kategori1, kategori2):
        """Tambah relasi dua arah antar kategori"""
        if kategori1 not in self.adjacency_list:
            self.tambah_kategori(kategori1)
        if kategori2 not in self.adjacency_list:
            self.tambah_kategori(kategori2)
        # set.add() otomatis cegah duplikat
        self.adjacency_list[kategori1].add(kategori2)
        self.adjacency_list[kategori2].add(kategori1)

    def rekomendasi(self, kategori):
        """Return set kategori yang berkaitan"""
        if kategori not in self.adjacency_list:
            return set()
        return self.adjacency_list[kategori]   # <-- return SET

    def semua_kategori(self):
        """Return set semua kategori yang ada (unik)"""
        return set(self.adjacency_list.keys())  # <-- SET

    def tampil_graph(self):
        print("\n========== RELASI KATEGORI BUKU ==========")
        if not self.adjacency_list:
            print("Belum ada data kategori.")
            return
        for kategori, relasi in self.adjacency_list.items():
            relasi_str = ", ".join(sorted(relasi)) if relasi else "(tidak ada relasi)"
            print(f"  {kategori:20s} --> {relasi_str}")
