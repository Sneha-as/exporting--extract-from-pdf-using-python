#-*- coding: utf-8 -*-
import PyPDF2 as pdf
import json
file=open('The_Living_World.pdf','rb')
file
pdf_reader=pdf.PdfFileReader(file)
pdf_reader
help(pdf_reader)
pdf_reader.getIsEncrypted()
pdf_reader.getNumPages()
i=0
while i<pdf_reader.getNumPages():
    pageinfo=pdf_reader.getPage(i)
    text=pageinfo.extractText()
    print(text)
    i=i+1  
  
fd=open('The_Living_World.pdf','r','utf-8')
d=fd.read()
fd.close()
new_file=open('The_Living_World.pdf','w')
for i in range(len(file)):
        new_file.write(fd)
new_file.close()        

x=json.loads(fd)
print(x)