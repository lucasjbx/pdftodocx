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
def select_file():
    pdf_file = filedialog.askopenfilename()
    label.config(text=pdf_file)

def select_folder():
    dest_folder = filedialog. askdirectory()
    label_dest_folder.config(text=dest_folder)
    print(label_dest_folder["text"])
    if label["text"] != "Select PDF file":
        button3 = Button(text="Convert")
        button3.grid(row=5, column=1)


# calls action() when pressed
button = Button(text="Select file", command=select_file)

button.grid(row=1, column=1)


button2 = Button(text="Select Dest Folder", command=select_folder)
button2.grid(row=3, column=1)




window.mainloop()