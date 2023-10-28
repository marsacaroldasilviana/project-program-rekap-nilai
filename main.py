# Fungsi pertama: Mengambil input dari pengguna berupa nama mata pelajaran dan nilai KKM
def input_data_matapelajaran():
    print("Rekap Nilai Siswa")
    print("=========================================")
    # Perulangan yang terus berjalan hingga kondisi tertentu terpenuhi
    while True:
        matapelajaran = input("Masukkan nama mata pelajaran: ")
        # Percabangan yang memeriksa apakah pengguna telah memasukkan nama mata pelajaran atau tidak
        if matapelajaran:
            # Perulangan untuk memeriksa apakah input KKM adalah angka
            while True:
                try:
                    kkm = float(input(f"Masukkan nilai KKM untuk mata pelajaran {matapelajaran}: "))
                    break
                except ValueError:
                    print("KKM harus berupa angka. Coba lagi.")
            return matapelajaran, kkm

# Fungsi kedua: Mengambil input dari pengguna berupa data siswa
def input_data_siswa(matapelajaran):
    siswa = {}
    print("\nMasukkan data siswa (ketik 'selesai' untuk mencetak):")
    # Perulangan yang terus berjalan hingga pengguna memasukkan "selesai" sebagai nama siswa
    while True:
        nama_siswa = input("Nama siswa: ")
        # Percabangan yang memeriksa apakah pengguna ingin mengakhiri penginputan data siswa.
        if nama_siswa.lower() == 'selesai':
            break
        # Perulangan untuk memeriksa apakah input nilai siswa adalah angka
        while True:
            try:
                nilai = float(input(f"Masukkan nilai {matapelajaran} untuk siswa {nama_siswa}: "))
                siswa[nama_siswa] = nilai
                break
            except ValueError:
                print("Nilai harus berupa angka. Coba lagi.")
    return siswa

# Fungsi ketiga: Mencetak rekap nilai siswa untuk mata pelajaran tersebut
def cetak_rekap_nilai(siswa, matapelajaran, kkm):
    print(f"\nRekap Nilai Mata Pelajaran {matapelajaran} (KKM = {kkm}):")
    # Perulangan yang terus berjalan pada setiap siswa untuk mencetak rekap nilai mereka.
    for nama_siswa, nilai in siswa.items():
        status = "Lulus" if nilai >= kkm else "Tidak Lulus"
        print(f"- {nama_siswa} = {nilai}")
        print(f"Status: {status}")
        # Percabangan yang memeriksa rentang nilai dan mencetak keterangan nilai yang sesuai berdasarkan nilai siswa
        if nilai >= 90:
            print("Keterangan Nilai: A")
        elif nilai >= 80:
            print("Keterangan Nilai: B")
        elif nilai >= 70:
            print("Keterangan Nilai: C")
        elif nilai >= 60:
            print("Keterangan Nilai: D")
        else:
            print("Keterangan Nilai: E")
    print()

# Perulangan untuk mengulangi proses input dan pencetakan rekap nilai
while True:
    matapelajaran, kkm = input_data_matapelajaran()
    if matapelajaran.lower() == 'selesai':
        break
    siswa = input_data_siswa(matapelajaran)
    cetak_rekap_nilai(siswa, matapelajaran, kkm)

