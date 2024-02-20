def hitung_berat_badan(tinggi, bmi):
    berat = bmi * (tinggi ** 2)
    return berat

tinggi = float(input("Masukkan tinggi badan Anda (meter): "))
bmi = float(input("Masukkan nilai Body mass Index yang diinginkan: "))

print(f"Berat badan yang diperlukan untuk mencapai Body Mass Index seperti yang di inginkan, berat badan harus mencapai {hitung_berat_badan(tinggi, bmi)} kg")