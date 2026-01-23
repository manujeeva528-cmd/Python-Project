import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter
import os

class PDFMergerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("500x400")
        self.pdf_files = []
        
        # Title
        title_label = tk.Label(root, text="PDF Merger", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)
        
        # File listbox
        tk.Label(root, text="Selected PDFs:", font=("Arial", 10)).pack(anchor="w", padx=20)
        self.file_listbox = tk.Listbox(root, height=8, width=55)
        self.file_listbox.pack(padx=20, pady=10)
        
        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(root, command=self.file_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)
        
        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # Buttons
        add_btn = tk.Button(button_frame, text="Add PDF", command=self.add_files, width=15)
        add_btn.grid(row=0, column=0, padx=5)
        
        remove_btn = tk.Button(button_frame, text="Remove Selected", command=self.remove_file, width=15)
        remove_btn.grid(row=0, column=1, padx=5)
        
        clear_btn = tk.Button(button_frame, text="Clear All", command=self.clear_files, width=15)
        clear_btn.grid(row=0, column=2, padx=5)
        
        # Merge button
        merge_btn = tk.Button(root, text="Merge PDFs", command=self.merge_pdfs, bg="green", fg="white", font=("Arial", 12, "bold"), width=20)
        merge_btn.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(root, text="Ready", font=("Arial", 9), fg="blue")
        self.status_label.pack(pady=5)
    
    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
        self.update_listbox()
    
    def remove_file(self):
        selection = self.file_listbox.curselection()
        if selection:
            for index in reversed(selection):
                self.pdf_files.pop(index)
            self.update_listbox()
    
    def clear_files(self):
        self.pdf_files.clear()
        self.update_listbox()
    
    def update_listbox(self):
        self.file_listbox.delete(0, tk.END)
        for pdf in self.pdf_files:
            self.file_listbox.insert(tk.END, os.path.basename(pdf))
    
    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("No Files", "Please add PDF files to merge.")
            return
        
        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile="merged_document.pdf"
        )
        
        if output_file:
            try:
                self.status_label.config(text="Merging...", fg="orange")
                self.root.update()
                
                merger = PdfWriter()
                for pdf in self.pdf_files:
                    merger.append(pdf)
                
                merger.write(output_file)
                self.status_label.config(text=f"Success! Saved to {os.path.basename(output_file)}", fg="green")
                messagebox.showinfo("Success", f"PDFs merged successfully!\nSaved as: {output_file}")
            except Exception as e:
                self.status_label.config(text="Error occurred", fg="red")
                messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerGUI(root)
    root.mainloop()