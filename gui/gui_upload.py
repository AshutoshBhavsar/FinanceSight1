import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

from ocr.extractor import extract_text_from_pdf, extract_text_from_docx
from parser import parse_invoice_data
from api_client import insert_invoice_api
from api_client import insert_invoice_api

class UploadWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("📤 Upload Financial Document")
        self.geometry("500x400")
        self.configure(bg="white")

        # Title
        tk.Label(self, text="Upload Financial Document", font=("Helvetica", 16, "bold"), bg="white").pack(pady=20)

        # File path entry
        self.file_path = tk.StringVar()
        tk.Entry(self, textvariable=self.file_path, width=50, state="readonly").pack(pady=10)
        tk.Button(self, text="📁 Browse File", bg="#3498DB", fg="white", command=self.browse_file).pack(pady=5)

        # Category Dropdown
        tk.Label(self, text="Document Category:", bg="white").pack(pady=10)
        self.category = ttk.Combobox(self, values=["Invoice", "Profit & Loss Statement", "Expense Report"], state="readonly")
        self.category.set("Invoice")
        self.category.pack()

        # Upload button
        tk.Button(self, text="📥 Upload & Parse", bg="#2ECC71", fg="white", width=30, command=self.upload_and_parse).pack(pady=20)

        # Status
        self.status_label = tk.Label(self, text="", bg="white", fg="green")
        self.status_label.pack(pady=5)

    def browse_file(self):
        file = filedialog.askopenfilename(filetypes=[("PDF or Word Files", "*.pdf *.docx")])
        if file:
            self.file_path.set(file)

    def upload_and_parse(self):
        path = self.file_path.get()
        if not path:
            messagebox.showwarning("No File", "Please select a PDF or DOCX file.")
            return

        ext = os.path.splitext(path)[1].lower()
        category = self.category.get()

        try:
            # OCR based on file type
            if ext == ".pdf":
                text = extract_text_from_pdf(path)
            elif ext == ".docx":
                text = extract_text_from_docx(path)
            else:
                raise ValueError("Unsupported file type")

            # 🔍 DEBUG: Show extracted OCR text
            print("\n=== OCR TEXT START ===\n")
            print(text)
            print("\n=== OCR TEXT END ===\n")

            # Parse text to get structured data
            vendor, amount, date, _ = parse_invoice_data(text)

            # 🔍 DEBUG: Show extracted fields
            print(f"Parsed Vendor: {vendor}")
            print(f"Parsed Amount: {amount}")
            print(f"Parsed Date: {date}")

            if not vendor or not amount or not date:
                messagebox.showwarning("Parsing Error", "Could not extract vendor, amount, or date. Please check the document.")
                return

            # Upload to backend
            success = insert_invoice_api(vendor, amount, date.isoformat(), category, path)



            if success:
                messagebox.showinfo("Upload Success", f"✅ Invoice Uploaded:\nVendor: {vendor}\nAmount: ₹{amount}\nDate: {date}")
                self.destroy()
            else:
                messagebox.showerror("API Error", "❌ Could not insert into backend.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process file:\n{e}")
            print("[UPLOAD ERROR]", e)


