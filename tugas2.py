kontak = {}

def tampilkan_menu():
    print("\n=== Menu Kontak ===")
    print("1. Tambahkan Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama kontak: ").lower()
        nomor = input("Masukkan nomor telepon: ")
        kontak[nama] = nomor
        print(f"kontak '{nama}' berhasil ditambahkan.")

    elif pilihan == "2":
        nama = input("Masukkan nama kontak yang ingin dihapus: ").lower()
        if nama in kontak:
            del kontak[nama]
            print(f"kontak '{nama}' berhasil dihapus.")
        else:
            print(f"kontak '{nama}' tidak ditemukan.")

    elif pilihan == "3":
        nama = input("Masukkan kontak yang ingin dicari: ").lower()
        if nama in kontak:
            print(f"Nomor telepon '{nama}': {kontak[nama]}")
        else:
            print(f"kontak '{nama}' tidak ditemukan.")

    elif pilihan == "4":
        if not kontak:
            print("Belum ada kontak yang tersimpan.")
        else:
            print("\nDaftar kontak: ")
            for nama, nomor in kontak.items():
                print(f"- {nama.capitalize()}: {nomor}")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak ada. silahkan ppilih menu yang di tentukan.")