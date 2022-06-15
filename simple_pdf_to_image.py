

from pdf2image import convert_from_path

pages = convert_from_path('./test.pdf')

for i in range(len(pages)):
    pages[i].save('page'+ str(i) +'.jpg', 'JPEG')