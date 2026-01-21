import streamlit as st
import google.generativeai as genai

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Asisten Modul Ajar SD",
    page_icon="🏫",
    layout="wide"
)

# --- FUNGSI AI ---
def generate_perangkat_lengkap(api_key, data, topik):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Bertindaklah sebagai ahli kurikulum pendidikan dasar (SD). Buatkan perangkat pembelajaran lengkap.
    
    DATA ADMINISTRASI:
    Nama Guru: {data['nama']}
    Sekolah: {data['sekolah']}
    Kelas/Semester: {data['kelas']} / {data['semester']}
    Tahun Ajaran: {data['tahun']}
    Mata Pelajaran: {data['mapel']}
    Topik: {topik}

    ISI PERANGKAT:
    1. MODUL AJAR: Gunakan pendekatan Deep Learning dengan integrasi 8 Dimensi Lulusan (Character, Citizenship, Collaboration, Communication, Creativity, Critical Thinking, Compassion, Computational Thinking).
    2. LANGKAH PEMBELAJARAN: Buat aktivitas yang konkret untuk anak SD (Fase {data['fase']}).
    3. RUBRIK PENILAIAN: Buat tabel penilaian autentik untuk aspek kognitif dan karakter (8 dimensi).
    4. REKOMENDASI MEDIA: Sarankan alat peraga atau media digital (YouTube/Simulasi) yang relevan.

    Gunakan format Markdown yang rapi dengan heading dan tabel.
    """
    
    response = model.generate_content(prompt)
    return response.text

# --- ANTARMUKA PENGGUNA (UI) ---
st.title("🏫 Generator Perangkat Pembelajaran SD")
st.markdown("Aplikasi berbasis AI untuk menyusun Modul Ajar **Deep Learning** dengan **8 Dimensi Lulusan**.")

# Sidebar untuk API Key
with st.sidebar:
    st.header("🔑 Pengaturan")
    api_key = st.text_input("Gemini API Key", type="password", help="Dapatkan API Key gratis di Google AI Studio")
    st.divider()
    st.info("Aplikasi ini membantu guru memenuhi administrasi Kurikulum Merdeka secara otomatis.")

# Form Input Data Guru & Sekolah
st.subheader("📋 Data Administrasi & Identitas")
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        nama_guru = st.text_input("Nama Lengkap Guru", placeholder="Contoh: Siti Aminah, S.Pd.")
        nama_sekolah = st.text_input("Nama Sekolah", placeholder="Contoh: SDN 05 Pagi Jakarta")
        tahun_ajaran = st.text_input("Tahun Ajaran", value="2025/2026")
    with c2:
        mapel = st.selectbox("Mata Pelajaran", ["Bahasa Indonesia", "Matematika", "IPAS", "Pancasila", "Seni Budaya", "PJOK"])
        col_k, col_s = st.columns(2)
        with col_k:
            kelas = st.selectbox("Kelas", ["1", "2", "3", "4", "5", "6"])
        with col_s:
            semester = st.radio("Semester", ["1 (Ganjil)", "2 (Genap)"], horizontal=True)

# Input Topik Pembelajaran
st.subheader("💡 Materi Pembelajaran")
topik_materi = st.text_area("Masukkan Topik atau Tujuan Pembelajaran (TP)", 
                            placeholder="Contoh: Mengetahui proses siklus air dan dampaknya bagi makhluk hidup.")

# Penentuan Fase Otomatis
fase_map = {"1": "A", "2": "A", "3": "B", "4": "B", "5": "C", "6": "C"}
fase_terpilih = fase_map[kelas]

# Tombol Eksekusi
if st.button("🚀 Buat Perangkat Pembelajaran Lengkap"):
    if not api_key:
        st.error("Silakan masukkan API Key di sidebar!")
    elif not nama_guru or not topik_materi:
        st.warning("Mohon lengkapi Nama Guru dan Topik Materi.")
    else:
        with st.spinner("AI sedang merancang pembelajaran mendalam..."):
            try:
                data_guru = {
                    "nama": nama_guru, "sekolah": nama_sekolah, "tahun": tahun_ajaran,
                    "mapel": mapel, "kelas": kelas, "semester": semester, "fase": fase_terpilih
                }
                
                hasil = generate_perangkat_lengkap(api_key, data_guru, topik_materi)
                
                st.success("Perangkat Pembelajaran Berhasil Disusun!")
                st.divider()
                
                # Menampilkan Hasil
                st.markdown(hasil)
                
                # Tombol Download
                st.download_button(
                    label="📥 Unduh Hasil (Format .txt)",
                    data=hasil,
                    file_name=f"Modul_Ajar_{mapel}_Kelas{kelas}.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Terjadi kesalahan teknis: {e}")

st.divider()
st.caption("Dikembangkan untuk mendukung transformasi pendidikan guru SD Indonesia.")
