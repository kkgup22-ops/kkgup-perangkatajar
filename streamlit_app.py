import streamlit as st
import google.generativeai as genai

# --- CONFIGURASI UI ---
st.set_page_config(page_title="Penyusun Perangkat SD", layout="wide", page_icon="🏫")

# --- FUNGSI GENERATOR AI ---
def generate_perangkat(api_key, data, topik):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Bertindaklah sebagai Ahli Kurikulum Merdeka Kemdikbud. Buatkan perangkat pembelajaran lengkap.
    
    DATA ADMINISTRASI:
    Nama Guru: {data['nama']}
    Sekolah: {data['sekolah']}
    Kelas/Semester: {data['kelas']} / {data['semester']}
    Tahun Ajaran: {data['tahun']}
    Mata Pelajaran: {data['mapel']}
    Topik: {topik}

    TUGAS ANDA:
    1. Buat MODUL AJAR dengan strategi Pembelajaran Mendalam (Deep Learning).
    2. Integrasikan 8 Dimensi: Karakter, Kewarganegaraan, Kolaborasi, Komunikasi, Kreativitas, Berpikir Kritis, Empati (Compassion), dan Berpikir Komputasi.
    3. Buat RUBRIK PENILAIAN yang mencakup kriteria: Perlu Bimbingan, Cukup, Baik, dan Sangat Baik untuk setiap dimensi tersebut.

    FORMAT OUTPUT:
    --- BAGIAN 1: MODUL AJAR ---
    (Tujuan, Langkah-langkah detail per dimensi, dan Penutup)
    
    --- BAGIAN 2: RUBRIK PENILAIAN ---
    (Tabel rubrik penilaian autentik yang siap digunakan untuk mengamati siswa)
    """
    
    response = model.generate_content(prompt)
    return response.text

# --- TAMPILAN APLIKASI ---
st.title("🛡️ Generator Perangkat Pembelajaran SD Lengkap")
st.write("Sesuai Kurikulum Merdeka & Standar Pembelajaran Mendalam (Deep Learning)")

# Input Data Administrasi
with st.expander("📝 1. Isi Data Administrasi (KOP Dokumen)", expanded=True):
    c1, c2, c3 = st.columns(3)
    with c1:
        nama_guru = st.text_input("Nama Guru & Gelar", placeholder="Contoh: Budi Santoso, S.Pd.")
        nama_sekolah = st.text_input("Nama Sekolah", placeholder="Contoh: SDN 01 Merdeka")
    with c2:
        kelas_sd = st.selectbox("Kelas", ["1", "2", "3", "4", "5", "6"])
        semester = st.radio("Semester", ["Ganjil", "Genap"], horizontal=True)
    with c3:
        tahun_ajaran = st.text_input("Tahun Ajaran", "2025/2026")
        mapel = st.selectbox("Mata Pelajaran", ["Bahasa Indonesia", "Matematika", "IPAS", "Pendidikan Pancasila", "Seni Budaya", "PJOK"])

# Input Materi
with st.expander("💡 2. Isi Detail Materi", expanded=True):
    topik_materi = st.text_area("Topik Pembelajaran", placeholder="Contoh: Mengenal Bagian Tubuh Tumbuhan dan Fungsinya")

# Sidebar untuk API
with st.sidebar:
    st.header("🔑 Pengaturan AI")
    api_key = st.text_input("Gemini API Key", type="password")
    st.divider()
    st.caption("Aplikasi ini membantu Guru SD menghemat waktu administrasi sambil tetap menjaga kualitas pembelajaran yang mendalam (Deep Learning).")

# Tombol Eksekusi
if st.button("✨ Buat Modul Ajar & Rubrik Penilaian"):
    if not api_key or not nama_guru or not topik_materi:
        st.error("Lengkapi Data Guru, Topik, dan API Key untuk melanjutkan.")
    else:
        with st.spinner("Sedang memproses 8 dimensi lulusan..."):
            try:
                data_final = {
                    "nama": nama_guru, "sekolah": nama_sekolah, "kelas": kelas_sd,
                    "semester": semester, "tahun": tahun_ajaran, "mapel": mapel
                }
                hasil = generate_perangkat(api_key, data_final, topik_materi)
                
                st.success("Berhasil! Silakan periksa draf di bawah ini.")
                st.markdown("---")
                st.markdown(hasil)
                
                # Fitur Download
                st.download_button(
                    label="📥 Unduh Perangkat Pembelajaran (Format .txt)",
                    data=hasil,
                    file_name=f"Perangkat_SD_{mapel}_Kelas{kelas_sd}.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error: {e}")
