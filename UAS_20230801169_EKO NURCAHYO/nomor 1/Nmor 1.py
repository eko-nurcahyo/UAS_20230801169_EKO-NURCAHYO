import tkinter as tk
from tkinter import messagebox

# Data kamar
kamar = {
    'M': ('Melati', 650000),
    'S': ('Sakura', 550000),
    'L': ('Lily', 400000),
    'A': ('Anggrek', 350000)
}

def hitung_pembayaran(nama_petugas, nama_customer, tanggal_check_in, kode_kamar, lama_sewa, uang_bayar):
    if kode_kamar not in kamar:
        return "Kode kamar tidak valid."
    
    nama_kamar, harga_per_malam = kamar[kode_kamar]
    total_sewa = harga_per_malam * lama_sewa
    
    # Penerapan diskon
    if lama_sewa > 5:
        diskon = 0.10
    elif lama_sewa > 3:
        diskon = 0.05
    else:
        diskon = 0.0
    
    jumlah_diskon = total_sewa * diskon
    total_sewa -= jumlah_diskon
    
    # Penerapan pajak
    tarif_pajak = 0.10
    pajak = tarif_pajak * total_sewa
    
    total_bayar = total_sewa + pajak
    uang_kembali = uang_bayar - total_bayar
    
    return {
        "Nama Petugas": nama_petugas,
        "Nama Customer": nama_customer,
        "Tanggal Check-in": tanggal_check_in,
        "Nama Kamar": nama_kamar,
        "Harga per Malam": harga_per_malam,
        "Lama Sewa": lama_sewa,
        "PPN 10%": pajak,
        "Jumlah Bayar": total_sewa,
        "Total Bayar": total_bayar,
        "Uang Bayar": uang_bayar,
        "Uang Kembali": uang_kembali
    }

def hitung():
    nama_petugas = ent_nama_petugas.get()
    nama_customer = ent_nama_customer.get()
    tanggal_check_in = ent_tanggal_check_in.get()
    kode_kamar = ent_kode_kamar.get().upper()
    lama_sewa = int(ent_lama_sewa.get())
    uang_bayar = float(ent_uang_bayar.get())
    
    hasil = hitung_pembayaran(nama_petugas, nama_customer, tanggal_check_in, kode_kamar, lama_sewa, uang_bayar)
    
    if isinstance(hasil, dict):
        result_str =          f"Bukti Pemesanan Kamar\n"
        result_str +=           f"Hotel 'SEJUK ASRI'\n"
        result_str += f"=======================================\n\n"
        result_str += f"Nama Petugas: {hasil['Nama Petugas']}\n"
        result_str += f"Nama Customer: {hasil['Nama Customer']}\n"
        result_str += f"Tanggal Check-in: {hasil['Tanggal Check-in']}\n"
        result_str += f"=======================================\n"
        result_str += f"Nama Kamar yang dipesan: {hasil['Nama Kamar']}\n"
        result_str += f"Harga sewa per malam: Rp. {hasil['Harga per Malam']:,.0f}\n"
        result_str += f"Lama sewa: {hasil['Lama Sewa']} hari\n"
        result_str += f"PPN 10%: Rp. {hasil['PPN 10%']:,.0f}\n"
        result_str += f"Jumlah bayar: Rp. {hasil['Jumlah Bayar']:,.0f}\n"
        result_str += f"Total bayar: Rp. {hasil['Total Bayar']:,.0f}\n"
        result_str += f"Uang bayar: Rp. {hasil['Uang Bayar']:,.0f}\n"
        result_str += f"Uang kembali: Rp. {hasil['Uang Kembali']:,.0f}\n"
        messagebox.showinfo("Hasil", result_str)
    else:
        messagebox.showerror("Error", hasil)

# Setup GUI
root = tk.Tk()
root.title("Pemesanan Kamar Hotel 'SEJUK ASRI'")

tk.Label(root, text="Hotel 'SEJUK ASRI'", font=("Arial", 14)).grid(row=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Input Nama Petugas:", anchor="w", width=20).grid(row=1, column=0, padx=10, pady=5, sticky="w")
ent_nama_petugas = tk.Entry(root, width=30)
ent_nama_petugas.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Input Nama Customer:", anchor="w", width=20).grid(row=2, column=0, padx=10, pady=5, sticky="w")
ent_nama_customer = tk.Entry(root, width=30)
ent_nama_customer.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Input Tanggal Check-in:", anchor="w", width=20).grid(row=3, column=0, padx=10, pady=5, sticky="w")
ent_tanggal_check_in = tk.Entry(root, width=30)
ent_tanggal_check_in.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Pilih Kode Kamar (M/S/L/A):", anchor="w", width=20).grid(row=4, column=0, padx=10, pady=5, sticky="w")
ent_kode_kamar = tk.Entry(root, width=30)
ent_kode_kamar.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Input Lama Sewa:", anchor="w", width=20).grid(row=5, column=0, padx=10, pady=5, sticky="w")
ent_lama_sewa = tk.Entry(root, width=30)
ent_lama_sewa.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Jumlah Uang Bayar:", anchor="w", width=20).grid(row=6, column=0, padx=10, pady=5, sticky="w")
ent_uang_bayar = tk.Entry(root, width=30)
ent_uang_bayar.grid(row=6, column=1, padx=10, pady=5)

tk.Button(root, text="Hitung", command=hitung).grid(row=7, columnspan=2, padx=10, pady=10)

root.mainloop()
