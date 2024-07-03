# Import the required modules
from pdf2docx import Converter

# for selec files
import tkinter as tk
from tkinter import filedialog

#for open path
import subprocess


root = tk.Tk()
root.withdraw()

# Keeping the PDF's location in a separate variable
pdf_file = filedialog.askopenfilename() 

# Maintaining the Document's path in a separate variable
docx_file = ""

# Using the built-in function, convert the PDF file to a document file by saving it in a variable.
cv = Converter(pdf_file)
print(pdf_file)

path = filedialog. askdirectory()
print(path)

# Storing the Document in the variable's initialised path
cv.convert(path+"/pdf.docx")

# Conversion closure through the function close()
cv.close()

new_path = path.replace("/", "\\")
# open resul folder
subprocess.Popen(f'explorer {new_path}')
