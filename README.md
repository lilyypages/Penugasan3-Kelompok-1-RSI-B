# 🗂️ Penugasan Praktikum 3 RSI – Penugasan Backend: Authentication & Authorization
Repo ini dibuat untuk memenuhi **Penugasan Praktikum 3**

---

## 👥 Anggota Kelompok

| No | Nama | NIM |
|----|------|-----|
| 1 | Stefani Ayudya Prasetyo | L0224011 |
| 2 | Jocelyn Louisa | L0224034 |
| 3 | Talitha Sukma Mahardika | L0224037 |
| 4 | Adrian Farrel Aziz Yatyoga | L0224040 |

---

# Penugasan 3 – Authentication & Authorization

Repositori ini berisi pengembangan lanjutan dari sistem backend dengan fokus pada implementasi keamanan (security) dan kontrol akses pengguna menggunakan JWT dan RBAC.

## 📌 Fitur Utama

### 🔐 1. Implementasi Hashing Password
Keamanan data pengguna menjadi prioritas utama:
- Password tidak disimpan dalam bentuk *plain text*.
- Menggunakan library **argon2** untuk proses hashing.
- Hashing dilakukan secara otomatis pada saat registrasi pengguna baru.

### 🔑 2. Endpoint Login & JWT Authentication
Mekanisme autentikasi untuk verifikasi identitas:
- Endpoint Login memvalidasi kredensial (email/username dan password).
- Jika valid, sistem menghasilkan **JSON Web Token (JWT)** sebagai *access token*.
- Token digunakan untuk mengautentikasi setiap permintaan ke endpoint yang dilindungi.

### 🛡️ 3. Proteksi Endpoint (Authorization)
Membatasi akses API agar hanya dapat digunakan oleh pengguna sah:
- Endpoint CRUD (dari Penugasan 2) kini bersifat *protected*.
- Setiap request wajib menyertakan header:
  `Authorization: Bearer <access_token>`
- Akses akan ditolak dengan status **401 Unauthorized** jika token tidak valid atau tidak disertakan.

### 👑 4. Role-Based Access Control (RBAC)
Pembatasan hak akses berdasarkan peran pengguna:
- **Admin**: Memiliki akses penuh (Full Access) terhadap data Event (Create, Read, Update, Delete).
- **User**: Akses terbatas, hanya dapat melihat (Read) data Event dan melakukan pendaftaran (POST Registration).

### 📸 5. Dokumentasi API (Swagger)
Seluruh endpoint dapat diuji melalui UI Swagger di `/docs`:
- Dokumentasi mencakup skenario **Success** dan **Failed** untuk setiap endpoint.
- Screenshot hasil pengujian telah dikompilasi dalam file PDF pendukung.

---

## 🔁 Integrasi Sistem
Proyek ini mengintegrasikan fitur keamanan ke dalam struktur backend yang sudah ada:
1. **Layered Architecture**: Tetap menggunakan pola *Repository, Service, Controller,* dan *DTO*.
2. **Seamless Update**: Menambahkan middleware keamanan tanpa merusak logika bisnis yang sudah ada.
3. **Data Integrity**: Memastikan data event tetap konsisten sambil membatasi siapa yang bisa memodifikasinya.

--- 

## 🔧 Panduan Git untuk Anggota

> Gunakan **Git Bash** untuk semua perintah berikut.

### 1. Clone Repository *(sekali saja di awal)*
```bash
git clone https://github.com/lilyypages/Penugasan3-Kelompok-1-RSI-B.git
cd Penugasan3-Kelompok-1-RSI-B
```

### 2. Buat Branch Pribadi
```bash
git checkout -b nama-kamu   # contoh: git checkout -b ian
```

### 3. Sebelum Mulai Kerja — Selalu Pull Dulu
```bash
git pull origin main
```

### 4. Simpan Perubahan
```bash
git add .
git commit -m "ubah frontend"
git push -u origin nama-kamu
```

### 5. Buat Pull Request (PR)
- Buka repo di GitHub
- Klik **"Compare & Pull Request"**
- Isi deskripsi → klik **Create Pull Request**

---
