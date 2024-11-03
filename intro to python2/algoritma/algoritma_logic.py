nilai_raport = 10
#if
#if(kondisi yang di mau)
print("===== Soal 1 =====")
if nilai_raport > 5:
    print("wah nilai saya bagus ni !")

print("===== Soal 2 =====")
#if else
# petik satu itu artinya char karakter
# petik dua itu artinya string
# char nama [12] ini artinya panjang variabel nama max 12 karakter
# char nama [12] berubah jadi char nama[255] --- string
nilai_raport = 'F'
if nilai_raport == 'A' :
    print("Selamat kamu lulus ujian ini !")
else :
    print("Sana kamu remedial lagi !!")
print("===== Soal 3=====")
nilai_raport = 'C'
if nilai_raport == 'A' :
    print("Selamat kamu lulus dengan nilai sempurna !")
elif nilai_raport == 'B' :
    print("Selamat kamu lulus dengan nilai bagus !")
elif nilai_raport == 'C' :
    print("Selamat kamu lulus dengan kurang bagus !")
else :
    print("Mohon maaf kamu harus remedial lagi !")

print("===== Ternary =====")
a = 10
b = 12
bandingkan = "Posisi A Menang" if a > b else "Posisi B Menang"
print(bandingkan)

print("----- if Elfi Else (if Nested / if bersarang) ------")
nilai_raport == 'B'
if nilai_raport == 'A' :
    print("Selamat kamu lulus dengan nilai sempurna !")
elif nilai_raport == 'B' :
    print("Selamat kamu lulus dengan nilai bagus !")
elif nilai_raport == 'C' :
    print("Selamat kamu lulus tapi dengan nilai kurang bagus !")
else :
    print("Mohon maaf kamu harus remedial lagi !")

