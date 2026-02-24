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

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def show_welcome_page(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#121212")
        self.current_frame.pack(expand=True, fill="both")
        tk.Label(self.current_frame, text="WELCOME TO OWLTASKS", fg="white", bg="#121212",
                 font=("Arial", 16, "bold")).pack(pady=40)
        tk.Label(self.current_frame, text="Reduce stress and stay focused\non what matters most.", fg="#bbbbbb",
                 bg="#121212", font=("Arial", 11)).pack(pady=10)
        self.create_visible_button(self.current_frame, "GET STARTED", self.show_auth_page).pack(pady=30)

    def show_auth_page(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#121212")
        self.current_frame.pack(expand=True, fill="both")
        tk.Label(self.current_frame, text="SIGN IN", fg="white", bg="#121212", font=("Arial", 14, "bold")).pack(pady=20)
        tk.Label(self.current_frame, text="Email:", fg="white", bg="#121212").pack(pady=5)
        tk.Entry(self.current_frame, width=30).pack()
        tk.Label(self.current_frame, text="Password:", fg="white", bg="#121212").pack(pady=5)
        tk.Entry(self.current_frame, show="*", width=30).pack()
        self.create_visible_button(self.current_frame, "LOGIN", self.show_dashboard, width=15).pack(pady=25)
        self.create_visible_button(self.current_frame, "BACK", self.show_welcome_page, width=10).pack()

    def show_dashboard(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#121212")
        self.current_frame.pack(expand=True, fill="both")

        header = tk.Frame(self.current_frame, bg="#121212")
        header.pack(fill="x", padx=10, pady=10)
        tk.Label(header, text="MY TASKS", fg="white", bg="#121212", font=("Arial", 14, "bold")).pack(side="left")
        self.create_visible_button(header, "?", self.show_help_page, width=3).pack(side="right")

        self.task_listbox = tk.Listbox(self.current_frame, bg="#1e1e1e", fg="white", width=45, height=12,
                                       font=("Arial", 10))
        self.task_listbox.pack(pady=10, padx=20)
        self.update_task_list()

        self.create_visible_button(self.current_frame, "(+) Add New Task", self.show_add_task_modal, width=25).pack(
            pady=5)
        self.create_visible_button(self.current_frame, "Delete Selected Task", self.confirm_delete, width=25).pack(
            pady=5)

        # El botón para el microservicio
        self.create_visible_button(self.current_frame, "Generate Report JSON", self.request_microservice_report,
                                   width=25).pack(pady=20)

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"  [{task['priority']}] {task['title']}")

    def confirm_delete(self):
        selection = self.task_listbox.curselection()
        if selection and messagebox.askyesno("Confirm Deletion", "Are you sure?"):
            self.tasks.pop(selection[0])
            self.update_task_list()

    def show_add_task_modal(self):
        modal = tk.Toplevel(self.root)
        modal.title("Create Task")
        modal.geometry("300x350")
        modal.configure(bg="#1e1e1e")
        tk.Label(modal, text="Task Title:", fg="white", bg="#1e1e1e").pack(pady=10)
        title_entry = tk.Entry(modal, width=25)
        title_entry.pack()
        tk.Label(modal, text="Select Priority:", fg="white", bg="#1e1e1e").pack(pady=10)
        priority_cb = ttk.Combobox(modal, values=["High", "Medium", "Low"], state="readonly")
        priority_cb.set("Medium")
        priority_cb.pack()

        def save():
            if title_entry.get():
                self.tasks.append({"title": title_entry.get(), "priority": priority_cb.get()})
                self.update_task_list()
                modal.destroy()

        self.create_visible_button(modal, "SAVE TASK", save, width=15).pack(pady=30)

    def show_help_page(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#121212")
        self.current_frame.pack(expand=True, fill="both")
        tk.Label(self.current_frame, text="HELP & GUIDES", fg="white", bg="#121212", font=("Arial", 14, "bold")).pack(
            pady=20)
        self.create_visible_button(self.current_frame, "RETURN TO DASHBOARD", self.show_dashboard, width=25).pack(
            pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = OwlTasksApp(root)
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.mainloop()