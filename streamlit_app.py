import streamlit as st
from pdf import PDF

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="PDF Generator Modul SD", page_icon="📄", layout="wide")

# --- DATABASE MATERI ---
DATABASE_MATERI = {
    "Bahasa Indonesia": {
        "A (Kelas 1-2)": ["Membaca Huruf", "Suku Kata"],
        "B (Kelas 3-4)": ["Sehatlah Ragaku (Kesehatan)", "Ide Pokok", "Fakta & Opini"],
        "C (Kelas 5-6)": ["Teks Eksplanasi", "Pidato"]
    },
    "Pendidikan Pancasila": {
        "A (Kelas 1-2)": ["Simbol Pancasila", "Aturan Rumah"],
        "B (Kelas 3-4)": ["Sila Pancasila", "Hak & Kewajiban"],
        "C (Kelas 5-6)": ["Norma & Hukum", "Cinta Tanah Air"]
    },
    "PJOK": {
        "B (Kelas 3-4)": ["Kombinasi Gerak Dasar", "Renang Gaya Dada"],
        "C (Kelas 5-6)": ["Pencak Silat", "Kebugaran Jasmani"]
    }
    # Tambahkan mapel lain sesuai kebutuhan di sini
}

# --- CLASS UNTUK GENERATE PDF ---
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'MODUL AJAR KURIKULUM MERDEKA', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 11)
        self.set_fill_color(230, 230, 230)
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 6, body)
        self.ln()

# --- UI APLIKASI ---
st.title("📄 Pembuat PDF Modul Ajar SD")
st.write("Isi data di bawah ini untuk mengunduh Modul Ajar dalam format PDF siap cetak.")

with st.container():
    c1, c2 = st.columns(2)
    with c1:
        nama_guru = st.text_input("Nama Guru & Gelar")
        nama_sekolah = st.text_input("Nama Sekolah")
        mapel = st.selectbox("Mata Pelajaran", list(DATABASE_MATERI.keys()))
    with c2:
        kelas = st.selectbox("Kelas", ["1", "2", "3", "4", "5", "6"])
        semester = st.radio("Semester", ["1 (Ganjil)", "2 (Genap)"], horizontal=True)
        tahun = st.text_input("Tahun Ajaran", "2025/2026")

fase_map = {"1":"A", "2":"A", "3":"B", "4":"B", "5":"C", "6":"C"}
fase_label = f"{fase_map[kelas]} (Kelas {kelas})"

options_materi = DATABASE_MATERI[mapel].get(fase_label.split(" (")[0] + f" (Kelas {kelas})", ["Materi Lainnya..."])
# Menyesuaikan filter fase database sederhana
key_fase = [k for k in DATABASE_MATERI[mapel].keys() if kelas in k][0]
topik_pilihan = st.selectbox("Pilih Topik", DATABASE_MATERI[mapel][key_fase])

if st.button("生成 Buat & Unduh PDF"):
    if not nama_guru or not nama_sekolah:
        st.error("Lengkapi Nama Guru dan Sekolah!")
    else:
        # 1. Bangun Konten Teks
        isi_kegiatan = (
            f"1. PENDAHULUAN: Doa, Absensi, Apersepsi materi {topik_pilihan}.\n"
            f"2. KEGIATAN INTI (Deep Learning):\n"
            f"   - Mindful: Observasi mendalam tentang {topik_pilihan}.\n"
            f"   - Meaningful: Diskusi 8 Profil Lulusan (Kritis, Kreatif, Kolaboratif).\n"
            f"   - Joyful: Game edukatif dan apresiasi karya.\n"
            f"3. PENUTUP: Refleksi dan kesimpulan."
        )

        # 2. Proses PDF
        pdf = PDF()
        pdf.add_page()
        
        pdf.chapter_title("I. IDENTITAS MODUL")
        pdf.chapter_body(f"Nama Guru: {nama_guru}\nSekolah: {nama_sekolah}\nMapel: {mapel}\nKelas: {kelas} / Semester {semester}\nTahun Ajaran: {tahun}\nTopik: {topik_pilihan}")
        
        pdf.chapter_title("II. PROFIL LULUSAN (8 DIMENSI)")
        pdf.chapter_body("Keimanan, Kewargaan, Penalaran Kritis, Kreativitas, Kolaborasi, Kemandirian, Kesehatan, Komunikasi.")
        
        pdf.chapter_title("III. KEGIATAN PEMBELAJARAN")
        pdf.chapter_body(isi_kegiatan)
        
        pdf.ln(10)
        pdf.cell(100)
        pdf.cell(0, 5, f"Jakarta, Januari 2026", 0, 1, 'L')
        pdf.cell(100)
        pdf.cell(0, 5, f"Guru Kelas,", 0, 1, 'L')
        pdf.ln(15)
        pdf.cell(100)
        pdf.cell(0, 5, f"( {nama_guru} )", 0, 1, 'L')

        # 3. Output ke Streamlit
        pdf_output = pdf.output(dest='S').encode('latin-1')
        st.success("PDF Berhasil Dibuat!")
        st.download_button(
            label="⬇️ Klik Di Sini Untuk Unduh PDF",
            data=pdf_output,
            file_name=f"Modul_Ajar_{topik_pilihan}.pdf",
            mime="application/pdf"
        )
