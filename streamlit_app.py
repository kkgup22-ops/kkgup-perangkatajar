import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Penyusun Modul SD", page_icon="🏫", layout="wide")

# --- DATABASE MATERI SD (CONTOH) ---
DATABASE_MATERI = {
    "Bahasa Indonesia": {
        "A (Kelas 1-2)": ["Mengenal Huruf & Suku Kata", "Membaca Kalimat Sederhana", "Menulis Nama Benda"],
        "B (Kelas 3-4)": ["Ide Pokok Paragraf", "Wawancara Sederhana", "Menulis Narasi"],
        "C (Kelas 5-6)": ["Teks Eksplanasi", "Pidato & Presentasi", "Menganalisis Karya Sastra"]
    },
    "Matematika": {
        "A (Kelas 1-2)": ["Bilangan 1-20", "Penjumlahan & Pengurangan", "Bangun Datar Sederhana"],
        "B (Kelas 3-4)": ["Perkalian & Pembagian", "Pecahan Senilai", "Keliling & Luas Persegi"],
        "C (Kelas 5-6)": ["Operasi Hitung Campuran", "Volume Bangun Ruang", "Statistika Data Sederhana"]
    },
    "IPAS": {
        "B (Kelas 3-4)": ["Wujud Zat & Perubahannya", "Bagian Tubuh Tumbuhan", "Siklus Hidup Hewan"],
        "C (Kelas 5-6)": ["Sistem Organ Manusia", "Ekosistem & Keseimbangan", "Tata Surya"]
    }
}

# --- UI APLIKASI ---
st.title("🏫 Generator Modul Ajar SD: Deep Learning")
st.subheader("Sistem Administrasi Guru Tanpa API Key")

# 1. Identitas Administrasi
st.info("### 📋 1. Identitas Administrasi")
c1, c2, c3 = st.columns(3)
with c1:
    nama_guru = st.text_input("Nama Lengkap & Gelar")
    nama_sekolah = st.text_input("Nama Sekolah")
    tahun_ajaran = st.text_input("Tahun Ajaran", "2025/2026")
with c2:
    mapel = st.selectbox("Mata Pelajaran", list(DATABASE_MATERI.keys()))
    fase = st.selectbox("Fase (Tingkatan)", ["A (Kelas 1-2)", "B (Kelas 3-4)", "C (Kelas 5-6)"])
with c3:
    kelas = st.selectbox("Kelas", ["1", "2", "3", "4", "5", "6"])
    semester = st.radio("Semester", ["1 (Ganjil)", "2 (Genap)"], horizontal=True)

st.divider()

# 2. Pemilihan Materi Otomatis
st.info("### 💡 2. Detail Materi & Deep Learning")
options_materi = DATABASE_MATERI[mapel].get(fase, ["Materi Lainnya..."])
topik_pilihan = st.selectbox("Pilih Topik Pembelajaran", options_materi)

if topik_pilihan == "Materi Lainnya...":
    topik_pilihan = st.text_input("Ketik Nama Topik Secara Manual")

# --- PROSES GENERATE ---
if st.button("🚀 Susun Modul & Rubrik Sekarang"):
    if not nama_guru or not topik_pilihan:
        st.error("Lengkapi Nama Guru dan Topik untuk melanjutkan!")
    else:
        # Template Strategi 8 Dimensi
        modul_result = f"""
        ============================================================
        MODUL AJAR KURIKULUM MERDEKA - PEMBELAJARAN MENDALAM
        ============================================================
        
        A. IDENTITAS UMUM
        ------------------------------------------------------------
        Penyusun     : {nama_guru}
        Instansi     : {nama_sekolah}
        Tahun Ajaran : {tahun_ajaran}
        Mata Pelajaran: {mapel}
        Fase / Kelas : {fase} / {kelas}
        Semester     : {semester}
        Topik        : {topik_pilihan}

        B. LANGKAH PEMBELAJARAN (INTEGRASI 8 DIMENSI LULUSAN)
        ------------------------------------------------------------
        1. [Character] : Memulai kelas dengan doa dan refleksi tanggung jawab diri terkait {topik_pilihan}.
        2. [Citizenship] : Diskusi bagaimana {topik_pilihan} berdampak pada kehidupan masyarakat di sekitar sekolah.
        3. [Collaboration] : Siswa bekerja dalam kelompok heterogen untuk menyelesaikan tantangan {topik_pilihan}.
        4. [Communication] : Setiap kelompok mempresentasikan hasil diskusi menggunakan alat peraga sederhana.
        5. [Creativity] : Siswa membuat produk/gambar/karya orisinal sebagai bukti pemahaman materi.
        6. [Critical Thinking] : Sesi tanya jawab 'Mengapa' untuk menggali logika mendalam tentang {topik_pilihan}.
        7. [Compassion] : Menumbuhkan empati dengan mendiskusikan manfaat belajar {topik_pilihan} bagi orang lain.
        8. [Computational Thinking] : Menyusun urutan logis langkah-langkah dalam menyelesaikan tugas {topik_pilihan}.

        C. RUBRIK PENILAIAN (ASESMEN AUTENTIK)
        ------------------------------------------------------------
        | Dimensi | Perlu Bimbingan | Baik | Sangat Baik |
        |---------|-----------------|------|-------------|
        | Kognitif| Mengetahui dasar | Memahami konsep | Mampu menerapkan |
        | Karakter| Mulai terlihat | Konsisten | Menjadi teladan |
        | Kreativitas | Meniru contoh | Ada variasi ide | Sangat inovatif |

        Ditetapkan di: {nama_sekolah}
        Mengetahui,                                 Guru Kelas,
        
        
        (Kepala Sekolah)                            ({nama_guru})
        """
        
        st.success("Modul Berhasil Dibuat!")
        st.text_area("Preview Dokumen", modul_result, height=500)
        
        st.download_button(
            label="📥 Unduh Modul Ajar (TXT)",
            data=modul_result,
            file_name=f"Modul_{mapel}_Kelas{kelas}_{topik_pilihan}.txt",
            mime="text/plain"
        )

st.divider()
st.caption("Aplikasi ini bekerja secara offline/lokal dan tidak memerlukan biaya API.")
