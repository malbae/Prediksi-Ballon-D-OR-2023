daftar_barang = {
    "Beras": 10000,
    "Gula": 15000,
    "Minyak Goreng": 20000,
    "Telur": 25000,
    "Daging Ayam": 30000,
    "Sabun": 10000,
    "Shampoo": 15000 
}

print("Selamat Datang Di Program Kasir Swalayan!")
nama = input("Silakan Masukkan Nama Anda: ")
items = []
prices = []
print("Berikut Adalah Daftar Barang Dan Harga:")
for k, v in daftar_barang.items():
 print(f"{k}: Rp {v:,}")
    
while True:
    def inputan():
        print("")
        print("====================================================================================")
        return input("Masukkan nama barang yang ingin Anda beli 'selesai' atau 'kembali' : ")
    item = inputan()
    price = daftar_barang[item]
    quantity = int(input("Masukkan jumlah barang: "))
    items.append(item)
    prices.append(price * quantity)

def print_receipt(items, prices):
    print(f"\n\nNota Pembelian\n-----------------------")
    total = 0
    for i in range(len(items)):
        print("{:<20} {:>2} x Rp {:>6.2f} = Rp {:>8.2f}".format(items[i], prices[i] // daftar_barang[items[i]], daftar_barang[items[i]], prices[i]))
        total += prices[i]
    print("-----------------------")
    print("{:<20} Rp {:>8.2f}".format("Total:", total))

print_receipt(items, prices)

