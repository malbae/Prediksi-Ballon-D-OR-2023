import random

teams = "=== Program prediksi juara liga inggris tahun 2023 - 2024 ==="
print(teams)

pemain = ('Lionel Messi', 'Erling Haaland', 'Karim Benzema', 'Kylian Mbappe', 'Vinicius Junior')

print("Masukkan nama pemain yang menurut Anda akan menjadi juara Ballon D`Or 2023:")
for i, team in enumerate(pemain):
    print(f"{i+1}. {team}")

prediksi = int(input("Masukkan nama pemain: "))

if prediksi < 1 or prediksi > len(pemain):
    print("Nama pemain yang dimasukkan tidak valid!")
else:
    persentase_prediksi = int(input("Masukkan persentase prediksi juara: "))

    if persentase_prediksi < 1 or persentase_prediksi > 100:
        print("Persentase prediksi tidak valid!")
    else:
        juara = pemain[prediksi - 1]

        print(f"\nBerdasarkan prediksi Anda, {juara} memiliki peluang sebesar {persentase_prediksi}% untuk menjadi juara Liga Inggris tahun ini!")
