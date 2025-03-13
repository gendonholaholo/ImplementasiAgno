**Agno Web Application**
**Pendahuluan**
Aplikasi ini adalah implementasi sederhana dari **Agno**, menggunakan **FastAPI** untuk backend dan **React** untuk frontend. Backend memproses teks menggunakan Agno dan frontend menyediakan antarmuka pengguna.
**Struktur Direktori**
agno-app/
│── backend/                   # Backend menggunakan FastAPI
│   ├── main.py                # Entry point backend
│   ├── database.py             # Koneksi database
│   ├── config.py               # Konfigurasi backend
│   ├── api/
│   │   ├── routes.py           # Routing API
│   │   ├── models.py           # Model database
│   │   ├── agno\_handler.py     # Integrasi Agno
│   ├── requirements.txt        # Dependencies backend
│── frontend/                   # Frontend menggunakan React
│   ├── src/
│   │   ├── components/        # Komponen UI
│   │   ├── pages/             # Halaman utama
│   │   ├── services/          # API handler
│   │   ├── App.jsx            # Root React App
│   ├── public/
│   ├── package.json           # Dependencies frontend
│── database/                  # Database setup
│   ├── schema.sql             # Skema database
│   ├── migrations/            # Folder untuk migrasi database
│── docs/                      # Dokumentasi proyek
│   ├── architecture.md        # Arsitektur sistem
│   ├── api-docs.md            # Dokumentasi API
│── .env                       # Environment variables
│── docker-compose.yml         # File Docker untuk deploy
│── README.md                  # Dokumentasi utama proyek
**Instalasi & Menjalankan Aplikasi**
**Menjalankan Backend**
```
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```
Cek API di browser atau Postman:

http://127.0.0.1:8000/
**Menjalankan Frontend**
```
cd frontend

npm install

npm run dev
```
Akses frontend di browser:

http://localhost:5173/
**API Endpoint**

|**Endpoint**|**Method**|**Deskripsi**|
| :-: | :-: | :-: |
|/|GET|Cek status API|
|/process-agno|POST|Memproses teks menggunakan Agno|

Contoh request:

curl -X POST "http://127.0.0.1:8000/process-agno" \

`     `-H "Content-Type: application/json" \

`     `-d '{"input\_text": "Hello Agno"}'
**🛠 Debugging**
Jika ada error saat menjalankan backend, coba:

pip install psycopg2-binary

Jika frontend error karena package hilang, jalankan:
```
npm install react-router-dom axios
```

-----
~Mas Gendon
