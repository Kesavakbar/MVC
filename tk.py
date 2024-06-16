import tkinter as tk
from tkinter import messagebox

class HealthCheckApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Cek Kesehatan")

        # Setting warna background
        self.root.configure(bg="#f0f0f0")

        # Frame untuk form input
        self.frame_form = tk.Frame(root, bg="#d3d3d3", bd=5, relief="groove")
        self.frame_form.pack(padx=20, pady=20)

        # Nama
        self.label_name = tk.Label(self.frame_form, text="Nama:", bg="#d3d3d3", font=('Arial', 12))
        self.label_name.grid(row=0, column=0, sticky='e', pady=5)
        self.entry_name = tk.Entry(self.frame_form, font=('Arial', 12))
        self.entry_name.grid(row=0, column=1, pady=5)

        # Umur
        self.label_age = tk.Label(self.frame_form, text="Umur:", bg="#d3d3d3", font=('Arial', 12))
        self.label_age.grid(row=1, column=0, sticky='e', pady=5)
        self.entry_age = tk.Entry(self.frame_form, font=('Arial', 12))
        self.entry_age.grid(row=1, column=1, pady=5)

        # Berat Badan
        self.label_weight = tk.Label(self.frame_form, text="Berat Badan (kg):", bg="#d3d3d3", font=('Arial', 12))
        self.label_weight.grid(row=2, column=0, sticky='e', pady=5)
        self.entry_weight = tk.Entry(self.frame_form, font=('Arial', 12))
        self.entry_weight.grid(row=2, column=1, pady=5)

        # Tinggi Badan
        self.label_height = tk.Label(self.frame_form, text="Tinggi Badan (cm):", bg="#d3d3d3", font=('Arial', 12))
        self.label_height.grid(row=3, column=0, sticky='e', pady=5)
        self.entry_height = tk.Entry(self.frame_form, font=('Arial', 12))
        self.entry_height.grid(row=3, column=1, pady=5)

        # Tombol cek kesehatan
        self.button_check = tk.Button(self.frame_form, text="Cek Kesehatan", command=self.check_health, bg="#4CAF50", fg="white", font=('Arial', 12, 'bold'))
        self.button_check.grid(row=4, columnspan=2, pady=10)

        # Area hasil
        self.label_result = tk.Label(root, text="Hasil Pengecekan:", bg="#f0f0f0", font=('Arial', 14, 'bold'))
        self.label_result.pack()
        self.text_result = tk.Text(root, height=10, width=50, font=('Arial', 12), bg="#ffffff", bd=5, relief="sunken")
        self.text_result.pack(padx=20, pady=20)

    def check_health(self):
        # Ambil data dari entry
        name = self.entry_name.get()
        age = self.entry_age.get()
        weight = self.entry_weight.get()
        height = self.entry_height.get()

        try:
            age = int(age)
            weight = float(weight)
            height = float(height) / 100  # Convert cm to meters
        except ValueError:
            messagebox.showerror("Input Error", "Pastikan semua data diisi dengan benar.")
            return

        # Perhitungan BMI
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            status = "Kekurangan berat badan (Kurus)"
        elif 18.5 <= bmi < 24.9:
            status = "Berat badan normal"
        elif 25 <= bmi < 29.9:
            status = "Kelebihan berat badan (Gemuk)"
        else:
            status = "Obesitas"

        # Tampilkan hasil
        result = (f"Nama: {name}\n"
                  f"Umur: {age} tahun\n"
                  f"Berat Badan: {weight:.2f} kg\n"
                  f"Tinggi Badan: {height * 100:.2f} cm\n"
                  f"BMI: {bmi:.2f}\n"
                  f"Status: {status}")
        
        self.text_result.delete("1.0", tk.END)
        self.text_result.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthCheckApp(root)
    root.mainloop()
