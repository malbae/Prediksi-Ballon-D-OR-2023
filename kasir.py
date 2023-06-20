print("=== Program Kasir Swalayan ===")
def main():
    items = []
    prices = []
    while True:
        item = input("Masukkan nama belanja anda (atau 'selesai' untuk menyelesaikan order): ")
        if item == 'selesai':
            break
        price = float(input("Masukkan harga barang: "))
        items.append(item)
        prices.append(price)
    print_receipt(items, prices)

def print_receipt(items, prices):
    print("\n\nNota Pembelian\n-----------------------")
    total = 0
    for i in range(len(items)):
        print("{:<20} ${:>6.2f}".format(items[i], prices[i]))
        total += prices[i]
    print("-----------------------")
    print("{:<20} ${:>6.2f}".format("Total:", total))

if __name__ == '__main__':
    main()
