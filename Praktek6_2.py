print("masukan angka di luar bulan untuk berhenti")
hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def LeapYearCheck(tahun):
    if tahun % 4 == 0:
        return 29
    else:
        return 28
            
def HitungHari(bulan):
    if bulan == 2:
        tahun = int(input("tahun: "))
        return LeapYearCheck(tahun)
    else:
        return hari[bulan-1]

while True:
    bulan = int(input("bulan (1-12): "))
    if bulan < 1 or bulan > 12:
        print("bye bye :3")
        break
    else:
        print(HitungHari(bulan), "hari dalam bulan tersebut")