import PyPDF2

archivo_pdf = open("ejemplo.pdf", "rb")
lector_pdf = PyPDF2.PdfFileReader(archivo_pdf)

# Accede al contenido del PDF
for pagina in range(lector_pdf.numPages):
    texto = lector_pdf.getPage(pagina).extractText()
    print(texto)

archivo_pdf.close()
