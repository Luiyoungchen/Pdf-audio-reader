import os
import threading
import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader

class PDFReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Audio Reader")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        self.pdf_path = None

        # Init text-to-speech
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.root, text="PDF Audio Reader", font=("Helvetica", 16, "bold")).pack(pady=15)

        # File path label
        self.lbl_file = tk.Label(self.root, text="No PDF selected", fg="gray", wraplength=350)
        self.lbl_file.pack(pady=5)

        # Buttons frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        self.btn_select = tk.Button(btn_frame, text="Select PDF", command=self.select_pdf, width=12)
        self.btn_select.grid(row=0, column=0, padx=10)

        self.btn_play = tk.Button(btn_frame, text="Play", command=self.play_audio, state=tk.DISABLED, width=12)
        self.btn_play.grid(row=0, column=1, padx=10)

    def select_pdf(self):
        file_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_path = file_path
            self.lbl_file.config(text=f"Selected: {os.path.basename(file_path)}", fg="black")
            self.btn_play.config(state=tk.NORMAL)

    def play_audio(self):
        if not self.pdf_path:
            return
        
        # Open the PDF in the default PDF viewer
        try:
            os.startfile(self.pdf_path)
            print(f"Opened PDF in viewer: {self.pdf_path}")
        except Exception as e:
            messagebox.showwarning("Warning", f"Could not open PDF viewer: {e}")

        # Disable play button during playback
        self.btn_play.config(state=tk.DISABLED)
        self.lbl_file.config(text="Reading... (Please wait)")

        # Start reading in a separate thread so UI does not freeze
        threading.Thread(target=self._read_pdf_thread, daemon=True).start()

    def _read_pdf_thread(self):
        try:
            reader = PdfReader(self.pdf_path)
            pages = len(reader.pages)

            for num in range(pages):
                page = reader.pages[num]
                text = page.extract_text()
                if text:
                    self.engine.say(text)

            self.engine.runAndWait()

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"An error occurred while reading: {e}"))

        finally:
            # Re-enable the button when finished reading (using safe after method for tkinter)
            if self.root.winfo_exists():
                self.root.after(0, self._playback_finished)
                
    def _playback_finished(self):
        self.lbl_file.config(text=f"Finished: {os.path.basename(self.pdf_path)}")
        self.btn_play.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFReaderApp(root)
    root.mainloop()
