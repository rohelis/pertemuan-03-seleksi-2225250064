# Pertemuan 03 Seleksi Python

Nama: Rohelis
NIM: 2225250064
Kelas: 3B

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan
python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
1. Menerima masukan dari pengguna berupa koefisien a, b, dan c sebagai bilangan desimal (float).
2. Memeriksa apakah nilai a bernilai 0. Jika ya, tampilkan pesan bahwa input bukan persamaan kuadrat.
3. Jika nilai a bukan 0, hitung nilai diskriminan D menggunakan rumus D = b^2 - 4ac, lalu tampilkan nilainya.
4. Mengevaluasi nilai D menggunakan struktur nested if:
   - Jika D > 0, hitung dua akar real berbeda (x1 dan x2) menggunakan rumus kuadratik lalu tampilkan hasilnya.
   - Jika D == 0, hitung satu akar real kembar (x) lalu tampilkan hasilnya.
   - Jika D < 0, tampilkan pesan bahwa tidak ada akar real.
5. Format semua output angka desimal agar menampilkan dua angka di belakang koma.

## Hasil Pengujian
| Skenario | Input (a, b, c) | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|---|
| Bukan Kuadrat | 0, 2, 4 | Bukan persamaan kuadrat. | Bukan persamaan kuadrat. | Berhasil |
| Dua Akar Berbeda | 1, -5, 6 | Diskriminan = 1.00<br>Dua akar real berbeda: x1 = 3.00, x2 = 2.00 | Diskriminan = 1.00<br>Dua akar real berbeda: x1 = 3.00, x2 = 2.00 | Berhasil |
| Akar Kembar | 1, -4, 4 | Diskriminan = 0.00<br>Satu akar real kembar: x = 2.00 | Diskriminan = 0.00<br>Satu akar real kembar: x = 2.00 | Berhasil |
| Tidak Ada Akar | 1, 2, 5 | Diskriminan = -16.00<br>Tidak ada akar real. | Diskriminan = -16.00<br>Tidak ada akar real. | Berhasil |

## Refleksi
Kesalahan logika yang sempat ditemukan adalah lupa menambahkan tanda kurung pada pembagi rumus kuadratik, yaitu `(-b + diskriminan ** 0.5) / 2 * a`. Hal ini membuat Python membagi dengan 2 terlebih dahulu baru mengalikannya dengan a. 

Cara memperbaikinya adalah dengan membungkus penyebut dengan tanda kurung menjadi `/(2 * a)` sehingga perhitungan $2a$ diselesaikan lebih dulu sebagai pembagi yang utuh.