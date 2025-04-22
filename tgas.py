kamus = {
    "kucing": "hewan peliharaan yang lucu",
    "anjing": "hewan peliharaan yang setia kepada majikan nya",
    "durian": "buah yang memiliki kulit yang berduri dan bau yang menyengat",
}

print("=== kamus sederhana ===")
print("ketik (keluar) untuk mengakhiri program. \n")

while True:
    kata = input("Masukkan kata yang ingin dicari artinya: ").lower()

    if kata == "keluar":
        print("Terimakasih telah menggunakn kamus.")
        break

    if kata in kamus:
        print(f"Arti kata '{kata}' adalah: {kamus[kata]}\n")
    else:
        print(f"Maaf, kata '{kata}' tidak ditemukan dalam kamus. \n")
