import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()
for pdf in os.listdir('PDFtoMerge/'):
    merger.append('.\PDFtoMerge\\'+pdf)
    print('Success!')

merger.write('super.pdf')

