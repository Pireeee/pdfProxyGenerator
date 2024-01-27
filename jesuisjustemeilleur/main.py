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

img = Resize(folder_path)
img.cut()
pdf = PdfCreator(output_filename)
pdf.place(img.tuplesimg)
pdf.document.save()
print(f"Document '{output_filename}' created successfully.")
total_time = time.time() - start_time
print(f"Total time taken: {total_time:.2f} seconds")
