from imgresize import Resize
from pdfCreator import PdfCreator
import os
from tkinter import Tk, filedialog

import time
print("Select the folder containing images.")
folder_path = filedialog.askdirectory(title="Select the folder containing images")
# Ask where to save the PDF document
print("Select where to save the PDF document.")
Tk().withdraw()  # Hide the main window
output_filename = filedialog.asksaveasfilename(
    title="Save PDF As",
    filetypes=[("PDF files", "*.pdf")],
    defaultextension=".pdf"
)
    
start_time = time.time()
print("Creating PDF document...")
img = Resize(folder_path)
print("Cutting images...")
img.cut()
print("Placing images...")
pdf = PdfCreator(output_filename)
pdf.place(img.tuplesimg)
print("Saving PDF document...")
pdf.document.save()
print(f"Document '{output_filename}' created successfully.")
total_time = time.time() - start_time
print(f"Total time : {total_time:.2f} seconds")
