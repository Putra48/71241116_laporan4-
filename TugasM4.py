def sisi_segitiga(sisi_1, sisi_2, sisi_3):

    if sisi_1 == sisi_2 == sisi_3:
        print("Semua sisi sama")
    elif sisi_1 == sisi_2 or sisi_1 == sisi_3 or sisi_2 == sisi_3:
        print("Ada 2 sisi yang sama")
    else:
        print("Tidak ada sisi yang sama")

if __name__ == "__main__":
    try:
        sisi_1 = float(input("Masukan angka untuk sisi 1: "))
        sisi_2 = float(input("Masukan angka untuk sisi 2: "))
        sisi_3 = float(input("Masukan angka untuk sisi 3: "))
    
        sisi_segitiga(sisi_1, sisi_2, sisi_3)

    except ValueError:
        print("Anda salah memasukan input, Tolong masukan input kembali dengan benar")
    
