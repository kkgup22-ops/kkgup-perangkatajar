import datetime

class ModulAjarGenerator:
    def __init__(self, topik, fase, mapel):
        self.topik = topik
        self.fase = fase
        self.mapel = mapel
        self.dimensi_8 = {
            "Character": "Refleksi nilai moral dan tanggung jawab pribadi terhadap materi.",
            "Citizenship": "Menghubungkan topik dengan peran siswa sebagai warga masyarakat/global.",
            "Collaboration": "Kerja kelompok untuk memecahkan masalah kompleks.",
            "Communication": "Presentasi hasil pemikiran menggunakan media kreatif.",
            "Creativity": "Membuat produk atau solusi orisinal dari hasil belajar.",
            "Critical Thinking": "Menganalisis data, fakta, dan argumen secara mendalam.",
            "Compassion": "Menumbuhkan empati terhadap isu kemanusiaan/lingkungan terkait topik.",
            "Computational Thinking": "Menggunakan logika urutan (algoritma) atau dekomposisi masalah."
        }

    def buat_modul(self, tp):
        print(f"\n{'='*50}")
        print(f"MODUL AJAR KURIKULUM MERDEKA (DEEP LEARNING)")
        print(f"{'='*50}")
        print(f"Topik          : {self.topik}")
        print(f"Mata Pelajaran : {self.mapel}")
        print(f"Fase           : {self.fase}")
        print(f"Tanggal        : {datetime.date.today()}")
        print(f"\nTujuan Pembelajaran (TP):\n- {tp}")
        
        print(f"\n{'-'*20} STRATEGI 8 DIMENSI LULUSAN {'-'*20}")
        for dimensi, aktivitas in self.dimensi_8.items():
            print(f"[{dimensi}] -> {aktivitas}")
        
        print(f"\n{'-'*50}")
        print("Modul berhasil dibuat. Siap diimplementasikan!")

# --- CARA PENGGUNAAN ---
print("--- Generator Perangkat Pembelajaran Mendalam ---")
topik_input = input("Masukkan Topik Pembelajaran: ")
tp_input = input("Masukkan Tujuan Pembelajaran: ")

app = ModulAjarGenerator(topik_input, "Fase E", "IPA/IPS")
app.buat_modul(tp_input)
