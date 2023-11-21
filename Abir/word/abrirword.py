from docx import Document

documento = Document("ejemplo.docx")
# Ahora puedes acceder al contenido del archivo Word
for paragraph in documento.paragraphs:
    print(paragraph.text)
