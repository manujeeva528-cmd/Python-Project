from pypdf import PdfReader, PdfWriter
merger = PdfWriter()
pdfs=['Resume.pdf', 'SI-638735742032575305.pdf', 'Home_patta.pdf']
for pdf in pdfs:
    merger.append(pdf)
merger.write("merged_document.pdf")