# Marge the PDF files into a single PDF file
from PyPDF2 import PdfWriter
import os


merger = PdfWriter()

files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf, import_outline=False)

merger.write("merged-pdf.pdf")
merger.close()
