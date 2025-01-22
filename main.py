
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
                result = num1 + num2
                print(f"Hasil {num1} + {num2} = {result}")
            elif choice == 2:
                result = num1 - num2
                print(f"Hasil {num1} - {num2} = {result}")
            elif choice == 3:
                result = num1 * num2 
                print(f"Hasil {num1} x {num2} = {result}")
            elif choice == 4:
                if num2 != 0:
                    result = num1 / num2
                    print(f"Hasil {num1} : {num2} = {result}")
                else:
                    print("Terjadi kesalahan: Pembagian dengan nol tidak diperbolehkan!")
        else:
            print("Pilihan operasi tidak valid!")

    except ValueError:
        print("Anda memasukkan angka yg salah")

calculator()