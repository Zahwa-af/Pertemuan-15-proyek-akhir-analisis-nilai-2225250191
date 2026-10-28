# Program Analisis dan Rekap Nilai Siswa

## Deskripsi
Aplikasi berbasis konsol Python untuk membantu guru atau pengajar membaca data nilai siswa dari file teks, melakukan validasi rentang nilai 0-100, menghitung statistik kelas (rata-rata, min, max, ketuntasan), serta menyimpan laporan hasil rekap secara otomatis[cite: 76, 77].

## Fitur Utama
- **File Reader:** Membaca data eksternal dengan pengaman error file hilang[cite: 72, 75, 78].
- **Data Validation:** Menyaring format baris salah serta menolak input angka di luar rentang atau berupa huruf[cite: 76, 78].
- **Statistical Processing:** Menghitung rata-rata, nilai minimum, maksimum, serta klasifikasi kelulusan berdasarkan KKM[cite: 76, 77].
- **Automatic Reporter:** Mencetak laporan akhir ke file teks `data/laporan_hasil.txt`.

## Persyaratan Sistem
- Python 3.x[cite: 79]

## Cara Menjalankan Program
Jalankan perintah berikut melalui terminal di root folder proyek[cite: 79]:
```bash
python3 main.py