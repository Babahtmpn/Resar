import time

class Document:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"{self.name} ({self.pages} halaman)"

class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_rear(self, item):
        self.items.append(item)
    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    def size(self):
        return len(self.items)

printer_queue = Deque()

print("=== Sistem Antrian Printer ===")
while True:
    nama = input("Masukkan nama dokumen (atau ketik 'selesai' untuk mencetak): ")
    if nama.lower() == "selesai":
        break
    try:
        halaman = int(input("Masukkan jumlah halaman: "))
        if halaman <= 0:
            print("Jumlah halaman harus lebih dari 0!")
            continue
        printer_queue.add_rear(Document(nama, halaman))
        print(f"Dokumen '{nama}' telah ditambahkan ke antrian.\n")
    except ValueError:
        print("Jumlah halaman harus berupa angka!\n")

print("\n=== Memulai proses pencetakan ===\n")

if printer_queue.is_empty():
    print("Tidak ada dokumen dalam antrian.")
else:
    while not printer_queue.is_empty():
        dokumen = printer_queue.remove_front()
        if dokumen:
            print(f"Mulai mencetak: {dokumen}")
            for halaman in range(1, dokumen.pages + 1):
                print(f"  Mencetak halaman {halaman} dari {dokumen.pages}...")
                time.sleep(1) 
            print(f"Selesai mencetak {dokumen.name}\n")

    print("Semua dokumen telah dicetak.")
