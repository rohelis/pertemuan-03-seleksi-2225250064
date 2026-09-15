print("Analisis Persamaan Kuadrat")
a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    diskriminan = b ** 2 - 4 * a * c
    print(f"Diskriminan = {diskriminan:.2f}")

    if diskriminan > 0:
        print("Persamaan memiliki dua akar real berbeda.")
    elif diskriminan == 0:
        print("Persamaan memiliki satu akar real kembar.")
    else:
        print("Persamaan memiliki dua akar kompleks (tidak real).")