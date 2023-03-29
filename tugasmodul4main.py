from tugasmodul4 import *

# Program utama
while True:
    print("\n=== MENU ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Daftar Buku")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")
    
    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        tampilkan_daftar_buku()
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid.")
