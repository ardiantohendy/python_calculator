
def penjumlahan(n1, n2):
    result = n1 + n2
    print(f"Hasil {n1} + {n2} = {result}")

    return result

def pengurangan(n1, n2):
    result = n1 - n2
    print(f"Hasil {n1} - {n2} = {result}")

    return result

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
            num1 = int(input("Masukkan angka pertama: "))
            num2 = int(input("Masukkan angka kedua: "))

            if choice == 1:
                penjumlahan(num1,num2)
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