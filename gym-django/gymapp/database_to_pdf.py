import sqlite3
from fpdf import FPDF


def gymbros_user():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    myfile = open('myfile', 'w')
    myfile.write('id | ')
    myfile.write('username | ')
    myfile.write('email | ')
    myfile.write('password | ')
    myfile.writelines('')  # create a line between rows
    x = cursor.execute('''SELECT * FROM gymbros_user ''')
    for row in x:
        row = str(row).replace("(", "").replace(")",
                  "").replace("'", "").replace(",", "|")
        myfile.write("\n%s" % row)
    db.commit()
    myfile.close()

    # Python program to convert
    # text file to pdf file
    # save FPDF() class into
    # a variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=14)

    # open the text file in read mode
    f = open("myfile", "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='L')

    # save the pdf with name .pdf
    pdf.output("gymbros_users report.pdf")


def gymbros_customer():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    myfile = open('myfile', 'w')
    myfile.write('id | ')
    myfile.write('gender | ')
    myfile.write('weight | ')
    myfile.write('height | ')
    myfile.write('bmi | ')
    myfile.write('Programs | ')
    myfile.write('bill | ')
    myfile.write('customer_id | ')
    myfile.writelines('')  # create a line between rows
    x = cursor.execute('''SELECT * FROM gymbros_customer ''')
    for row in x:
        row = str(row).replace("(", "").replace(")",
                  "").replace("'", "").replace(",", "|")
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
    pdf.set_font("Arial", size=14)

    # open the text file in read mode
    f = open("myfile", "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='L')

    # save the pdf with name .pdf
    pdf.output("gymbros_customer report.pdf")


def workers_workers():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    myfile = open('myfile', 'w')
    myfile.write('id | ')
    myfile.write('name | ')
    myfile.write('email | ')
    myfile.write('password | ')
    myfile.write('nb | ')
    myfile.write('job title | ')
    myfile.write('legal | ')
    myfile.write('salary | ')
    myfile.writelines('')  # create a line between rows
    x = cursor.execute('''SELECT * FROM workers_workers ''')
    for row in x:
        row = str(row).replace("(", "").replace(")",
                  "").replace("'", "").replace(",", "|")
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
    pdf.set_font("Arial", size=14)

    # open the text file in read mode
    f = open("myfile", "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='L')

    # save the pdf with name .pdf
    pdf.output("wokrers_workers report.pdf")


def workers_customers():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    myfile = open('myfile', 'w')
    myfile.write('id | ')
    myfile.write('gender | ')
    myfile.write('email | ')
    myfile.write('passwrord | ')
    myfile.write('bill | ')
    myfile.write('Punch_in | ')
    myfile.write('Punch_out | ')
    myfile.write('Customer_id | ')
    myfile.writelines('')  # create a line between rows
    x = cursor.execute('''SELECT * FROM workers_customers ''')
    for row in x:
        row = str(row).replace("(", "").replace(")", "").replace("'", "").replace(",", "|")
        myfile.write("\n%s" % row)
    db.commit()
    myfile.close()

    # Python program to convert
    # text file to pdf file

    from fpdf import FPDF

    # save FPDF() class into
    # a variable pdf
    pdf=FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 14)

    # open the text file in read mode
    f=open("myfile", "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'L')

    # save the pdf with name .pdf
    pdf.output("workers_customers report.pdf")


def workers_schedule():
    db=sqlite3.connect('db.sqlite3')
    cursor=db.cursor()
    myfile=open('myfile', 'w')
    myfile.write('id | ')
    myfile.write('name | ')
    myfile.write('Mon | ')
    myfile.write('Tues | ')
    myfile.write('Wed | ')
    myfile.write('Thu | ')
    myfile.write('Fri | ')
    myfile.write('Sat | ')
    myfile.write('Sun | ')
    myfile.writelines('')  # create a line between rows
    x=cursor.execute('''SELECT * FROM workers_schedule ''')
    for row in x:
        row=str(row).replace("(", "").replace(")", "").replace("'", "").replace(",", "|")
        myfile.write("\n%s" % row)
    db.commit()
    myfile.close()

    # Python program to convert
    # text file to pdf file

    from fpdf import FPDF

    # save FPDF() class into
    # a variable pdf
    pdf=FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=14)

    # open the text file in read mode
    f=open("myfile", "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='L')

    # save the pdf with name .pdf
    pdf.output("wokrers_schedule report.pdf")
