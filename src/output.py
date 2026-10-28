def tampilkan_ke_terminal(statistik):
    """Menampilkan ringkasan hasil analisis ke layar terminal."""
    print("=" * 45)
    print("      LAPORAN REKAP & ANALISIS NILAI SISWA")
    print("=" * 45)
    print(f"Jumlah Siswa Valid   : {statistik['jumlah']}")
    print(f"Nilai Rata-rata      : {statistik['rata_rata']:.2f}")
    print(f"Nilai Minimum        : {statistik['minimum']:.2f}")
    print(f"Nilai Maksimum       : {statistik['maksimum']:.2f}")
    print(f"Jumlah Tuntas        : {statistik['jumlah_tuntas']}")
    print(f"Jumlah Belum Tuntas  : {statistik['jumlah_belum_tuntas']}")
    print("=" * 45)

def simpan_laporan_file(nama_file, statistik):
    """Menyimpan laporan ringkasan ke file teks keluaran."""
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write("LAPORAN REKAP & ANALISIS NILAI SISWA\n")
            file.write("-" * 40 + "\n")
            file.write(f"Jumlah Siswa Valid   : {statistik['jumlah']}\n")
            file.write(f"Nilai Rata-rata      : {statistik['rata_rata']:.2f}\n")
            file.write(f"Nilai Minimum        : {statistik['minimum']:.2f}\n")
            file.write(f"Nilai Maksimum       : {statistik['maksimum']:.2f}\n")
            file.write(f"Jumlah Tuntas        : {statistik['jumlah_tuntas']}\n")
            file.write(f"Jumlah Belum Tuntas  : {statistik['jumlah_belum_tuntas']}\n")
        print(f"[SUKSES] Laporan berhasil disimpan ke '{nama_file}'.")
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan file: {e}")