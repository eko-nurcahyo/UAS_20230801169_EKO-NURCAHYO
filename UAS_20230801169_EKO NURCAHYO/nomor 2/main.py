# main.py

import tkinter as tk
from tkinter import messagebox
from bangun_datar import *

def hitung_luas_keliling():
    bangun_datar = selected_bangun.get()
    
    if bangun_datar == "Segi Empat":
        sisi = float(ent_sisi.get())
        luas = luas_segi_empat(sisi)
        keliling = keliling_segi_empat(sisi)
    elif bangun_datar == "Persegi Panjang":
        panjang = float(ent_panjang.get())
        lebar = float(ent_lebar.get())
        luas = luas_persegi_panjang(panjang, lebar)
        keliling = keliling_persegi_panjang(panjang, lebar)
    elif bangun_datar == "Segitiga":
        alas = float(ent_alas.get())
        tinggi = float(ent_tinggi.get())
        sisi_a = float(ent_sisi_a.get())
        sisi_b = float(ent_sisi_b.get())
        sisi_c = float(ent_sisi_c.get())
        luas = luas_segitiga(alas, tinggi)
        keliling = keliling_segitiga(sisi_a, sisi_b, sisi_c)
    elif bangun_datar == "Lingkaran":
        jari_jari = float(ent_jari_jari.get())
        luas = luas_lingkaran(jari_jari)
        keliling = keliling_lingkaran(jari_jari)
    else:
        messagebox.showerror("Error", "Pilih bangun datar yang valid.")
        return

    result_str = f"Luas {bangun_datar}: {luas:.2f}\nKeliling {bangun_datar}: {keliling:.2f}"
    messagebox.showinfo("Hasil", result_str)

# Setup GUI
root = tk.Tk()
root.title("Perhitungan Bangun Datar")

selected_bangun = tk.StringVar()
selected_bangun.set("Segi Empat")

bangun_options = ["Segi Empat", "Persegi Panjang", "Segitiga", "Lingkaran"]

tk.Label(root, text="Pilih Bangun Datar:", anchor="w", width=20).grid(row=0, column=0, padx=10, pady=5)
option_menu = tk.OptionMenu(root, selected_bangun, *bangun_options)
option_menu.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Sisi:", anchor="w", width=20).grid(row=1, column=0, padx=10, pady=5)
ent_sisi = tk.Entry(root, width=30)
ent_sisi.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Panjang:", anchor="w", width=20).grid(row=2, column=0, padx=10, pady=5)
ent_panjang = tk.Entry(root, width=30)
ent_panjang.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Lebar:", anchor="w", width=20).grid(row=3, column=0, padx=10, pady=5)
ent_lebar = tk.Entry(root, width=30)
ent_lebar.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Alas:", anchor="w", width=20).grid(row=4, column=0, padx=10, pady=5)
ent_alas = tk.Entry(root, width=30)
ent_alas.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Tinggi:", anchor="w", width=20).grid(row=5, column=0, padx=10, pady=5)
ent_tinggi = tk.Entry(root, width=30)
ent_tinggi.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Sisi A:", anchor="w", width=20).grid(row=6, column=0, padx=10, pady=5)
ent_sisi_a = tk.Entry(root, width=30)
ent_sisi_a.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Sisi B:", anchor="w", width=20).grid(row=7, column=0, padx=10, pady=5)
ent_sisi_b = tk.Entry(root, width=30)
ent_sisi_b.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Sisi C:", anchor="w", width=20).grid(row=8, column=0, padx=10, pady=5)
ent_sisi_c = tk.Entry(root, width=30)
ent_sisi_c.grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="Jari-jari:", anchor="w", width=20).grid(row=9, column=0, padx=10, pady=5)
ent_jari_jari = tk.Entry(root, width=30)
ent_jari_jari.grid(row=9, column=1, padx=10, pady=5)

tk.Button(root, text="Hitung", command=hitung_luas_keliling).grid(row=10, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
