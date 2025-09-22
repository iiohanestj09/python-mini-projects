### Tahapan-tahapan:
- `import random` untuk 2 versi generator
- input panjang Password
    1. Versi 1:
        - `import math`
        - inisialisasi 3 variabel untuk alfabet, angka dan karakter spesial
        - panjang password = pakai formula 50% alfabet - 30% angka - 20% karakter 
        - bikin fungsi `generatePassword`
        - panggil fungsi `generatePassword` untuk 3 jenis tadi bertahap
        - shuffle atau acak elemen di dalam password
        - join password dari list -> string
    
    2. Versi 2:
        - `import string`
        - inisialisasi `total` dari gabungan
            * string.ascii_letters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
            * string.digits = 0123456789
            * string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        - ambil sample dari `total` dengan panjang inputan di awal
        - karena `random.sample` mengembalikkan list, maka kita harus join dari list -> string
