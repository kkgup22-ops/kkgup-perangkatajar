import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Admin Guru SD Lengkap", page_icon="🏫", layout="wide")

# --- DATABASE MATERI LENGKAP ---
DATABASE_MATERI = {
    "Pendidikan Agama Islam": {
        "A (Kelas 1-2)": ["Huruf Hijaiyah", "Rukun Islam & Iman", "Adab Makan & Minum", "Kisah Nabi Adam as."],
        "B (Kelas 3-4)": ["Asmaul Husna", "Shalat Fardhu", "Kisah Nabi Muhammad saw.", "Mari Mengaji Surah Pendek"],
        "C (Kelas 5-6)": ["Hari Akhir", "Zakat & Haji", "Kisah Sahabat Nabi", "Etika Berteman (Ukhuwah)"]
    },
    "Pendidikan Pancasila": {
        "A (Kelas 1-2)": ["Simbol Pancasila", "Aturan di Rumah & Sekolah", "Identitas Diri", "Gotong Royong"],
        "B (Kelas 3-4)": ["Makna Sila Pancasila", "Hak & Kewajiban", "Keberagaman Budaya", "Musyawarah"],
        "C (Kelas 5-6)": ["Penerapan Pancasila", "Norma & Hukum", "Kedaulatan Rakyat", "Cinta Tanah Air"]
    },
    "Bahasa Inggris": {
        "A (Kelas 1-2)": ["Greetings & Farewell", "Numbers 1-10", "My Family", "Colors & Shapes"],
        "B (Kelas 3-4)": ["Parts of Body", "My House", "Daily Activities", "Animal Names"],
        "C (Kelas 5-6)": ["Direction & Location", "Health & Illness", "Future Dreams", "Simple Past Experiences"]
    },
    "Seni Budaya": {
        "A (Kelas 1-2)": ["Garis & Warna", "Bunyi Musik Sederhana", "Gerak Tari Hewan", "Membuat Kolase"],
        "B (Kelas 3-4)": ["Menggambar Perspektif", "Alat Musik Ritmis", "Tari Tradisional Daerah", "Membuat Anyaman"],
        "C (Kelas 5-6)": ["Seni Rupa Terapan", "Ansambel Musik", "Koreografi Tari Modern", "Pameran Karya Seni"]
    },
    "PJOK": {
        "A (Kelas 1-2)": ["Gerak Lokomotor", "Senam Irama", "Kebersihan Tubuh", "Permainan Bola Kecil"],
        "B (Kelas 3-4)": ["Kombinasi Gerak Dasar", "Atletik Dasar", "Renang Gaya Dada", "Bahaya Merokok"],
        "C (Kelas 5-6)": ["Pencak Silat", "Kebugaran Jasmani", "Permainan Bola Besar", "Pencegahan Penyakit Menular"]
    },
    "IPAS": {
        "B (Kelas 3-4)": ["Wujud Zat", "Bagian Tubuh Tumbuhan", "Energi & Perubahannya", "Peta Lingkungan"],
        "C (Kelas 5-6)": ["Sistem Pencernaan", "Listrik & Magnet", "Warisan Budaya", "Bumi & Alam Semesta"]
    },
    "Matematika": {
        "A (Kelas 1-2)": ["Bilangan Cacah", "Penjumlahan & Pengurangan", "Pola Gambar", "Jam & Waktu"],
        "B (Kelas 3-4)": ["Perkalian & Pembagian", "Pecahan", "Luas & Keliling Bangun", "Diagram Batang"],
        "C (Kelas 5-6)": ["Bilangan Bulat Negatif", "Lingkaran", "Bangun Ruang Campuran", "Rata-rata (Mean)"]
    },
    "Bahasa Indonesia": {
        "A (Kelas 1-2)": ["Membaca Huruf", "Suku Kata", "Teks Deskripsi Benda", "Puisi Anak"],
        "B (Kelas 3-4)": ["Mencari Ide Pokok", "Wawancara Tokoh", "Menulis Laporan", "Pantun Nasihat"],
        "C (Kelas 5-6)": ["Surat Resmi", "Teks Prosedur", "Iklan & Poster", "Meringkas Buku"]
    }
}

# --- UI APLIKASI ---
st.title("🛡️ Generator Perangkat Pembelajaran SD Lengkap")
st.write("Versi Offline - Tanpa API Key - Strategi 8 Dimensi Lulusan")

# 1. Input Data Administrasi
with st.container():
    st.info("### 📋 1. Identitas Administrasi")
    c1, c2, c3 = st.columns(3)
    with c1:
        nama_guru = st.text_input("Nama Guru & Gelar")
        nama_sekolah = st.text_input("Nama Sekolah")
        tahun_ajaran = st.text_input("Tahun Ajaran", "2025/2026")
    with c2:
        mapel = st.selectbox("Mata Pelajaran", list(DATABASE_MATERI.keys()))
        fase = st.selectbox("Fase", ["A (Kelas 1-2)", "B (Kelas 3-4)", "C (Kelas 5-6)"])
    with c3:
        kelas = st.selectbox("Kelas", ["1", "2", "3", "4", "5", "6"])
        semester = st.radio("Semester", ["1 (Ganjil)", "2 (Genap)"], horizontal=True)

st.divider()

# 2. Detail Materi
st.info("### 💡 2. Pemilihan Materi & Strategi")
options_materi = DATABASE_MATERI[mapel].get(fase, ["Materi Lainnya..."])
topik_pilihan = st.selectbox("Pilih Materi Spesifik", options_materi)

if topik_pilihan == "Materi Lainnya...":
    topik_pilihan = st.text_input("Ketik Topik Baru")

# --- PROSES GENERATE ---
if st.button("🚀 Susun Modul Ajar Lengkap"):
    if not nama_guru or not topik_pilihan:
        st.error("Lengkapi data administrasi dan materi!")
    else:
        # Template Aktivitas 8 Dimensi
        modul_teks = f"""
============================================================
MODUL AJAR KURIKULUM MERDEKA - DEEP LEARNING
============================================================

I. IDENTITAS MODUL
------------------------------------------------------------
Penyusun        : {nama_guru}
Sekolah         : {nama_sekolah}
Tahun Ajaran    : {tahun_ajaran}
Fase / Kelas    : {fase} / {kelas}
Mata Pelajaran  : {mapel}
Topik / Materi  : {topik_pilihan}
Semester        : {semester}

II. KEGIATAN INTI (INTEGRASI 8 DIMENSI LULUSAN)
------------------------------------------------------------
1. Character      : Pembiasaan berdoa dan menanamkan nilai integritas dalam {topik_pilihan}.
2. Citizenship    : Menghubungkan {topik_pilihan} dengan tanggung jawab sosial di masyarakat.
3. Collaboration  : Kerja tim dalam memecahkan studi kasus atau proyek terkait {topik_pilihan}.
4. Communication  : Sesi presentasi kelompok dan berbagi umpan balik yang konstruktif.
5. Creativity     : Mendesain karya orisinal (gambar/alat peraga) berdasarkan materi.
6. Critical Thinking: Menganalisis alasan 'mengapa' konsep {topik_pilihan} penting dipelajari.
7. Compassion     : Berbagi manfaat belajar {topik_pilihan} untuk membantu sesama teman.
8. Comp. Thinking : Menyusun instruksi langkah-demi-langkah terkait penyelesaian materi.

III. RUBRIK ASESMEN (PENILAIAN)
------------------------------------------------------------
- Sangat Baik : Menguasai konsep dan aktif di seluruh 8 dimensi.
- Baik        : Menguasai konsep dan menunjukkan sebagian besar dimensi.
- Cukup       : Memahami konsep dasar dengan bantuan bimbingan guru.

------------------------------------------------------------
Mengetahui,                                 Guru Kelas,
Kepala Sekolah


(____________________)                      ({nama_guru})
        """
        
        st.success("Perangkat Pembelajaran Berhasil Disusun!")
        st.text_area("Pratinjau Dokumen", modul_teks, height=500)
