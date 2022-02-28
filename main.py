from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilenames
from pdf_manager import PDFManager

pdf = PDFManager()
file_path = ''

# Setting window
window = Tk()
window.title("PDF Converter")
window.geometry('700x450') 
window.resizable(False, False)
window.grid_columnconfigure(0, weight=1)

# Upload files
def upload_files():
    global file_path
    file_path = askopenfilenames(filetypes=[('PDF Files', '*pdf')])
    if file_path is not None:
        Label(window, text='Files Uploaded Successfully!', foreground='green', font=("Open Sans", 10)).grid(row=2, pady=10)
        pdf_to_text_btn.config(state=NORMAL)
        language_list_label.config(state=NORMAL)
        language_list.config(state='readonly')

# Convert pdf to txt
def pdf_to_txt(file_path):
    pdf.pdf_to_txt(file_path)
    messagebox.showinfo(title="Save successfully", message="PDF files converted to .txt files successfully!")

# Convert pdf to mp3
def pdf_to_mp3(file_path):
    lang_name = language_list.get()
    for code, name in pdf.languages.items():
        if lang_name == name:
            lang_code = code
            break
    pdf.text_to_speech(file_path, lang_code)
    messagebox.showinfo(title="Save successfully", message="PDF files converted to .mp3 files successfully!")

    
Label(window, text="PDF Converter", font=("Open Sans", 20, "bold")).grid(row=0, pady=20)
upload_btn = Button(window, text='Upload Files', font=("Open Sans", 10), command=upload_files) 
upload_btn.grid(row=1, pady=20)

pdf_to_text_btn = Button(window, text='PDF to Text', font=("Open Sans", 10), state=DISABLED, command=lambda: pdf_to_txt(file_path))
pdf_to_text_btn.grid(row=3, pady=10)

pdf_to_mp3_btn = Button(window, text='PDF to MP3', font=("Open Sans", 10), state=DISABLED, command=lambda: pdf_to_mp3(file_path))
pdf_to_mp3_btn.grid(row=4)

language_list_label = Label(window, text="Audio Languages Lists", font=("Open Sans", 10), state=DISABLED)
language_list_label.grid(row=5, pady=10)

language_list = ttk.Combobox(window, width=25, state=DISABLED)
language_list['values'] = [lang_name for _, lang_name in pdf.languages.items()]
language_list.grid(row=6)
language_list.bind("<<ComboboxSelected>>", lambda _: pdf_to_mp3_btn.config(state=ACTIVE))

window.mainloop()