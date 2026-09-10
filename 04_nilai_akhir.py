nama = input("Masukkan nama:Siti Rohmah ")
nilai_tugas = float(input("Masukkan nilai tugas:80 "))
nilai_uts = float(input("Masukkan nilai UTS:80 "))
nilai_uas = float(input("Masukkan nilai UAS:80 "))

BOBOT_TUGAS = 0.20
BOBOT_UTS = 0.30
BOBOT_UAS = 0.50

nilai_akhir = (nilai_tugas * BOBOT_TUGAS) + (nilai_uts * BOBOT_UTS) + (nilai_uas * BOBOT_UAS)

print()
print("HASIL NILAI AKHIR")
print(f"Nama       : {nama}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")