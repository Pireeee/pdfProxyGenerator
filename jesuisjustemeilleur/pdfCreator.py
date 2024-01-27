from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
class PdfCreator():
    def __init__(self,output_filename):
        self.grid = 3
        self.height = 3.5 * 72  # Convert inches to points
        self.width = 2.5 * 72    # Convert inches to points
        self.formatW,self.formatH = A4
        self.output_filename = output_filename

        # Create a new PDF document
        self.document = canvas.Canvas(self.output_filename, pagesize=A4)

        # Set up the page size
        self.gap_x = (self.formatW - (self.grid * self.width)) / (self.grid + 1)
        self.gap_y = (self.formatH - (self.grid * self.height)) / (self.grid + 1)
    def place(self,imgtupleslist):
        iteration = 0
        for imgtuples in imgtupleslist:
            img,pdf_width,pdf_height = imgtuples
            row = iteration // self.grid
            col = iteration % self.grid
            x = col * (pdf_width + self.gap_x) + self.gap_x
            y = self.formatH - ((row + 1) * (pdf_height + self.gap_y)) - self.gap_y
            # Add the image to the PDF using drawInlineImage
            self.document.drawInlineImage(img, x, y, pdf_width, pdf_height)
            # Move to the next page if needed
            if (iteration + 1) % (self.grid * self.grid) == 0:
                self.document.showPage()
                iteration = 0
            else:
                iteration +=1