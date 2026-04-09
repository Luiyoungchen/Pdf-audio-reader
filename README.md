# PDF Audio Reader 🎧
This is the beginer level , simple and easy code, I hope it will be understandable.     

A lightweight, user-friendly desktop application built with Python that reads your PDF files out loud! It comes with a modern Tkinter Graphical User Interface (GUI) and utilizes text-to-speech capabilities to make your documents accessible and easy to listen to.

## Features 
- **Clean Interface:** A responsive and straightforward window to easily select and play files.
- **Auto-Open Viewer:** Whenever you start playing a document, the application will automatically pop open the PDF in your default system viewer so you can easily read along.
- **Responsive execution:** The text-to-speech engine runs in a dedicated background thread, ensuring that the main GUI never randomly freezes up.
- **Powered by `pypdf`:** Fast and reliable text extraction from pdf documents.

## Prerequisites 
You will need to have **Python 3.x** installed on your system.

## Installation 
1. Clone or download this project to your computer.
2. Open your terminal (or command prompt) and navigate to the project directory.
3. Install the required dependencies using the enclosed `requirement.txt` file by running:
    ```bash
    pip install -r requirement.txt
    ```

> The script uses `pypdf` for parsing the PDF content and `pyttsx3` for the text-to-speech audio.

## Usage 
1. Start the application by running:
    ```bash
    python main.py
    ```
2. Once the application window opens, click **"Select PDF"**.
3. Choose a `.pdf` file from your computer.
4. Click **"Play"** to let the program open your document and begin reading it out loud!

## Troubleshooting 
- **ModuleNotFoundError:** Ensure you ran the `pip install -r requirement.txt` command in the correct directory.
- **No Audio Playing:** Make sure your system volume is turned up and you selected a valid PDF that contains actual text (not purely scanned images!).

I hpoe you understand , thank you
