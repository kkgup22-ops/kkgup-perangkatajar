import streamlit as st

# Pengaturan Halaman
st.set_page_config(page_title="Deep Learning Generator", layout="wide")

# Database Aktivitas 8 Dimensi
dimensi_data = {
    "Character": "Siswa merefleksikan tanggung jawab moral terkait {topik}.",
    "Citizenship": "Diskusi peran siswa sebagai warga global dalam isu {topik}.",
    "Collaboration": "Proyek kelompok untuk memecahkan tantangan nyata pada {topik}.",
    "Communication": "Presentasi ide kreatif atau kampanye tentang {topik}.",
    "Creativity": "Membuat produk, desain, atau karya orisinal bertema {topik}.",
    "Critical Thinking": "Debat atau analisis data mendalam mengenai fenomena {topik}.",
    "Compassion": "Sesi empati untuk memahami pihak yang terdampak oleh {topik}.",
    "Computational Thinking": "Menyusun algoritma atau langkah sistematis solusi {topik}."
}

# Antarmuka Pengguna (UI)
st.title("🚀 Pembuat Perangkat Pembelajaran Mendalam")
st.subheader("Kurikulum Merdeka - 8 Dimensi Lulusan")

with st.sidebar:
    st.header("Konfigurasi Modul")
    mapel = st.text_input("Mata Pelajaran", "IPA / IPS")
    fase = st.selectbox("Fase", ["A", "B", "C", "D", "E", "F"])
    topik = st.text_input("Topik Pembelajaran", "Perubahan Iklim")
    submit = st.button("Generate Modul")

if submit:
    st.success(f"Modul Ajar untuk Topik: {topik} berhasil dibuat!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Identitas Modul")
        st.write(f"**Mapel:** {mapel}")
        st.write(f"**Fase:** {fase}")
        st.write(f"**Topik:** {topik}")
        
        st.markdown("---")
        st.markdown("### 🎯 Langkah Pembelajaran (Deep Learning)")
        for dim, deskripsi in dimensi_data.items():
            st.info(f"**{dim}:** {deskripsi.format(topik=topik)}")

    with col2:
        st.markdown("### 📊 Rubrik Asesmen 8 Dimensi")
        for dim in dimensi_data.keys():
            st.checkbox(f"Evaluasi Dimensi {dim}")
        
        st.download_button(
            label="Unduh Modul (Teks)",
            data=f"Modul Ajar: {topik}\nFase: {fase}\nMapel: {mapel}\n\nLangkah Deep Learning tersedia.",
            file_name=f"Modul_{topik}.txt"
        )
else:
    st.info("Masukkan data di samping kiri dan klik 'Generate Modul' untuk memulai.")
