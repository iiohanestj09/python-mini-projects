### Convert JSON file to CSV

1. JSON (JavaScript Object Notation)
adalah format berbais teks yg digunakan utk menyimpan struktur data dalam bentuk objek

2. CSV (Comma-Separated Values)
adalah format sederhana untuk menyimpan data tabular (seprti spreadsheet). Setiap baris mewakili satu record, dan setiap kolom dipisahkan oleh koma

Untuk permulaan, `pip install json`

### Tahapan-tahapan:
- Bikin file input.json berisi 3 object yang di dalamnya menyimpan nama, umur dan tahunLahir
- Open file input.json dengan tipe `'r'`
- selanjutnya, `output` menyimpan key object pertama
- lalu `output` menyimpan values dari object 1,2,3
- Terakhir, open file output.csv dengan tipe `'w'`
- Masukkan/menulis `output` ke file output.csv