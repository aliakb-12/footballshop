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






