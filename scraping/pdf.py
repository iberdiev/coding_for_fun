'''
Cool snippets that may help in the future.
Various tools to scrape data from PDF.
'''
# Tika
##################################################
import csv
from tika import parser
import os.path
raw = parser.from_file(a)['content'].split('\n')

# Textract
###################################################
import textract
text = textract.process(input_file).decode("utf-8").split('\n')

# PyPDF2
#############################################
import PyPDF2
pdfFileObj = open(input_file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
raw_data = []
for page in range(pages):
    pageObj = pdfReader.getPage(page)
    temp_raw = pageObj.extractText().split('\n')
    print(temp_raw)

######################################################
# pdfminer

import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()
    print(text)

##########################