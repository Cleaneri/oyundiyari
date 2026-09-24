import tkinter as tk

# Ana pencereyi oluşturuyoruz
pencere = tk.Tk()
pencere.title("Uygulama")
pencere.geometry("300x150")  # Pencere boyutu (Genişlik x Yükseklik)

# Ekrana yazılacak metin (Etiket)
yazi = tk.Label(pencere, text="Yakında birçok oyun olacak.", font=("Arial", 12))
yazi.pack(pady=20)  # pady: Üstten ve alttan bırakılacak boşluk

# Kapatma butonu
# command=pencere.destroy ifadesi butona basılınca pencereyi kapatır
kapat_butonu = tk.Button(pencere, text="Kapat", command=pencere.destroy, bg="red", fg="white", font=("Arial", 10, "bold"))
kapat_butonu.pack(pady=10)

# Pencerenin ekranda kalmasını sağlayan döngü
pencere.mainloop()
