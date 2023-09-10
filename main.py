import PyPDF3
import pdfplumber
import pyttsx3 as tts
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry("400x200")
root.title("Pdf to AudioFile")


def upload_file():
    file = askopenfilename()
    f = open(file, "rb")
    pdf_reader = PyPDF3.PdfFileReader(f)
    pages = pdf_reader.pages
    text = ""

    with pdfplumber.open(file) as pdf:
        for i in range(len(pages)):
            page = pdf.pages[i]
            text += page.extract_text()
            print(text)

    engine = tts.init()
    engine.setProperty("rate", 150)
    engine.save_to_file(text, "audio.mp3")
    engine.runAndWait()
    info_label = Label(text="DOWNLOADED", font=("Arial", 15))
    info_label.pack(pady=20)


title_label = Label(text="Choose a pdf file to convert", font=("Arial", 15))
title_label.pack(pady=10)

upload_file_button = Button(text="Upload File", command=upload_file)
upload_file_button.pack()

root.mainloop()