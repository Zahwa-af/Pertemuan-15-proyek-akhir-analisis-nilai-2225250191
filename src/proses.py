BATAS_KKM = 60

def hitung_rata_rata(nilai):
    """Mengembalikan rata-rata list numerik, mengembalikan 0 jika kosong."""
    if not nilai:
        return 0
    return sum(nilai) / len(nilai)

def status_lulus(nilai, batas=BATAS_KKM):
    """Menentukan daftar nilai yang memenuhi batas kelulusan."""
    return [x for x in nilai if x >= batas]

def validasi_dan_proses_data(data_mentah):
    """Memvalidasi format data dan rentang nilai 0-100."""
    data_valid = []
    for nomor, baris in data_mentah:
        pecah = baris.split(",")
        if len(pecah) != 3:
            print(f"Peringatan: Baris {nomor} format salah -> {baris}")
            continue

        nim, nama, teks_nilai = pecah
        try:
            nilai = float(teks_nilai.strip())
            # Validasi batas rentang nilai 0 - 100
            if not (0 <= nilai <= 100):
                print(f"Peringatan: Baris {nomor} nilai di luar rentang (0-100) -> {baris}")
                continue

            status = "Tuntas" if nilai >= BATAS_KKM else "Belum Tuntas"
            data_valid.append({
                "nim": nim.strip(),
                "nama": nama.strip(),
                "nilai": nilai,
                "status": status
            })
        except ValueError:
            print(f"Peringatan: Baris {nomor} nilai bukan angka valid -> {baris}")

    return data_valid

def ringkasan_statistik(data_valid):
    """Menghitung ringkasan statistik kelas secara lengkap."""
    if not data_valid:
        return None

    nilai_list = [item["nilai"] for item in data_valid]
    lulus_list = status_lulus(nilai_list)

    return {
        "jumlah": len(nilai_list),
        "rata_rata": hitung_rata_rata(nilai_list),
        "minimum": min(nilai_list) if nilai_list else None,
        "maksimum": max(nilai_list) if nilai_list else None,
        "jumlah_tuntas": len(lulus_list),
        "jumlah_belum_tuntas": len(nilai_list) - len(lulus_list)
    }