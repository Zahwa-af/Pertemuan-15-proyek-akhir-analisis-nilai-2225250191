from src.input_data import baca_data_file
from src.proses import validasi_dan_proses_data, ringkasan_statistik
from src.output import tampilkan_ke_terminal, simpan_laporan_file

def main():
    path_input = "data/contoh_data.txt"
    path_output = "data/laporan_hasil.txt"

    print("Memulai program pengolahan data nilai...")
    mentah = baca_data_file(path_input)

    if not mentah:
        print("Program dihentikan karena data input kosong atau file tidak ditemukan.")
        return

    data_valid = validasi_dan_proses_data(mentah)

    if not data_valid:
        print("Tidak ada data valid yang dapat diproses lebih lanjut.")
        return

    statistik = ringkasan_statistik(data_valid)

    tampilkan_ke_terminal(statistik)
    simpan_laporan_file(path_output, statistik)

if __name__ == "__main__":
    main()