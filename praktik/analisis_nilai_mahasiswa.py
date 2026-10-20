
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)
    return lulus


nilai = [59, 60, 61]

banyak_data = len(nilai)
total = sum(nilai)

if banyak_data > 0:
    minimum = min(nilai)
    maksimum = max(nilai)
    rata = rata_rata(nilai)
else:
    minimum = 0
    maksimum = 0
    rata = 0

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Data nilai       : {nilai}")
print(f"Banyak data      : {banyak_data}")
print(f"Total nilai      : {total}")
print(f"Rata-rata        : {rata:.2f}")
print(f"Nilai minimum    : {minimum}")
print(f"Nilai maksimum   : {maksimum}")
print(f"Batas kelulusan  : 60")
print(f"Jumlah lulus     : {jumlah_lulus}")
print(f"Jumlah belum lulus: {jumlah_belum_lulus}")
print(f"Daftar nilai lulus: {lulus}")
