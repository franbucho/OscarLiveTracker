import tkinter as tk
from tkinter import messagebox, simpledialog
import time

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

    def setup_ui(self):
        tk.Label(self.root, text="Premios Entregados", bg="#1e1e2e", fg="#cdd6f4", font=("Helvetica", 16)).pack(pady=10)
        
        self.delivered_listbox = tk.Listbox(self.root, bg="#313244", fg="#a6e3a1", font=("Helvetica", 12), height=8)
        self.delivered_listbox.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Button(self.root, text="Editar Premio Entregado", command=self.edit_delivered_award, bg="#f9e2af", fg="#1e1e2e", font=("Helvetica", 14)).pack(pady=5)
        
        tk.Label(self.root, text="Próximos Premios", bg="#1e1e2e", fg="#cdd6f4", font=("Helvetica", 16)).pack(pady=10)
        
        self.pending_listbox = tk.Listbox(self.root, bg="#313244", fg="#f9e2af", font=("Helvetica", 12), height=8)
        self.pending_listbox.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Button(self.root, text="Mover a Entregados", command=self.move_to_delivered, bg="#89b4fa", fg="#1e1e2e", font=("Helvetica", 14)).pack(pady=10)
        
        frame = tk.Frame(self.root, bg="#1e1e2e")
        frame.pack(pady=10)
        
        tk.Label(frame, text="Agregar Premio Entregado:", bg="#1e1e2e", fg="#cdd6f4", font=("Helvetica", 14)).grid(row=0, column=0, padx=10)
        self.delivered_entry = tk.Entry(frame, bg="#313244", fg="#f5c2e7", font=("Helvetica", 12), width=30)
        self.delivered_entry.grid(row=0, column=1, padx=10)
        
        tk.Label(frame, text="Agregar Premio Pendiente:", bg="#1e1e2e", fg="#cdd6f4", font=("Helvetica", 14)).grid(row=0, column=2, padx=10)
        self.pending_entry = tk.Entry(frame, bg="#313244", fg="#f5c2e7", font=("Helvetica", 12), width=30)
        self.pending_entry.grid(row=0, column=3, padx=10)
        
        tk.Button(self.root, text="Actualizar", command=self.update_awards, bg="#f38ba8", fg="#1e1e2e", font=("Helvetica", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Mensaje en vivo:", bg="#1e1e2e", fg="#cdd6f4", font=("Helvetica", 16)).pack(pady=10)
        self.message_entry = tk.Entry(self.root, bg="#313244", fg="#f5c2e7", font=("Helvetica", 12), width=50)
        self.message_entry.pack(pady=10)
        
        self.timer_label = tk.Label(self.root, text="Tiempo en vivo: 00:00:00", bg="#1e1e2e", fg="#fab387", font=("Helvetica", 16))
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

if __name__ == "__main__":
    root = tk.Tk()
    app = OscarTrackerApp(root)
    root.mainloop()
