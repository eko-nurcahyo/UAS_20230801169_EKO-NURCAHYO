import tkinter as tk
from tkinter import messagebox, simpledialog
from barang import *

barang_list = []

def input_data_barang():
    nama = simpledialog.askstring("Input", "Masukkan Nama Barang:")
    if not nama:
        return
    harga = simpledialog.askfloat("Input", "Masukkan Harga Barang:")
    if harga is None:
        return
    stok = simpledialog.askinteger("Input", "Masukkan Stok Barang:")
    if stok is None:
        return
    
    barang = Barang(nama, harga, stok)
    barang_list.append(barang)
    messagebox.showinfo("Sukses", f"Barang '{nama}' berhasil ditambahkan.")

def tampil_data_barang():
    if not barang_list:
        messagebox.showinfo("Data Barang", "Tidak ada data barang.")
        return
    
    result_str = "\n--- Daftar Barang ---\n"
    for barang in barang_list:
        result_str += f"Nama: {barang.nama}, Harga: Rp. {barang.harga:,.0f}, Stok: {barang.stok}\n"
    
    messagebox.showinfo("Data Barang", result_str)

def delete_data_barang():
    nama = simpledialog.askstring("Input", "Masukkan Nama Barang yang akan dihapus:")
    if not nama:
        return
    
    for barang in barang_list:
        if barang.nama == nama:
            barang_list.remove(barang)
            messagebox.showinfo("Sukses", f"Barang '{nama}' berhasil dihapus.")
            return
    
    messagebox.showerror("Error", f"Barang '{nama}' tidak ditemukan.")

def cari_data_barang():
    nama = simpledialog.askstring("Input", "Masukkan Nama Barang yang dicari:")
    if not nama:
        return
    
    for barang in barang_list:
        if barang.nama == nama:
            result_str = f"Nama: {barang.nama}\nHarga: Rp. {barang.harga:,.0f}\nStok: {barang.stok}"
            messagebox.showinfo("Data Barang", result_str)
            return
    
    messagebox.showerror("Error", f"Barang '{nama}' tidak ditemukan.")

def hitung_jumlah_pembelian():
    nama = simpledialog.askstring("Input", "Masukkan Nama Barang yang dibeli:")
    if not nama:
        return
    jumlah = simpledialog.askinteger("Input", "Masukkan Jumlah Barang yang dibeli:")
    if jumlah is None:
        return
    
    for barang in barang_list:
        if barang.nama == nama:
            if jumlah > barang.stok:
                messagebox.showerror("Error", "Stok barang tidak mencukupi.")
                return
            
            total_harga = jumlah * barang.harga
            barang.stok -= jumlah
            messagebox.showinfo("Total Pembelian", f"Total Harga: Rp. {total_harga:,.0f}\nStok Tersisa: {barang.stok}")
            return
    
    messagebox.showerror("Error", f"Barang '{nama}' tidak ditemukan.")

root = tk.Tk()
root.title("Manajemen Barang dan Penjualan")

tk.Button(root, text="Input Data Barang", command=input_data_barang).grid(row=0, column=0, padx=10, pady=5)
tk.Button(root, text="Tampil Data Barang", command=tampil_data_barang).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Delete Data Barang", command=delete_data_barang).grid(row=1, column=0, padx=10, pady=5)
tk.Button(root, text="Cari Data Barang", command=cari_data_barang).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Hitung Jumlah Pembelian", command=hitung_jumlah_pembelian).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
