import openpyxl

libro_excel = openpyxl.load_workbook("ejemplo.xlsx")
hoja = libro_excel.active

# Accede a las celdas en la hoja de cálculo
for fila in hoja.iter_rows():
    for celda in fila:
        print(celda.value)
