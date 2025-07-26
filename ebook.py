from pypdf import PdfReader
from gtts import gTTS

def pdf_to_mp3(pdf_path, mp3_output, lang='en'):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    # Convert text to speech
    tts = gTTS(text=text, lang=lang)
    tts.save(mp3_output)
    print(f"MP3 saved to: {mp3_output}")

pdf_to_mp3("C:\\Users\\vuppu\\OneDrive\\Desktop\\risk.pdf", "output.mp3")
