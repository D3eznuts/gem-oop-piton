# 🖥️ TechMaster Inventory System

> 🔥 Advanced OOP Project (4 Pilar OOP)\
> Sistem manajemen inventaris toko elektronik berbasis Python.

---

## 📌 Deskripsi

**TechMaster** adalah sistem backend sederhana untuk mengelola stok dan
transaksi barang elektronik seperti **Laptop** dan **Smartphone**.

Project ini dibuat untuk mengimplementasikan konsep **Object-Oriented
Programming (OOP)** secara lengkap dan terstruktur.

---

## 🧠 Implementasi 4 Pilar OOP

### 1️⃣ Abstraction

- Menggunakan `Abstract Base Class (ABC)`
- Class `BarangElektronik` tidak bisa dibuat objek langsung
- Memiliki abstract method:
  - `tampilkan_detail()`
  - `hitung_harga_total(jumlah)`

---

### 2️⃣ Encapsulation

- Atribut sensitif dibuat **private**

  ```python
  __stok
  __harga_dasar
  ```

- Akses melalui:
  - `get_stok()`
  - `get_harga_dasar()`
  - `tambah_stok(jumlah)` dengan validasi

🛡️ **Stok tidak bisa negatif (data aman).**

---

### 3️⃣ Inheritance

Class turunan dari `BarangElektronik`:

- 💻 `Laptop`
- 📱 `Smartphone`

Masing-masing memiliki: - Atribut tambahan berbeda - Persentase pajak
berbeda

---

### 4️⃣ Polymorphism

Method dioverride pada masing-masing class:

```python
tampilkan_detail()
hitung_harga_total()
```

Fungsi global:

```python
proses_transaksi(daftar_barang)
```

Dapat menerima campuran objek Laptop & Smartphone dalam satu list.

---

## 🏗️ Struktur Project

    TechMaster/
    │
    ├── inventaris.py
    ├── README.md
    └── assets/
        ├── setup-data.png
        └── struk-transaksi.png

---

## 🖼️ Tampilan Output Program

Tambahkan screenshot hasil run program ke folder `assets/` lalu gunakan:

```markdown
![Setup Data](assets/setup-data.png)

![Struk Transaksi](assets/struk-transaksi.png)
```

---

## 🚀 Cara Menjalankan Program

1.  Pastikan Python 3 sudah terinstall
2.  Jalankan perintah berikut di terminal:

```bash
python inventaris.py
```

---

## 🎯 Fitur Utama

✔ Validasi stok (tidak bisa negatif)\
✔ Perhitungan pajak otomatis\
✔ Multi tipe barang\
✔ Struktur OOP clean & modular\
✔ Mudah dikembangkan

---

## 🔥 Highlight Project

⭐ Implementasi 4 Pilar OOP Lengkap\
⭐ Abstract Class (Level Advanced)\
⭐ Private Attribute + Getter/Setter\
⭐ Method Overriding (Polymorphism)\
⭐ Struktur kode rapi & scalable

---

## 📈 Pengembangan Selanjutnya

- 🔄 Pengurangan stok otomatis saat transaksi
- 💳 Sistem pembayaran
- 📊 Laporan penjualan
- 🗂 Integrasi database (SQLite/MySQL)
- 🖥 GUI atau Web App (Flask)

---

## 👨‍💻 Author

Project dibuat untuk memenuhi tugas **Challenge OOP Advanced -- Sistem
Manajemen Inventaris TechMaster**.
