import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Generator Modul SD", page_icon="🏫", layout="wide")

# --- DATABASE MATERI LENGKAP ---
DATABASE_MATERI = {
    "Bahasa Indonesia": {
        "A (Kelas 1-2)": ["Mengenal Huruf & Suku Kata", "Teks Deskripsi Benda", "Puisi Anak"],
        "B (Kelas 3-4)": ["Sehatlah Ragaku (Kesehatan Tubuh)", "Ide Pokok & Pendukung", "Membedakan Fakta & Opini", "Menulis Teks Narasi"],
        "C (Kelas 5-6)": ["Teks Eksplanasi", "Pidato & Presentasi", "Surat Resmi"]
    },
    "Pendidikan Agama Islam": {
        "A (Kelas 1-2)": ["Huruf Hijaiyah", "Rukun Islam & Iman", "Adab Makan & Minum"],
        "B (Kelas 3-4)": ["Asmaul Husna", "Shalat Fardhu", "Kisah Nabi Muhammad saw."],
        "C (Kelas 5-6)": ["Zakat & Haji", "Etika Berteman", "Hari Akhir"]
    },
    "Pendidikan Pancasila": {
        "A (Kelas 1-2)": ["Simbol Pancasila", "Aturan di Rumah", "Gotong Royong"],
        "B (Kelas 3-4)": ["Makna Sila Pancasila", "Hak & Kewajiban", "Keberagaman Budaya"],
        "C (Kelas 5-6)": ["Penerapan Pancasila", "Norma & Hukum", "Kedaulatan Rakyat"]
    },
    "Bahasa Inggris": {
        "A (Kelas 1-2)": ["Greetings", "Numbers 1-10", "Colors"],
        "B (Kelas 3-4)": ["Parts of Body", "My House", "Daily Activities"],
        "C (Kelas 5-6)": ["Direction", "Future Dreams", "Simple Past"]
    },
    "PJOK": {
        "A (Kelas 1-2)": ["Gerak Lokomotor", "Kebersihan Tubuh", "Senam Irama"],
        "B (Kelas 3-4)": ["Kombinasi Gerak Dasar", "Renang Gaya Dada", "Atletik"],
        "C (Kelas 5-6)": ["Pencak Silat", "Kebugaran Jasmani", "Bola Besar"]
    },
    "Seni Budaya": {
        "A (Kelas 1-2)": ["Garis & Warna", "Gerak Tari Hewan", "Kolase"],
        "B (Kelas 3-4)": ["Menggambar Perspektif", "Tari Tradisional", "Anyaman"],
        "C (Kelas 5-6)": ["Seni Rupa Terapan", "Ansambel Musik", "Koreografi"]
    }
}

# --- UI APLIKASI ---
st.title("🛡️ Generator Perangkat Pembelajaran SD (Deep Learning)")
st.write("Sesuai Ketentuan Pemerintah - Berbasis 8 Profil Lulusan - Tanpa API Key")

# 1. Input Identitas
with st.expander("📝 1. Identitas Administrasi", expanded=True):
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

# 2. Detail Materi
with st.expander("💡 2. Materi & Topik", expanded=True):
    options_materi = DATABASE_MATERI[mapel].get(fase, ["Materi Lainnya..."])
    topik_pilihan = st.selectbox("Pilih Materi", options_materi)
    if topik_pilihan == "Materi Lainnya...":
        topik_pilihan = st.text_input("Ketik Topik Baru")

# --- PROSES GENERATE ---
if st.button("🚀 Susun Modul Ajar Lengkap"):
    if not nama_guru or not topik_pilihan:
        st.error("Lengkapi Nama Guru dan Topik!")
    else:
        # LOGIKA KEGIATAN PEMBELAJARAN (DEEP LEARNING)
        kegiatan_inti = f"""
        A. KEGIATAN PENDAHULUAN (15 Menit)
        1. Guru membuka dengan salam dan doa (Dimensi: Keimanan).
        2. Apersepsi: Guru mengaitkan materi {topik_pilihan} dengan pengalaman nyata siswa.
        3. Guru menyampaikan tujuan pembelajaran dan pertanyaan pemantik.

        B. KEGIATAN INTI (90 Menit) - Metode Deep Learning
        1. Mindful Learning: 
           - Siswa mengamati video/gambar/teks terkait {topik_pilihan}.
           - Siswa secara sadar (khusyuk) melakukan observasi dan mencatat hal penting.
        2. Meaningful Learning (8 Profil Lulusan):
           - [Penalaran Kritis] Siswa menganalisis permasalahan dalam topik {topik_pilihan}.
           - [Kolaborasi] Siswa berdiskusi kelompok untuk mencari solusi nyata.
           - [Komunikasi] Setiap kelompok mempresentasikan hasil karyanya di depan kelas.
           - [Kreativitas] Siswa membuat produk (poster/model/tulisan) tentang {topik_pilihan}.
           - [Kewargaan] Siswa membahas dampak topik ini bagi lingkungan sekitarnya.
        3. Joyful Learning:
           - Guru menyelipkan ice breaking atau kuis interaktif agar suasana menyenangkan.
           - Siswa saling memberikan apresiasi "Tepuk Hebat" kepada teman.

        C. KEGIATAN PENUTUP (15 Menit)
        1. Siswa melakukan refleksi: "Apa yang paling menarik hari ini?" (Dimensi: Kemandirian).
        2. Guru memberikan kesimpulan dan rencana pembelajaran berikutnya.
        3. Kelas ditutup dengan doa dan pesan kesehatan (Dimensi: Kesehatan).
        """

        # FORMAT MODUL AJAR LENGKAP
        modul_result = f"""
============================================================
MODUL AJAR KURIKULUM MERDEKA - PEMBELAJARAN MENDALAM
============================================================

I. INFORMASI UMUM
------------------------------------------------------------
Penyusun       : {nama_guru}
Instansi       : {nama_sekolah}
Tahun Ajaran   : {tahun_ajaran}
Mata Pelajaran : {mapel}
Fase / Kelas   : {fase} / {kelas}
Semester       : {semester}
Bab / Tema     : {topik_pilihan}

II. KOMPONEN INTI
------------------------------------------------------------
A. TUJUAN PEMBELAJARAN:
   Siswa mampu memahami, menganalisis, dan menerapkan konsep {topik_pilihan} 
   melalui pendekatan Deep Learning untuk mewujudkan 8 Profil Lulusan.

B. 8 PROFIL LULUSAN YANG DIKEMBANGKAN:
   1. Keimanan: Keyakinan spiritual dalam belajar.
   2. Kewargaan: Kepedulian sosial dan cinta tanah air.
   3. Penalaran Kritis: Berpikir logis dan analitis.
   4. Kreativitas: Inovasi dalam berkarya.
   5. Kolaborasi: Kerjasama tim yang harmonis.
   6. Kemandirian: Tanggung jawab belajar mandiri.
   7. Kesehatan: Keseimbangan fisik dan mental.
   8. Komunikasi: Menyampaikan gagasan dengan efektif.

III. KEGIATAN PEMBELAJARAN
------------------------------------------------------------
{kegiatan_inti}

IV. ASESMEN DAN RUBRIK PENILAIAN
------------------------------------------------------------
| Kriteria | Perlu Bimbingan (1) | Cukup (2) | Baik (3) | Sangat Baik (4) |
|----------|--------------------|-----------|----------|-----------------|
| Pemahaman| Belum paham konsep | Paham dasar| Paham utuh| Mampu mengajarkan|
| 8 Profil | Muncul 1-2 profil | Muncul 3-5 | Muncul 6-7| Muncul semua profil|

------------------------------------------------------------
Mengetahui,                                 Januari 2026
Kepala Sekolah                              Guru Kelas


(____________________)                      ({nama_guru})
        """
        
        st.success("Perangkat Pembelajaran Berhasil Disusun!")
        st.text_area("Preview Modul Ajar", modul_result, height=600)
        
        st.download_button(
            label="📥 Unduh Modul Ajar Lengkap (.txt)",
            data=modul_result,
            file_name=f"Modul_{mapel}_{topik_pilihan}.txt",
            mime="text/plain"
        )
        
