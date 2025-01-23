
def penjumlahan(nList):
    result = sum(nList)
    print(f"Hasil {" + ".join(map(str, nList))} = {result}")


def pengurangan(nList):
    result = nList[0]
    for num in nList[1:]:
        result -= num
    print(f"Hasil {" - ".join(map(str, nList))} = {result}")

def perkalian(nList):
    result = nList[0]
    for num in nList[1:]:
        result *= num
    print(f"Hasil {" x ".join(map(str, nList))} = {result}")


def pembagian(nList):
    try:  
        if 0 in nList[1:]:
            print("Terjadi kesalahan: Pembagian dengan nol tidak diperbolehkan!")
            return

        result = nList[0]
        for num in nList[1:]:
            result /= num
        print(f"Hasil {" / ".join(map(str, nList))} = {result}")

    except ZeroDivisionError:
        print("Pembagian dengan nol tidak diperbolehkan!")


def calculator():
    print("=== Calculator Sederhana ===")
    print("Pilih Operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (x)")
    print("4. Pembagian (:)")


    try:
        choice = int(input("Masukkan pilihan operasi (1,2,3,4): "))

        if choice in [1,2,3,4]:
            numbers = input("Masukkan angka-angka yg ingin dijumlahkan dan tolong pisahkan dengan koma contoh (10,99,19): ")
            num_list = [float(num) for num in numbers.split(",")]

            if len(num_list) < 2:
                print("Harap masukkan paling tidak dua angka!")
                return

            if choice == 1:
                penjumlahan(num_list)
            elif choice == 2:
                pengurangan(num_list)
            elif choice == 3:
                perkalian(num_list)
            elif choice == 4:
                pembagian(num_list)
        else:
            print("Pilihan operasi tidak valid!")
            choice = int(input("Apakah anda ingin mencoba lagi?\n1. Coba lagi\n2. Keluar\n "))

            if choice != 2:
                calculator()
            else:
                print("Selamat Tinggal")    

    except ValueError:
        print("Anda memasukkan angka yg salah")

calculator()


