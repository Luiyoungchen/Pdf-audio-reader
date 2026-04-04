# 📘 Code Explanation - PDF Audio Reader

## 📌 Overview

This application is a **Python-based GUI tool** that reads PDF files aloud using text-to-speech.

It combines:

* **Tkinter** → GUI
* **pyttsx3** → Speech engine
* **pypdf** → PDF text extraction
* **threading** → Smooth UI performance

---

## 🧱 1. Import Section

```python
import os
import threading
import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader
```

### Explanation:

* `os` → Used to open the PDF file and handle file paths
* `threading` → Runs audio reading in background
* `pyttsx3` → Converts text into speech
* `tkinter` → Builds the GUI
* `filedialog` → Opens file picker
* `messagebox` → Shows alerts
* `PdfReader` → Extracts text from PDF

---

## 🏗️ 2. Class Definition

```python
class PDFReaderApp:
```

This class manages the entire application:

* UI
* File selection
* Audio playback
* PDF processing

---

## ⚙️ 3. Initialization

```python
def __init__(self, root):
    self.root = root
    self.root.title("PDF Audio Reader")
    self.root.geometry("400x200")
    self.root.resizable(False, False)

    self.pdf_path = None

    self.engine = pyttsx3.init()
    self.engine.setProperty('rate', 150)

    self.setup_ui()
```

### Explanation:

* Sets window title and size
* Disables resizing
* Initializes speech engine
* Sets speech speed
* Calls UI setup

---

## 🎨 4. UI Setup

```python
def setup_ui(self):
    tk.Label(self.root, text="PDF Audio Reader", font=("Helvetica", 16, "bold")).pack(pady=15)

    self.lbl_file = tk.Label(self.root, text="No PDF selected", fg="gray", wraplength=350)
    self.lbl_file.pack(pady=5)

    btn_frame = tk.Frame(self.root)
    btn_frame.pack(pady=20)

    self.btn_select = tk.Button(btn_frame, text="Select PDF", command=self.select_pdf, width=12)
    self.btn_select.grid(row=0, column=0, padx=10)

    self.btn_play = tk.Button(btn_frame, text="Play", command=self.play_audio, state=tk.DISABLED, width=12)
    self.btn_play.grid(row=0, column=1, padx=10)
```

### Explanation:

* Creates title label
* Displays selected file name
* Adds buttons:

  * Select PDF
  * Play Audio

---

## 📂 5. Select PDF

```python
def select_pdf(self):
    file_path = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        self.pdf_path = file_path
        self.lbl_file.config(text=f"Selected: {os.path.basename(file_path)}", fg="black")
        self.btn_play.config(state=tk.NORMAL)
```

### Explanation:

* Opens file chooser
* Stores file path
* Updates label
* Enables Play button

---

## ▶️ 6. Play Audio

```python
def play_audio(self):
    if not self.pdf_path:
        return
```

### Step 1: Open PDF

```python
try:
    os.startfile(self.pdf_path)
except Exception as e:
    messagebox.showwarning("Warning", str(e))
```

### Step 2: Update UI

```python
self.btn_play.config(state=tk.DISABLED)
self.lbl_file.config(text="Reading... (Please wait)")
```

### Step 3: Start thread

```python
threading.Thread(target=self._read_pdf_thread, daemon=True).start()
```

### Explanation:

* Opens PDF in viewer
* Disables button
* Starts background reading

---

## 🔄 7. Background Reading

```python
def _read_pdf_thread(self):
    reader = PdfReader(self.pdf_path)
    pages = len(reader.pages)

    for num in range(pages):
        page = reader.pages[num]
        text = page.extract_text()

        if text:
            self.engine.say(text)

    self.engine.runAndWait()
```

### Explanation:

* Loads PDF
* Loops through pages
* Extracts text
* Sends text to speech engine
* Plays audio

---

## ❗ 8. Error Handling

```python
except Exception as e:
    self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
```

### Explanation:

* Shows error popup safely using main thread

---

## ✅ 9. Playback Finished

```python
def _playback_finished(self):
    self.lbl_file.config(text=f"Finished: {os.path.basename(self.pdf_path)}")
    self.btn_play.config(state=tk.NORMAL)
```

### Explanation:

* Updates status
* Enables Play button again

---

## 🚀 10. Main Entry Point

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFReaderApp(root)
    root.mainloop()
```

### Explanation:

* Starts application
* Runs GUI loop

---

## 🔄 Application Flow

```text
Start App
   ↓
Select PDF
   ↓
Enable Play Button
   ↓
Click Play
   ↓
Open PDF
   ↓
Extract Text
   ↓
Convert to Speech
   ↓
Finish
```

---

## ⚠️ Limitations

* Not suitable for scanned PDFs
* No pause/stop feature
* Reads entire document

---

## 🔮 Future Improvements

* Pause / Resume
* Voice selection
* Speed control
* OCR support
* Page selection

---
