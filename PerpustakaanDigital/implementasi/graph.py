# =====================================
# hashtable.py
# Hash Table untuk Login User/Admin
# =====================================

class HashTable:

    def __init__(self, size=10):

        self.size = size
        self.table = [[] for _ in range(size)]

    # =========================
    # HASH FUNCTION
    # =========================
    def hash_function(self, key):

        total = 0

        for char in key:
            total += ord(char)

        return total % self.size

    # =========================
    # TAMBAH USER
    # =========================
    def insert(self, username, password, role):

        index = self.hash_function(username)

        # cek apakah username sudah ada
        for data in self.table[index]:

            if data["username"] == username:
                print("\nUsername sudah digunakan.")
                return

        user = {
            "username": username,
            "password": password,
            "role": role
        }

        self.table[index].append(user)

        print("\nUser berhasil ditambahkan.")

    # =========================
    # LOGIN USER
    # =========================
    def login(self, username, password):

        index = self.hash_function(username)

        for data in self.table[index]:

            if (
                data["username"] == username and
                data["password"] == password
            ):
                return data

        return None

    # =========================
    # HAPUS USER
    # =========================
    def delete(self, username):

        index = self.hash_function(username)

        for i, data in enumerate(self.table[index]):

            if data["username"] == username:

                del self.table[index][i]

                print("\nUser berhasil dihapus.")
                return

        print("\nUser tidak ditemukan.")

    # =========================
    # TAMPILKAN USER
    # =========================
    def tampil_user(self):

        print("\n========== DATA USER ==========")

        kosong = True

        for bucket in self.table:

            for data in bucket:

                kosong = False

                print(f"""
Username : {data['username']}
Role     : {data['role']}
----------------------------------
""")

        if kosong:
            print("Belum ada user.")

    # =========================
    # CARI USER
    # =========================
    def cari_user(self, username):

        index = self.hash_function(username)

        for data in self.table[index]:

            if data["username"] == username:
                return data

        return None

    # =========================
    # UPDATE PASSWORD
    # =========================
    def update_password(self, username, password_baru):

        index = self.hash_function(username)

        for data in self.table[index]:

            if data["username"] == username:

                data["password"] = password_baru

                print("\nPassword berhasil diupdate.")
                return

        print("\nUser tidak ditemukan.")

    # =========================
    # JUMLAH USER
    # =========================
    def size_user(self):

        total = 0

        for bucket in self.table:
            total += len(bucket)

        return total

    # =========================
    # CLEAR TABLE
    # =========================
    def clear(self):

        self.table = [[] for _ in range(self.size)]

        print("\nHash table berhasil dikosongkan.")