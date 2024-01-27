from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image

STANDARD_HEIGHT = 3.5 * 72  # Convert inches to points
STANDARD_WIDTH = 2.5 * 72    # Convert inches to points

def create_document(output_filename, images):
    # Create a new PDF document
    document = canvas.Canvas(output_filename, pagesize=A4)

    # Set up the page size
    width, height = A4

    # Loop through the images and add them to the PDF
    for image_path in images:
        # Open the image using Pillow
        img = Image.open(image_path)

        # Calculate the aspect ratio to maintain the original proportions
        aspect_ratio = img.width / img.height

        # Calculate the width and height for the PDF
        pdf_width = STANDARD_WIDTH
        pdf_height = pdf_width / aspect_ratio

        # Add the image to the PDF using drawInlineImage
        document.drawInlineImage(img, 0, height - pdf_height, pdf_width, pdf_height)

        # Move to the next page
        document.showPage()

    # Save the PDF document
    document.save()

if __name__ == "__main__":
    # Specify the output PDF file and input image paths
    output_filename = "proxy_document.pdf"
    image_paths = ["Arid Mesa.jpg", "Tundra.jpg", "Plateau.jpg"]

    # Create the document
    create_document(output_filename, image_paths)

    print(f"Document '{output_filename}' created successfully.")
