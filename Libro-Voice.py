import tkinter
import PyPDF3
import pyttsx3
import pdfplumber
from tkinter import *
from tkinter import filedialog
import customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

def askfile():
    filepath = filedialog.askopenfilename(title="Open a PDF file",
                                          filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    book = open(filepath, 'rb')
    pdfReader = PyPDF3.PdfFileReader(book)
    pages = pdfReader.numPages
    print(filepath)

    global finalText
    finalText = ""
    mystr.set(filepath)
    with pdfplumber.open(filepath) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            finalText += text


def convert():
    engine = pyttsx3.init()

    engine.save_to_file(finalText, 'Libro-Voice.mp3')
    engine.runAndWait()
    print("Converted")


root = customtkinter.CTk()
mystr = StringVar()
root.geometry("640x480")
ask = customtkinter.CTkLabel(
    root,text="Welcome to LIBRO-VOICE",font=("Didot",20,"bold"))
ask.place(x=25, y=25)
mystr.set("Select the PDF to convert")
lable2 = customtkinter.CTkLabel(
    root, textvariable=mystr,font=("Didot",22,"bold")).place(x=25, y=120)
button1 = customtkinter.CTkButton(
    root, text="Open PDF",font=("Didot",20,"bold"), command=askfile)
button1.place(relx=0.66,rely=0.72)
button = customtkinter.CTkButton(
    root, text="Convert", command=convert,font=("Didot",20,"bold"))
button.place(relx=0.26,rely=0.75, anchor=tkinter.CENTER)
root.mainloop()
