import tkinter as tk
from tkinter import filedialog


class NotDefteri_MKYLisasn:
    def __init__(self, root):
        self.root = root
        self.root.title("MKYLisans Not Defteri")
        self.metin_alani = tk.Text(root, wrap="word", undo=True, maxundo=-1)
        self.metin_alani.pack(expand="yes", fill="both")

        # Menü oluştur
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Dosya Menüsü
        dosya_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Dosya", menu=dosya_menu)
        dosya_menu.add_command(label="Yeni", command=self.yeni_not_MKYLisans)
        dosya_menu.add_command(label="Aç", command=self.not_ac_MKYLisasn)
        dosya_menu.add_command(label="Kaydet", command=self.not_kaydet_MKYLisasn)
        dosya_menu.add_separator()
        dosya_menu.add_command(label="Çıkış", command=root.destroy)

    def yeni_not_MKYLisans(self):
        self.metin_alani.delete(1.0, tk.END)

    def not_ac_MKYLisasn(self):
        dosya_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
        if dosya_path:
            with open(dosya_path, "r") as dosya:
                icerik = dosya.read()
                self.metin_alani.delete(1.0, tk.END)
                self.metin_alani.insert(tk.END, icerik)

    def not_kaydet_MKYLisasn(self):
        dosya_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
        if dosya_path:
            with open(dosya_path, "w") as dosya:
                dosya.write(self.metin_alani.get(1.0, tk.END))


if __name__ == "__main__":
    root = tk.Tk()
    not_defteri = NotDefteri_MKYLisasn(root)
    root.mainloop()
