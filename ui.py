# Import the required modules
from pdf2docx import Converter
from tkinter import *
from tkinter import filedialog

# Creating a new window and configurations
window = Tk()
window.title("PDF to DOCX")
window.minsize(width=100, height=100)


# Labels

label = Label(text="Select PDF file")
label.grid(column=1, row=0)

label_dest_folder = Label(text="")
label_dest_folder.grid(column=1, row=2)




# Buttons

def convert():
    # Using the built-in function, convert the PDF file to a document file by saving it in a variable.
    cv = Converter(label["text"])
    file_name= label["text"].split('/')[-1].split('.')[0]
    dest = label_dest_folder["text"]+"/"+file_name+".docx"
    print(dest)
    cv.convert(dest)

def select_file():
    pdf_file = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    label.config(text=pdf_file)

def select_folder():
    dest_folder = filedialog. askdirectory()
    label_dest_folder.config(text=dest_folder)
    print(label_dest_folder["text"])
    if label["text"] != "Select PDF file":
        button3 = Button(text="Convert", command=convert)
        button3.grid(row=5, column=1)


# calls action() when pressed
button = Button(text="Select file", command=select_file)

button.grid(row=1, column=1)   


button2 = Button(text="Select Dest Folder", command=select_folder)
button2.grid(row=3, column=1)




window.mainloop()