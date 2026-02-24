import tkinter as tk
from tkinter import messagebox, ttk
import json


class OwlTasksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OwlTasks - Milestone 1")
        self.root.geometry("400x600")
        self.root.configure(bg="#121212")

        self.tasks = []
        self.current_frame = None

        self.BTN_WHITE = "white"
        self.TEXT_DARK = "#333333"

        self.show_welcome_page()

    def request_microservice_report(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "The task list is empty. Add tasks first!")
            return

        data_to_send = {
            "user_name": "Jaime Alvarado",
            "tasks": self.tasks
        }

        try:
            with open('report_request.json', 'w') as file:
                json.dump(data_to_send, file, indent=4)

            messagebox.showinfo("Success",
                                "File 'report_request.json' created!\nYour teammate's microservice can now read it.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not create JSON: {e}")

    def create_visible_button(self, parent, text, command, width=20):
        btn = tk.Label(parent, text=text, bg=self.BTN_WHITE, fg=self.TEXT_DARK,
                       font=("Arial", 11, "bold"), width=width, pady=8,
                       cursor="hand2", relief="raised", borderwidth=1)
        btn.bind("<Button-1>", lambda event: command())
        return btn