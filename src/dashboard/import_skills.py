import openpyxl


def load_skills():
    file_path = r'C:\Users\611776127\desktop\skill_metricx.xlsx'
    wb_obj = openpyxl.load_workbook(file_path)
    sheet_obj = wb_obj.get_sheet_by_name('Skills')
    print(sheet_obj.title)
    pass


if __name__ == "__main__":
    load_skills()
