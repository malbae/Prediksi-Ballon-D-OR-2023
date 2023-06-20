daftar_barang = {
    "Beras": 10000,
    "Gula": 15000,
    "Minyak Goreng": 20000,
    "Telur": 25000,
    "Daging Ayam": 30000,
    "Sabun": 10000,
    "Shampoo": 15000
}

print("Selamat datang di Program Kasir Swalayan!")
nama = input("Silakan masukkan nama Anda: ")
items = []
prices = []

while True:
    print("Berikut adalah daftar barang dan harga:")
    for k, v in daftar_barang.items():
        print(f"{k}: Rp {v:,}")
    item = input("Masukkan nama barang yang ingin Anda beli (atau 'selesai' untuk menyelesaikan order): ")
    if item == 'selesai':
        break
    if item not in daftar_barang:
        print("Barang yang Anda masukkan tidak tersedia.")
        continue
