import tkinter as tk
from tkinter import messagebox, simpledialog
import time
from PIL import Image, ImageTk
import os

class OscarTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Oscar Live Tracker")
        self.root.geometry("900x800")
        self.root.configure(bg="#1e1e2e")
        
        self.delivered_awards = []
        self.pending_awards = []
        
        self.setup_ui()
        self.update_timer()

        # Crear la segunda ventana
        self.create_second_window()

    def setup_ui(self):
        tk.Label(self.root, text="Premios Entregados", bg="#1e1e2e", fg="white", font=("Georgia", 16, "bold")).pack(pady=10)
        
        self.delivered_listbox = tk.Listbox(self.root, bg="#1e1e2e", fg="white", font=("Georgia", 12), height=8, bd=0)
        self.delivered_listbox.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Button(self.root, text="Editar Premio Entregado", command=self.edit_delivered_award, bg="#f9e2af", fg="#1e1e2e", font=("Georgia", 14, "bold")).pack(pady=5)
        
        tk.Label(self.root, text="Próximos Premios", bg="#1e1e2e", fg="white", font=("Georgia", 16, "bold")).pack(pady=10)
        
        self.pending_listbox = tk.Listbox(self.root, bg="#1e1e2e", fg="white", font=("Georgia", 12), height=8, bd=0)
        self.pending_listbox.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Button(self.root, text="Mover a Entregados", command=self.move_to_delivered, bg="#89b4fa", fg="#1e1e2e", font=("Georgia", 14, "bold")).pack(pady=10)
        
        frame = tk.Frame(self.root, bg="#1e1e2e")
        frame.pack(pady=10)
        
        tk.Label(frame, text="Agregar Premio Entregado:", bg="#1e1e2e", fg="white", font=("Georgia", 14, "bold")).grid(row=0, column=0, padx=10)
        self.delivered_entry = tk.Entry(frame, bg="#313244", fg="#f5c2e7", font=("Georgia", 12), width=30)
        self.delivered_entry.grid(row=0, column=1, padx=10)
        
        tk.Label(frame, text="Agregar Premio Pendiente:", bg="#1e1e2e", fg="white", font=("Georgia", 14, "bold")).grid(row=0, column=2, padx=10)
        self.pending_entry = tk.Entry(frame, bg="#313244", fg="#f5c2e7", font=("Georgia", 12), width=30)
        self.pending_entry.grid(row=0, column=3, padx=10)
        
        tk.Button(self.root, text="Actualizar", command=self.update_awards, bg="#f38ba8", fg="#1e1e2e", font=("Georgia", 14, "bold")).pack(pady=10)
        
        tk.Label(self.root, text="Mensaje en vivo:", bg="#1e1e2e", fg="white", font=("Georgia", 16, "bold")).pack(pady=10)
        self.message_entry = tk.Entry(self.root, bg="#313244", fg="#f5c2e7", font=("Georgia", 12), width=50)
        self.message_entry.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="Tiempo en vivo: 00:00:00", bg="#1e1e2e", fg="white", font=("Georgia", 16, "bold"))
        self.timer_label.pack(pady=10)

    def update_awards(self):
        delivered_award = self.delivered_entry.get()
        pending_award = self.pending_entry.get()
        
        if delivered_award:
            self.delivered_awards.append(delivered_award)
            self.delivered_listbox.insert(tk.END, delivered_award)
            self.delivered_entry.delete(0, tk.END)
        
        if pending_award:
            self.pending_awards.append(pending_award)
            self.pending_listbox.insert(tk.END, pending_award)
            self.pending_entry.delete(0, tk.END)
        
        messagebox.showinfo("Actualizar", "Premios actualizados. ¡Listo para el stream!")

    def move_to_delivered(self):
        try:
            selected_index = self.pending_listbox.curselection()[0]
            award = self.pending_listbox.get(selected_index)
            
            winner = simpledialog.askstring("Ganador del Premio", f"¿Quién ganó el premio '{award}'?")
            if not winner:
                return
            
            award_with_winner = f"{award} - {winner}"
            
            self.pending_listbox.delete(selected_index)
            self.delivered_listbox.insert(tk.END, award_with_winner)
            
            self.pending_awards.remove(award)
            self.delivered_awards.append(award_with_winner)
        except IndexError:
            messagebox.showwarning("Seleccionar Premio", "Por favor, selecciona un premio para mover a entregados.")

    def edit_delivered_award(self):
        try:
            selected_index = self.delivered_listbox.curselection()[0]
            current_award = self.delivered_listbox.get(selected_index)
            new_award = simpledialog.askstring("Editar Premio", f"Editar '{current_award}' a:")
            
            if new_award:
                self.delivered_listbox.delete(selected_index)
                self.delivered_listbox.insert(selected_index, new_award)
                self.delivered_awards[selected_index] = new_award
        except IndexError:
            messagebox.showwarning("Seleccionar Premio", "Por favor, selecciona un premio para editar.")

    def update_timer(self):
        current_time = time.strftime("%H:%M:%S")
        self.timer_label.config(text=f"Tiempo en vivo: {current_time}")
        self.root.after(1000, self.update_timer)

    def create_second_window(self):
        # Definir color dorado para la ventana de seguimiento en vivo
        golden_color = "#ffd700"
        
        # Verificar si la imagen existe en la ruta
        file_path = r"C:\Users\Admin\Desktop\Code\Oscar  Live Tacker\PNG1.png"
        if os.path.exists(file_path):
            self.bg_image = Image.open(file_path)  # Cargar la imagen
            self.bg_image = self.bg_image.resize((900, 800))  # Ajustar el tamaño
            self.bg_image = ImageTk.PhotoImage(self.bg_image)  # Convertir a formato que tkinter puede usar
        else:
            messagebox.showerror("Error", f"Imagen no encontrada en la ruta: {file_path}")
            return

        # Crear una nueva ventana para mostrar la visualización en segundo monitor
        second_window = tk.Toplevel(self.root)
        second_window.title("Visualización en Vivo")
        second_window.geometry("900x800")
        
        # Crear un canvas y colocar la imagen de fondo
        canvas = tk.Canvas(second_window, width=900, height=800)
        canvas.pack(fill="both", expand=True)

        # Colocar la imagen de fondo
        canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        # Crear las listas en la segunda ventana (sobre la imagen de fondo)
        label_delivered = tk.Label(second_window, text="Premios Entregados", bg="#1e1e2e", fg=golden_color, font=("Georgia", 16, "bold"))
        label_delivered.place(x=20, y=20)

        self.delivered_listbox_display = tk.Listbox(second_window, bg="#1e1e2e", fg=golden_color, font=("Georgia", 12), height=8, bd=0)
        self.delivered_listbox_display.place(x=20, y=60, width=860)

        label_pending = tk.Label(second_window, text="Próximos Premios", bg="#1e1e2e", fg=golden_color, font=("Georgia", 16, "bold"))
        label_pending.place(x=20, y=300)

        self.pending_listbox_display = tk.Listbox(second_window, bg="#1e1e2e", fg=golden_color, font=("Georgia", 12), height=8, bd=0)
        self.pending_listbox_display.place(x=20, y=340, width=860)

        # Crear el label para el mensaje en vivo
        self.live_message_label = tk.Label(second_window, text="", 
                                           bg="black", fg=golden_color, font=("Georgia", 16, "bold"), padx=10, pady=5)
        self.live_message_label.place(x=900, y=760, anchor="e")

        # Llenar las listas en la segunda ventana
        self.update_visual_display(second_window)

        # Actualizar la visualización cada 1 segundo
        second_window.after(1000, self.update_visual_display, second_window)

        # Mover el mensaje en vivo
        self.move_message(second_window)

    def update_visual_display(self, second_window):
        # Actualizar la lista de premios entregados y pendientes en la segunda ventana
        self.delivered_listbox_display.delete(0, tk.END)
        self.pending_listbox_display.delete(0, tk.END)

        # Llenar las listas con los premios entregados y pendientes
        for award in self.delivered_awards:
            self.delivered_listbox_display.insert(tk.END, award)
        
        for award in self.pending_awards:
            self.pending_listbox_display.insert(tk.END, award)

        # Actualizar la visualización cada 1 segundo
        second_window.after(1000, self.update_visual_display, second_window)

    def move_message(self, second_window):
        # Obtener el texto del mensaje en vivo
        live_message = self.message_entry.get()
        
        # Si no hay mensaje, ocultar el label
        if not live_message:
            self.live_message_label.config(text="")
        else:
            # Actualizar el texto del mensaje en vivo
            self.live_message_label.config(text=live_message)
            # Mover el texto de derecha a izquierda
            self.live_message_label.place(x=self.live_message_label.winfo_x() - 5, y=self.live_message_label.winfo_y())
        
        second_window.after(100, self.move_message, second_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = OscarTrackerApp(root)
    root.mainloop()
