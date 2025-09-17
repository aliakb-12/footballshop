Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).



** PENJELASAN CHECKLIST IMPLEMENTASI **
1. Menjalankan command 'django-admin startproject FootballShop' untuk membuat project baru
2. Di dalam root folder, menjalankan command 'python manage.py startapp main' dan menambahkan 'main' kedalam settings.py INSTALLED_APPS
3. Menambahkan 'main' kedalam settings.py INSTALLED_APPS
4. Di dalam main/modles.py membuat class bernama Product dan isi dengan :     
    CATEGORY_CHOICES = [
    ]

    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices= CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
5. Didalam views.py, membuat fungsi yang bernama show_main yang akan diisi dengan nama,kelas,npm, dan nama aplikasi. Serta fungsi tersebut akan me return template html
6. Didalam main/urls.py Didalam 'main/urls.py', menambahkan routing ke 'main.urls' dengan 'path('', include('main.urls'))'


** BAGAN **
A. CLIENT REQUEST --> B (urls.py)
B --> Jika urlsnya cocok C (views.py)
C --> Jika butuh data D (models.py)
D --> Mengasih data C (views.py)
C --> Merender file HTML (Template HTML)
E --> Respons ke client 

Hubungan antar file
urls.py akan menentukan url untuk masuk menuju fungsi yang mana
views.py akan memutuskan data apa yang perlu ditampilkan
models.py adalah tempat penyimpanan data-data (database)
HTML akan menampilkan aplikasi ke user


** PERAN SETTINGS.py **
untuk menyimpan konfigurasi utama projek Django, seperti:
- Database
- Installed apps
- Middleware
- Template settings
- Static & media files
- Konfigurasi khusus seperti debug mode dan allowed hosts


** MIGRASI DATABASE DI DJANGO **
1. Membuat model baru di models.py
2. Menjalankan perintah python manage.py makemigrations, django membuat file migration
3. Menjalankan python manage.py migrate, perubahan diterapkan ke database
4. Django akan mencatat setiap migrasi yang dilakukan


** MENGAPA DJANGO **
Django memiliki banyak fitur bawaan yang akan memudahkan bagi para pemula
Django memakai bahasa python, yang bisa dibilang lebih gampang untuk dipahami bagi pemula
Dengan belajar django kita akan paham dengan konsep MVC/MVT yang fundamental untuk framework web lainnya


** FEEDBACK UNTUK ASDOS **
belum ada











** TUGAS 3 **
1. Dikarenakan tanpanya data delivery, kita tidak akan bisa mengirim dan menerima data antara sercer dan client side.
contohnya ketika user membuka halaman produk, maka server akan mengirim/deliver data produk ke frontend agar user bisa melihat data-data produk tersebut.

2. Menurut saya json lebih baik, json lebih popular dan lebih baik karena dengan menyimpan data di json akan jauh lebih ringkas dan lebih mudah di baca. Di dalam file xml terdapat tag-tag yang bisa membuat membaca datanya lebih sulit. Json juga bisa dipakai hampir di semua bahasa pemrograman modern, sehingga interoperabilitasnya tinggi.

3. Untuk mengecek apakah daata yang dikirim oleh user melalui form sesua dengan aturan validasi form yang sudah kita bikin. Ketika is_valid() mengembalikan true, maka artinya data yang dimasukkan sesuai dan bisa dimasukkan ke dalam database. Sebaliknya jika is_valid() mengembalikan false, maka django akan mengasih tau user bahwa data yang mereka input itu salah. Kita membutuhkan ini agar bisa memastikan bahwa semua input yang dimasukkan user itu valid dan tidak akan ada input-input yang tidak relevan.

4. csrf_token digunakan untuk melindungi aplikasi dari serangan CSRF. Tanpa adanya csrf_token ini maka akan ada penyerang yang bisa membuat suatu form palsu yang dikirimkan dari situs lain. Form ini akan ditunjukkan kepada user lain, dan bisa memanipulasi data user tersebut tanpa sepengatahuan mereka.

5. 
- Buka main/views.py dan membuat fungi-fungsi untuk show_xml, show_json, show_xml_by_id, show_json_by_id. (bisa dilihat dalam fungsingya didalam main/views.py)
- Didalam url tambahkan path untuk masing masing views
    path('json/', show_json, name='show_json'),
    path('json/<str:product_id>', show_json_by_id, name='show_json_by_id'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:product_id>', show_xml_by_id, name='show_xml_by_id'),
- Didalam templates/main/main.html bikin sebuah button yang bisa dipencet untuk create_product. Ketika button itu dipencet, maka akan ganti kedalam create_product.html yang disana user akan memasukan data-data untuk product tersebut. 
- Didalam forms.py kita buat product form yang digunakan dari modelform. Lalu kita akan masuk ke dalam views.py dan akan membuat create_product serta membuat template create_product.html
- untuk membuat halaman detail kita akan membuat view show_product dan mengirim objek berdasarkan id ke product_detail.html.

6. Mungkin bisa tolong untuk kirimkan foto atau kasih tau eksplisit kepada mahasiswa bagaimana frontend seharusnya terlihat. (atau mungkin bisa kasih tau kalau bebas aja frontendnya yang penting ada hal-hal dalam checkbox)
