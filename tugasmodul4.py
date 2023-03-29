# Kelas Buku
class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    # Method untuk menampilkan informasi buku
    def tampilkan_info(self):
        print("Judul\t\t:", self.judul)
        print("Penulis\t\t:", self.penulis)
        print("Tahun Terbit\t:", self.tahun_terbit)

# Fungsi untuk menambahkan buku ke dalam list buku
def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    tahun_terbit = input("Masukkan tahun terbit: ")
    buku_baru = Buku(judul, penulis, tahun_terbit)
    list_buku.append(buku_baru)
    print("Buku berhasil ditambahkan.")
    return buku_baru

# Fungsi untuk menampilkan daftar buku
def tampilkan_daftar_buku():
    if list_buku:
        print("Daftar Buku:")
        for buku in list_buku:
            buku.tampilkan_info()
            print("==============================")
    else:
        print("Tidak ada buku yang tersimpan.")

# List untuk menyimpan objek buku
list_buku = []
