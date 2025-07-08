import tkinter as tk
from tkinter import ttk, messagebox
import requests
import os
import webbrowser
from fastapi import APIRouter
from backend.db import get_db_connection
router = APIRouter()


@router.get("/archive")
def get_file_list():
    # Your logic to fetch file paths and details from DB
    return {"message": "Archive endpoint working"}


class ArchiveWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("📁 Reports Archive")
        self.geometry("900x500")
        self.configure(bg="white")

        tk.Label(self, text="📁 Uploaded Reports Archive", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("Vendor", "Category", "Date", "File Path"), show="headings")
        for col in ("Vendor", "Category", "Date", "File Path"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200 if col != "File Path" else 300)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Button(self, text="🔄 Refresh", bg="#3498DB", fg="white", command=self.load_data).pack(pady=5)
        tk.Button(self, text="📂 Open Selected File", bg="#2ECC71", fg="white", command=self.open_selected_file).pack(pady=5)

        self.load_data()

    def load_data(self):
        try:
            self.tree.delete(*self.tree.get_children())
            response = requests.get("http://127.0.0.1:8000/archives")
            data = response.json()
            for row in data:
                self.tree.insert("", "end", values=(row["vendor"], row["category"], row["invoice_date"], row["file_path"]))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load archive:\n{e}")

    def open_selected_file(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a file.")
            return
        file_path = self.tree.item(selected[0], "values")[3]
        if os.path.exists(file_path):
            webbrowser.open(file_path)
        else:
            messagebox.showerror("Error", f"File not found:\n{file_path}")
