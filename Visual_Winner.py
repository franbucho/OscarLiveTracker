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

        # Create the second window
        self.create_second_window()

    def setup_ui(self):
        tk.Label(self.root, text="Delivered Awards", bg="#1e1e2e", fg="white", font=("Georgia", 16, "bold")).pack(pady=10)
        
        self.delivered_listbox = tk.Listbox(self.root, bg="#1e1e2e", fg="white", font=("Georgia", 12), height=8, bd=0)
        self.delivered_listbox.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Button(self.root, text="Edit Delivered Award", command=self.edit_delivered_award, bg="#f9e2af", fg="#1e1e2e", font=("Georgia", 14, "bold")).pack(pady=5)
        
        tk.Label(self.root, text="Upcoming Awards", bg="#1e1e2e", fg="white", font=("Georgia", 16, "bold")).pack(pady=10)
        
        self.pending_listbox = tk.Listbox(self.root, bg="#1e1e2e", fg="white", font=("Georgia", 12), height=8, bd=0)
        self.pending_listbox.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Button(self.root, text="Move to Delivered", command=self.move_to_delivered, bg="#89b4fa", fg="#1e1e2e", font=("Georgia", 14, "bold")).pack(pady=10)
        
        frame = tk.Frame(self.root, bg="#1e1e2e")
        frame.pack(pady=10)
        
        tk.Label(frame, text="Add Delivered Award:", bg="#1e1e2e", fg="white", font=("Georgia", 14, "bold")).grid(row=0, column=0, padx=10)
        self.delivered_entry = tk.Entry(frame, bg="#313244", fg="#f5c2e7", font=("Georgia", 12), width=30)
        self.delivered_entry.grid(row=0, column=1, padx=10)
        
        tk.Label(frame, text="Add Pending Award:", bg="#1e1e2e", fg="white", font=("Georgia", 14, "bold")).grid(row=0, column=2, padx=10)
        self.pending_entry = tk.Entry(frame, bg="#313244", fg="#f5c2e7", font=("Georgia", 12), width=30)
        self.pending_entry.grid(row=0, column=3, padx=10)
        
        tk.Button(self.root, text="Update", command=self.update_awards, bg="#f38ba8", fg="#1e1e2e", font=("Georgia", 14, "bold")).pack(pady=10)
        
        tk.Label(self.root, text="Live Message:", bg="#1e1e2e", fg="white", font=("Georgia", 16, "bold")).pack(pady=10)
        self.message_entry = tk.Entry(self.root, bg="#313244", fg="#f5c2e7", font=("Georgia", 12), width=50)
        self.message_entry.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="Live Time: 00:00:00", bg="#1e1e2e", fg="white", font=("Georgia", 16, "bold"))
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
        
        messagebox.showinfo("Update", "Awards updated. Ready for the stream!")

    def move_to_delivered(self):
        try:
            selected_index = self.pending_listbox.curselection()[0]
            award = self.pending_listbox.get(selected_index)
            
            winner = simpledialog.askstring("Award Winner", f"Who won the '{award}' award?")
            if not winner:
                return
            
            award_with_winner = f"{award} - {winner}"
            
            self.pending_listbox.delete(selected_index)
            self.delivered_listbox.insert(tk.END, award_with_winner)
            
            self.pending_awards.remove(award)
            self.delivered_awards.append(award_with_winner)
        except IndexError:
            messagebox.showwarning("Select Award", "Please select an award to move to delivered.")

    def edit_delivered_award(self):
        try:
            selected_index = self.delivered_listbox.curselection()[0]
            current_award = self.delivered_listbox.get(selected_index)
            new_award = simpledialog.askstring("Edit Award", f"Edit '{current_award}' to:")
            
            if new_award:
                self.delivered_listbox.delete(selected_index)
                self.delivered_listbox.insert(selected_index, new_award)
                self.delivered_awards[selected_index] = new_award
        except IndexError:
            messagebox.showwarning("Select Award", "Please select an award to edit.")

    def update_timer(self):
        current_time = time.strftime("%H:%M:%S")
        self.timer_label.config(text=f"Live Time: {current_time}")
        self.root.after(1000, self.update_timer)

    def create_second_window(self):
        # Define golden color for the live tracking window
        golden_color = "#ffd700"
        
        # Check if the image exists in the path
        file_path = r"C:\Users\Admin\Desktop\Code\Oscar  Live Tacker\PNG1.png"
        if os.path.exists(file_path):
            self.bg_image = Image.open(file_path)  # Load the image
            self.bg_image = self.bg_image.resize((900, 800))  # Adjust the size
            self.bg_image = ImageTk.PhotoImage(self.bg_image)  # Convert to a format Tkinter can use
        else:
            messagebox.showerror("Error", f"Image not found at path: {file_path}")
            return

        # Create a new window for live visualization
        second_window = tk.Toplevel(self.root)
        second_window.title("Live Visualization")
        second_window.geometry("900x800")
        
        # Create a canvas and place the background image
        canvas = tk.Canvas(second_window, width=900, height=800)
        canvas.pack(fill="both", expand=True)

        # Place the background image
        canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        # Create the lists in the second window (on top of the background image)
        label_delivered = tk.Label(second_window, text="Delivered Awards", bg="#1e1e2e", fg=golden_color, font=("Georgia", 16, "bold"))
        label_delivered.place(x=20, y=20)

        self.delivered_listbox_display = tk.Listbox(second_window, bg="#1e1e2e", fg=golden_color, font=("Georgia", 12), height=8, bd=0)
        self.delivered_listbox_display.place(x=20, y=60, width=860)

        label_pending = tk.Label(second_window, text="Upcoming Awards", bg="#1e1e2e", fg=golden_color, font=("Georgia", 16, "bold"))
        label_pending.place(x=20, y=300)

        self.pending_listbox_display = tk.Listbox(second_window, bg="#1e1e2e", fg=golden_color, font=("Georgia", 12), height=8, bd=0)
        self.pending_listbox_display.place(x=20, y=340, width=860)

        # Create the label for the live message
        self.live_message_label = tk.Label(second_window, text="", 
                                           bg="black", fg=golden_color, font=("Georgia", 16, "bold"), padx=10, pady=5)
        self.live_message_label.place(x=900, y=760, anchor="e")

        # Fill the lists in the second window
        self.update_visual_display(second_window)

        # Update the visualization every second
        second_window.after(1000, self.update_visual_display, second_window)

        # Move the live message
        self.move_message(second_window)

    def update_visual_display(self, second_window):
        # Update the delivered and pending awards list in the second window
        self.delivered_listbox_display.delete(0, tk.END)
        self.pending_listbox_display.delete(0, tk.END)

        # Fill the lists with the delivered and pending awards
        for award in self.delivered_awards:
            self.delivered_listbox_display.insert(tk.END, award)
        
        for award in self.pending_awards:
            self.pending_listbox_display.insert(tk.END, award)

        # Update the visualization every second
        second_window.after(1000, self.update_visual_display, second_window)

    def move_message(self, second_window):
        # Get the live message text
        live_message = self.message_entry.get()
        
        # If there is no message, hide the label
        if not live_message:
            self.live_message_label.config(text="")
        else:
            # Update the live message text
            self.live_message_label.config(text=live_message)
        
        # Move the live message to the next second
        second_window.after(1000, self.move_message, second_window)

# Running the main window
root = tk.Tk()
app = OscarTrackerApp(root)
root.mainloop()
