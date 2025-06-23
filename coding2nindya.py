# Aplikasi Hitung Luas Trapesium
print("Halo Semuanya!")
print("="*45)
print("\nSelamat Datang di Aplikasi Hitung Luas Trapesium")
tujuan = input("\nApa tujuan kamu kesini? ")
print("Baik, Saya akan membantu anda", tujuan)
print("Silahkan Isi Pertanyaan di bawah ini dengan Bilangan")
try:
    Alas_A = float(input("Masukkan Alas A = "))
    Alas_B = float(input("Masukkan Alas B = "))
    Tinggi = float(input("Masukkan Tinggi = "))
    Luas = 1/2*(Alas_A + Alas_B)*Tinggi
    print("Jadi luas trapesiumnya adalah = %.2f cm²" %(Luas))
    print("="*45)
except ValueError:
    print("\nInput tidak valid. Pastikan hanya memasukkan angka.")
