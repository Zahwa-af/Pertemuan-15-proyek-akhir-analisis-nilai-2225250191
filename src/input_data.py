def baca_data_file(nama_file):
    """Membaca data baris demi baris dari file teks eksternal."""
    data_mentah = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue  # Lewati baris kosong
                data_mentah.append((nomor, baris))
    except FileNotFoundError:
        print(f"[ERROR] File '{nama_file}' tidak ditemukan.")
    return data_mentah