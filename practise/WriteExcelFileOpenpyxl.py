import openpyxl
path="C:\\Users\GUDU\PycharmProjects\pythonprojects\ExcelFile\Testsheet.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook.active #workbook.get_sheet_by_name("Sheet1")
for r in range(1,6):
    for c in range(1, 4):
        sheet.cell(row=r,column=c).value="selenium"
        workbook.save(path)