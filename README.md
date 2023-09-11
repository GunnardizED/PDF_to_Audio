Pdf to AudioFile Converter

This is a simple Python script for converting PDF files into audio files. It utilizes the PyPDF3 and pdfplumber libraries to extract text from the PDF and the pyttsx3 library to convert the text into an audio file. The graphical user interface (GUI) is created using the Tkinter library.
Usage

    Make sure you have Python installed on your system.

    Install the required libraries using pip:

    bash

pip install PyPDF3 pdfplumber pyttsx3

Run the script by executing the following command:

bash

    python script.py

    Replace script.py with the actual name of your Python script containing the provided code.

    The GUI window will appear.

    Click the "Upload File" button to choose the PDF file you want to convert.

    The script will extract text from the PDF, convert it to audio, and save it as "audio.mp3" in the same directory where the script is located.

    Once the conversion is complete, you will see a "DOWNLOADED" message on the GUI.

Dependencies

    PyPDF3: Used for reading PDF files.
    pdfplumber: Used for more accurate text extraction from PDF pages.
    pyttsx3: Used for text-to-speech conversion.

Notes

    You can adjust the speech rate by modifying the engine.setProperty("rate", 150) line in the code.
    Make sure to handle exceptions and errors appropriately in a production environment.
    This script provides a basic example of PDF to audio conversion and can be further enhanced with additional features and error handling.
    Feel free to customize the GUI and add more functionalities as needed.

Please make sure to comply with copyright and licensing regulations when converting PDFs to audio files, as this script is intended for personal or educational use.
