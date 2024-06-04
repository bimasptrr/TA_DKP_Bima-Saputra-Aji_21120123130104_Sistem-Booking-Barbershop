from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.font import Font

class AplikasiBarbershop:
    def __init__(self, root):
        self.root = root
        self.root.title("Pemesanan Barbershop")
        self.root.geometry("600x800")
        self.root.configure(background="light gray")
        
        self.font_style = Font(family="Sans Serif", size=16, weight="bold")
        
        self.frame_utama = Frame(self.root, background="light gray")
        self.frame_utama.pack(padx=20, pady=20, fill='both', expand=True)
        
        Label(self.frame_utama, text="BIMZZ BARBERSHOP", font=self.font_style, background="light gray", foreground="black").pack(pady=10)
        
        self.isian = ["Nama", "No. Telepon", "Jenis Layanan","Tukang Cukur", "Tanggal", "Bulan", "Waktu", "Metode Pembayaran"]
        self.entri = {}
        self.buat_form()
        
        Button(self.frame_utama, text="Booking", font=self.font_style, background="black", foreground="white", command=self.kirim_pemesanan).pack(pady=20)
    
    def buat_form(self):
        for isian in self.isian:
            Label(self.frame_utama, text=f"{isian}:", font=self.font_style, background="light gray", foreground="black").pack()
            
            if isian == "Jenis Layanan":
                nilai = ["Cukur Rambut (Rp.30.000)", "Smoothing (Rp.100.000)", "Cat Rambut (Rp.70.000)", "Paket Komplit (Rp.180.000)"]
            elif isian == "Tukang Cukur":
                nilai = ["Tukang Cukur A", "Tukang Cukur B", "Tukang Cukur C", "Tukang Cukur D"]
            elif isian == "Tanggal":
                nilai = [int(i) for i in range(1, 31)]
            elif isian == "Bulan":
                nilai = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
            elif isian == "Waktu":
                nilai = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
            elif isian == "Metode Pembayaran":
                nilai = ["Tunai", "Kredit", "Debit", "E-Wallet"]
            else:
                nilai = None
            
            if nilai:
                self.entri[isian] = ttk.Combobox(self.frame_utama, values=nilai, font=self.font_style, state="readonly")
                self.entri[isian].current(0)
            else:
                if isian == "No. Telepon":
                    self.entri[isian] = Entry(self.frame_utama, font=self.font_style, background="white", foreground="black", validate="key")
                    self.entri[isian].config(validatecommand=(self.root.register(self.validasi_nomor), '%P'))
                elif isian == "Nama":
                    self.entri[isian] = Entry(self.frame_utama, font=self.font_style, background="white", foreground="black", validate="key")
                    self.entri[isian].config(validatecommand=(self.root.register(self.validasi_huruf), '%P'))
                else:
                    self.entri[isian] = Entry(self.frame_utama, font=self.font_style, background="white", foreground="black")
                
            self.entri[isian].pack()

    def validasi_nomor(self, nilai):
        if nilai.isdigit() or nilai == "":
            return True
        showinfo("Input Tidak Valid", "Nomor telepon hanya boleh berisi angka.")
        return False

    def validasi_huruf(self, nilai):
        if nilai.isalpha() or nilai == "":
            return True
        showinfo("Input Tidak Valid", "Nama hanya boleh berisi huruf.")
        return False

    def kirim_pemesanan(self):
        if not all([self.entri[isian].get() for isian in self.entri]):
            showinfo("Pemesanan Gagal", "Semua data harus diisi!")
            return

        detail = {isian: self.entri[isian].get() for isian in self.entri}
        showinfo("Pemesanan Berhasil", "Pemesanan Anda berhasil. Terima kasih telah menggunakan layanan kami.")
        self.tampilkan_detail_pemesanan(detail)

    def tampilkan_detail_pemesanan(self, detail):
        jendela_detail = Toplevel(self.root)
        jendela_detail.title("Detail Pemesanan")
        jendela_detail.geometry("500x400")
        jendela_detail.configure(background="light gray")
        
        for kunci, nilai in detail.items():
            Label(jendela_detail, text=f"{kunci}: {nilai}", font=self.font_style, background="white").pack()

if __name__ == "__main__":
    root = Tk()
    app = AplikasiBarbershop(root)
    root.mainloop()
