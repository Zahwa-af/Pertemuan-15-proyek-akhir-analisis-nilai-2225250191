# Dokumentasi Test Case Proyek Akhir

| ID | Fitur | Input / Kondisi | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC01** | Rata-rata & Normal | Nilai normal `85, 78, 92` | Menghitung rata-rata dengan benar | Sesuai perhitungan | **PASS**[cite: 78] |
| **TC02** | Batas Kelulusan | Nilai tepat batas `60` | Dikategorikan sebagai "Tuntas" | Tuntas | **PASS**[cite: 78] |
| **TC03** | Validasi Invalid | Input huruf `"abc"` | Dilewati dan memunculkan peringatan | Peringatan tampil | **PASS**[cite: 78] |
| **TC04** | Validasi Rentang | Input nilai `105` | Ditolak karena di atas 100 | Ditolak | **PASS**[cite: 78] |
| **TC05** | Penanganan File | File input tidak tersedia | Menangkap `FileNotFoundError` dengan aman | Aman, tidak crash | **PASS**[cite: 78] |