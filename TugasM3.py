def jumlah_hari_dalam_bulan(bulan):
   
    if bulan < 1 or bulan > 12:
        return None 
    jumlah_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return jumlah_hari[bulan - 1]

if __name__ == "__main__":
    try:
        bulan = int(input("Masukkan bulan dalam bentuk angka: "))
        hari = jumlah_hari_dalam_bulan(bulan)

        if hari is None:
            print("Bulan tidak valid.")
        else:
            print("Jumlah hari:", hari)

    except ValueError:
        print("Input tidak valid. Masukkan angka antara 1 sampai 12.")


