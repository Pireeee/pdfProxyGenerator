from PIL import Image
import os
class Resize:
    def __init__(self,folder):
        self.height = 3.5 * 72  # Convert inches to points
        self.width = 2.5 * 72    # Convert inches to points
        self.files = [filename for filename in os.listdir(folder) if filename.lower().endswith((".jpg", ".png", ".jpeg"))]
        self.folder = folder
        self.tuplesimg = []
    def cut(self):
        ite = 1
        for imgpath in self.files:
            img = Image.open(os.path.join(self.folder,imgpath))

            aspect_ratio = img.width / img.height
            pdf_width = self.width
            pdf_height = pdf_width / aspect_ratio

            self.tuplesimg.append((img, pdf_width,pdf_height))