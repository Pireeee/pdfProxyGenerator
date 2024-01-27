from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image
import os
from tkinter import Tk, filedialog

STANDARD_HEIGHT = 3.5 * 72  # Convert inches to points
STANDARD_WIDTH = 2.5 * 72    # Convert inches to points

def create_document(output_filename, folder_path):
    # Create a new PDF document
    document = canvas.Canvas(output_filename, pagesize=A4)

    # Set up the page size
    width, height = A4

    # Loop through the images in the specified folder and add them to the PDF
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".png") or filename.lower().endswith(".jpeg"):
            image_path = os.path.join(folder_path, filename)
            
            # Open the image using Pillow
            img = Image.open(image_path)

            # Calculate the aspect ratio to maintain the original proportions
            aspect_ratio = img.width / img.height

            # Calculate the width and height for the PDF
            pdf_width = STANDARD_WIDTH
            pdf_height = pdf_width / aspect_ratio

            # Add the image to the PDF using drawInlineImage
            document.drawInlineImage(img, 0, height - pdf_height, pdf_width, pdf_height)
            print(f"Added image '{filename}' to the PDF.")

            # Move to the next page
            document.showPage()

    # Save the PDF document
    document.save()

if __name__ == "__main__":
    # Ask for the folder path containing images
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

    # Create the document
    create_document(output_filename, folder_path)

    print(f"Document '{output_filename}' created successfully.")
