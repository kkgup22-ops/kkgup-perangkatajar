import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Penyusun Modul SD Pro", page_icon="🏫", layout="wide")

# --- DATABASE MATERI LENGKAP ---
DATABASE_MATERI = {
    "Bahasa Indonesia": {
        "A (Kelas 1-2)": ["Membaca Huruf & Suku Kata", "Teks Deskripsi Benda", "Puisi Anak"],
        "B (Kelas 3-4)": ["Sehatlah Ragaku (Kesehatan Tubuh)", "Ide Pokok & Pendukung", "Membedakan Fakta & Opini", "Menulis Teks Narasi"],
        "C (Kelas 5-6)": ["Teks Eksplanasi", "Pidato & Presentasi", "Surat Resmi"]
    },
    "Pendidikan Agama Islam": {
        "A (Kelas 1-2)": ["Huruf Hijaiyah", "Rukun Islam & Iman", "Adab Makan & Minum"],
        "B (Kelas 3-4)": ["Asmaul Husna", "Shalat Fardhu", "Kisah Nabi Muhammad saw."],
        "C (Kelas 5-6)": ["Hari Akhir", "Zakat & Haji", "Etika Berteman"]
    },
    "Pendidikan Pancasila": {
        "A (Kelas 1-2)": ["Simbol Pancasila", "Aturan di Rumah", "Gotong Royong"],
        "B (Kelas 3-4)": ["Makna Sila Pancasila", "Hak & Kewajiban", "Keberagaman Budaya"],
        "C (Kelas 5-6)": ["Penerapan Pancasila", "Norma & Hukum", "Cinta Tanah Air"]
    },
    "Bahasa Inggris": {
        "A (Kelas 1-2)": ["Greetings", "Numbers 1-10", "Colors"],
        "B (Kelas 3-4)": ["Parts of Body", "My House", "Daily Activities"],
        "C (Kelas 5-6)": ["Direction", "Future Dreams", "Simple Past"]
    },
    "Seni Budaya": {
        "A (Kelas 1-2)": ["Garis & Warna", "Gerak Tari Hewan", "Kolase"],
        "B (Kelas 3-4)": ["Menggambar Perspektif", "Tari Tradisional", "Membuat Anyaman"],
        "C (Kelas 5-6)": ["Seni Rupa Terapan", "Ansambel Musik", "Koreografi Tari"]
    },
    "PJOK": {
        "A (Kelas 1-2)": ["Gerak Lokomotor", "Senam Irama", "Kebersihan Tubuh"],
        "B (Kelas 3-4)": ["Kombinasi Gerak Dasar", "Renang Gaya Dada", "Atletik"],
        "C (Kelas 5-6)": ["Pencak Silat", "Kebugaran Jasmani", "Permainan Bola Besar"]
    }
}

# --- UI APLIKASI ---
st.title("🛡️ Generator Perangkat Pembelajaran SD Lengkap")
st.write("Versi Offline - Tanpa API Key - Berbasis Deep Learning & 8 Profil Lulusan")

# 1. Input Data Administrasi
with st.container():
    st.info("### 📋 1. Identitas Administrasi")
    c1, c2, c3 = st.columns(3)
    with c1:
        nama_guru = st.text_input("Nama Guru & Gelar", placeholder="Contoh: Haidar, S.Pd.")
        nama_sekolah = st.text_input("Nama Sekolah", placeholder="Contoh: SDN Merdeka")
        tahun_ajaran = st.text_input("Tahun Ajaran", "2025/2026")
    with c2:
        mapel = st.selectbox("Mata Pelajaran", list(DATABASE_MATERI.keys()))
        fase = st.selectbox("Fase", ["A (Kelas 1-2)", "B (Kelas 3-4)", "C (Kelas 5-6)"])
    with c3:
        kelas = st.selectbox("Kelas", ["1", "2", "3", "4", "5", "6"])
        semester = st.radio("Semester", ["1 (Ganjil)", "2 (Genap)"], horizontal=True)

st.divider()

# 2. Detail Materi
st.info("### 💡 2. Materi & Strategi")
options_materi = DATABASE_MATERI[mapel].get(fase, ["Materi Lainnya..."])
topik_pilihan = st.selectbox("Pilih Topik Pembelajaran", options_materi)

if topik_pilihan == "Materi Lainnya...":
    topik_pilihan = st.text_input("Ketik Topik Secara Manual")

# --- PROSES GENERATE ---
if st.button("🚀 Susun Modul Ajar Lengkap"):
    if not nama_guru or not topik_pilihan:
        st.error("Lengkapi Nama Guru dan Topik untuk melanjutkan!")
    else:
        # Template berdasarkan dokumen referensi user
        modul_result = f"""
MODUL AJAR KURIKULUM MERDEKA
------------------------------------------------------------
I. INFORMASI UMUM
------------------------------------------------------------
Penyusun       : {nama_guru}
Instansi       : {nama_sekolah}
Tahun Ajaran   : {tahun_ajaran}
Mata Pelajaran : {mapel}
Fase / Kelas   : {fase} / {kelas}
Semester       : {semester}
Bab / Tema     : {topik_pilihan}

II. 8 PROFIL LULUSAN (DEEP LEARNING)
------------------------------------------------------------
1. Keimanan     : Memiliki keyakinan teguh akan keberadaan Tuhan.
2. Kewargaan    : Cinta tanah air, taat aturan, dan tanggung jawab sosial.
3. Penalaran    : Berpikir logis, analitis, dan reflektif.
4. Kreativitas  : Berpikir inovatif, fleksibel, dan orisinal.
5. Kolaborasi   : Bekerja sama secara efektif dan gotong royong.
6. Kemandirian  : Bertanggung jawab atas proses dan hasil belajar.
7. Kesehatan    : Memiliki fisik prima dan keseimbangan mental (well-being).
8. Komunikasi   : Menyampaikan ide secara efektif (lisan & tulisan).

III. KEGIATAN PEMBELAJARAN (DEEP LEARNING METHOD)
------------------------------------------------------------
- Mindful Learning   : Siswa sadar penuh dalam menganalisis materi {topik_pilihan}.
- Meaningful Learning: Menghubungkan {topik_pilihan} dengan pengalaman nyata sehari-hari.
- Joyful Learning    : Aktivitas menyenangkan melalui kuis atau diskusi kelompok.

IV. ASESMEN / PENILAIAN
------------------------------------------------------------
- Skala 4 (Sangat Baik): Menguasai materi sepenuhnya & menunjukkan 8 profil lulusan.
- Skala 3 (Baik)       : Menguasai materi dengan kaidah yang benar.
- Skala 2 (Cukup)     : Memahami materi namun masih perlu bimbingan.
- Skala 1 (Kurang)    : Belum mampu mencapai indikator pembelajaran.

------------------------------------------------------------
Mengetahui,                                 2026
Kepala Sekolah                              Guru Kelas


(____________________)                      ({nama_guru})
        """
        
        st.success("Modul Berhasil Dibuat!")
        st.text_area("Pratinjau Dokumen", modul_result, height=500)
        
        st.download_button(
            label="📥 Unduh Modul Ajar (.txt)",
            data=modul_result,
            file_name=f"Modul_{mapel}_{topik_pilihan}.txt",
            mime="text/plain"
        )
