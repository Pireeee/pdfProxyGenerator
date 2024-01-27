from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image
import os
from tkinter import Tk, filedialog
from tqdm import tqdm
import time

STANDARD_HEIGHT = 3.5 * 72  # Convert inches to points
STANDARD_WIDTH = 2.5 * 72    # Convert inches to points

GRID_ROWS = 3
GRID_COLS = 3

def create_document(output_filename, folder_path):
    # Create a new PDF document
    document = canvas.Canvas(output_filename, pagesize=A4)

    # Set up the page size
    width, height = A4

    # Calculate the gap between images to center them on the page
    gap_x = (width - (GRID_COLS * STANDARD_WIDTH)) / (GRID_COLS + 1)
    gap_y = (height - (GRID_ROWS * STANDARD_HEIGHT)) / (GRID_ROWS + 1)

    # Get the list of image files
    image_files = [filename for filename in os.listdir(folder_path) if filename.lower().endswith((".jpg", ".png", ".jpeg"))]
    total_images = len(image_files)

    # Initialize time measurement
    start_time = time.time()

    # Loop through the images in the specified folder and add them to the PDF
    for i, filename in tqdm(enumerate(image_files), desc="Processing Images", unit="image", total=total_images):
        # Open the image using Pillow
        img = Image.open(os.path.join(folder_path, filename))

        # Calculate the aspect ratio to maintain the original proportions
        aspect_ratio = img.width / img.height

        # Calculate the width and height for the PDF
        pdf_width = STANDARD_WIDTH
        pdf_height = pdf_width / aspect_ratio

        # Calculate the row and column for the current image
        row = i // GRID_COLS
        col = i % GRID_COLS

        # Calculate the position for the current image
        x = col * (pdf_width + gap_x) + gap_x
        y = height - ((row + 1) * (pdf_height + gap_y)) - gap_y

        # Add the image to the PDF using drawInlineImage
        document.drawInlineImage(img, x, y, pdf_width, pdf_height)

        # Move to the next page if needed
        if (i + 1) % (GRID_ROWS * GRID_COLS) == 0:
            document.showPage()

    # Save the PDF document
    print("Saving PDF document...")
    document.save()

    # Calculate and print total time and total images
    total_time = time.time() - start_time
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Total images processed: {total_images}")

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
