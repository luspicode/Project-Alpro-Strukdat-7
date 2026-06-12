# =====================================
# hashtable.py
# Hash Table untuk Login Admin
# =====================================

class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, username, password, role):
        index = self.hash_function(username)

        for data in self.table[index]:
            if data["username"] == username:
                print("\nUsername sudah digunakan.")
                return False  # konsisten return False (bukan None)

        user = {
            "username": username,
            "password": password,
            "role": role
        }
        self.table[index].append(user)
        return True  # return True kalau berhasil (tanpa print di sini)

    def login(self, username, password):
        index = self.hash_function(username)

        for data in self.table[index]:
            if (
                data["username"] == username and
                data["password"] == password
            ):
                return data

        return None

    def delete(self, username):
        index = self.hash_function(username)

        for i, data in enumerate(self.table[index]):
            if data["username"] == username:
                del self.table[index][i]
                print("\nUser berhasil dihapus.")
                return

        print("\nUser tidak ditemukan.")

    def tampil_admin(self):
        print("\n========== DATA ADMIN YANG SUDAH TERDAFTAR ==========")
        kosong = True

        for bucket in self.table:
            for data in bucket:
                kosong = False
                print(f"\nUsername : {data['username']}\n----------------------------------")

        if kosong:
            print("Belum ada admin terdaftar.")

    def cari_user(self, username):
        index = self.hash_function(username)

        for data in self.table[index]:
            if data["username"] == username:
                return data

        return None

    def update_password(self, username, password_baru):
        index = self.hash_function(username)

        for data in self.table[index]:
            if data["username"] == username:
                data["password"] = password_baru
                print("\nPassword berhasil diupdate.")
                return

        print("\nUser tidak ditemukan.")

    def size_user(self):
        total = 0
        for bucket in self.table:
            total += len(bucket)
        return total

    def clear(self):
        self.table = [[] for _ in range(self.size)]
        print("\nHash table berhasil dikosongkan.")
