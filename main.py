
def penjumlahan(nList):
    result = sum(nList)
    print(f"Hasil + {" + ".join(map(str, nList))} = {result}")


def pengurangan(nList):
    result = n1 - n2
    print(f"Hasil + {" - ".join(map(str, nList))} = {result}")

def perkalian(n1, n2):
    result = n1 * n2
    print(f"Hasil {n1} x {n2} = {result}")

    return result

def pembagian(n1, n2):
    if n2 != 0:
        result = n1 / n2
        print(f"Hasil {n1} : {n2} = {result}")
    else:
        print("Terjadi kesalahan: Pembagian dengan nol tidak diperbolehkan!")


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
                pengurangan(num1,num2)
            elif choice == 3:
                perkalian(num1,num2)
            elif choice == 4:
                pembagian(num1,num2)
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


# result = penjumlahan(num1,num2)
#                 print(f"Hasil {num1} + {num2} = {result}")
#                 for i in range(1, 10):
#                     nextChoice = int(input("Lanjutkan?\n1. Iya\n2. Tidak\n "))
#                     if nextChoice != 2:
#                         numN = int(input("Masukan angka selanjutnya: "))
#                         penjumlahan(result, numN)
#                         resultN = penjumlahan(result, numN)
#                         print(f"Hasil {result} + {numN} = {resultN}")
#                     else:
#                         print("Selamat tinggal")
#                         break