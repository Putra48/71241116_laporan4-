# soal 4.1
try:
    suhu = int(input("Masukkan suhu tubuh: ")) 

    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")

except ValueError:
    print("Anda salah memasukan input, tolong masukan input yang benar kembali ")

# soal 4.2
try:
    bilangan = int(input("Masukkan suatu bilangan: "))
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")

except ValueError:
    print("Eror, coba masukan input dengan benar")

# soal 4.3
try:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    c = int(input("Masukkan bilangan ketiga: "))

    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)

except ValueError:
    print("Input kamu salah, coba lagi ")
