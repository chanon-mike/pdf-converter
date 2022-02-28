import pdfplumber
import gtts
from pathlib import Path

class PDFManager():
    def __init__(self) -> None:
        self.languages = gtts.lang.tts_langs()

    def extract_text(self, file_path):
        all_text = ""
        with pdfplumber.open(file_path) as pdf:
            for pdf_page in pdf.pages:
                single_page_text = pdf_page.extract_text()
                # separate each page's text with newline
                all_text = all_text + '\n' + single_page_text
            return all_text
            
    def pdf_to_txt(self, file_path):
        for path in file_path:
            # Extract text from pdf
            text = self.extract_text(path)
            file_name = Path(path).stem
            # Save file as .txt
            with open(file_name + "_text.txt", "w", encoding="UTF-8") as text_file:
                text_file.write(text)

    def text_to_speech(self, file_path, lang_code):
        for path in file_path:
            # Extract text from pdf
            text = self.extract_text(path)
            file_name = Path(path).stem
            # Save file as .mp3
            tts = gtts.gTTS(text, lang=lang_code)
            tts.save(file_name + ".mp3")
