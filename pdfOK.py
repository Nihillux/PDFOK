import os
import PyPDF2

from PyPDF2 import PdfFileReader
print('Archive, Widthmm, Hightmm, Page, Pages, Bleed')
for root, dirs, files in os.walk(r'./'):
    for f in files:
        if f.endswith(".pdf"):
            pdf=PdfFileReader(open(os.path.join(root, f),'rb'))
            pags = str(int(pdf.getNumPages()))
            p = int(pdf.getNumPages())-1
            count = 0
            while count <= p:
                factor = 0.35278
                a = int(float(pdf.getPage(count).bleedBox[2])*factor)-int(float(pdf.getPage(count).bleedBox[0])*factor)
                b = int(float(pdf.getPage(count).bleedBox[3])*factor)-int(float(pdf.getPage(count).bleedBox[1])*factor)
                x = int(float(pdf.getPage(count).bleedBox[2])*factor)
                y = int(float(pdf.getPage(count).trimBox[2])*factor)
              
                if (x-y > 0):
                    print(f + ', ' + str(a) + ', ' + str(b) + ', ' + str(count+1) + str(pags) + ', CON')
                else:
                    print(f + ', ' + str(a) + ', ' + str(b) + ', ' + str(count+1) + str(pags) + ', SIN')
                count += 1
