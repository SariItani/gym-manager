import sqlite3
db = sqlite3.connect('db.sqlite3')
cursor = db.cursor()
myfile = open('myfile','w')
myfile.write('id ')
myfile.write('name')
myfile.writelines('') #create a line between rows
x = cursor.execute('''SELECT * FROM * ''' )
for row in x:
  row = str(row).replace("(", "").replace(")", "").replace("'","")
  myfile.write("\n%s" % row)
db.commit()
myfile.close()

# Python program to convert
# text file to pdf file


from fpdf import FPDF

# save FPDF() class into
# a variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 14)

# open the text file in read mode
f = open("myfile", "r")

# insert the texts in pdf
for x in f:
	pdf.cell(200, 10, txt = x, ln = 1, align = 'L')

# save the pdf with name .pdf
pdf.output("mygfg.pdf")
