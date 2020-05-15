'''
Cool snippets that may help in the future.
xlrd is a tool to read data from excel files.
'''

##############################################

import xlrd
import csv
import os.path

exists = True if os.path.exists(output_file) else False

header_titles = []
header_row = []

with open(output_file, 'a') as f:

    writer = csv.writer(f)
    if not exists:
        writer.writerow(header_row)
    wb = xlrd.open_workbook(input_file) 
    sheet = wb.sheet_by_name('Subject view')
    workbook_datemode = wb.datemode
    QUALIFICATION, SUBJECT = '',''
    header = sheet.row(4)
    header = [title.value for title in header]
    indices = [
                header.index(header_titles[0]),
                header.index(header_titles[1]),
                header.index(header_titles[3]),
                header.index(header_titles[2]),
                header.index(header_titles[5]),
                header.index(header_titles[4]),
              ]
    for i in range(5, sheet.nrows):
        temp_qual = sheet.cell_value(i,indices[0])
        temp_subj = sheet.cell_value(i,indices[1])