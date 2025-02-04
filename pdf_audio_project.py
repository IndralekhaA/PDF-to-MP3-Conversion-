#Import the PyPDF2 library, which helps read PDF files and extract text from them
import PyPDF2
#Import the gTTS (Google Text-to-Speech) library to convert text into speech (audio)
from gtts import gTTS

#reading PDF and extract text
#Open the PDF file in 'rb' (read binary) mode
with open("C:\python_practice\pdfreader\Impara-Linglese-Con-La-Musica-Believer-2F-Imagine-Dragons.pdf", 'rb') as  file:
    #Create a PdfReader object from the opened file, which allows us to extract text from each page
    reader = PyPDF2.PdfReader(file)
    #Initialize an empty string to store the extracted text
    #Append the text extracted from each page to the 'text' variable
    text = ''.join([page.extract_text() for page in reader.pages])

#Convert text to audio 
#Use gTTS (Google Text-to-Speech) to convert the extracted text into audio
#The 'lang' argument specifies the language (English in this case)
tts = gTTS(text, lang='en')
#Save the generated audio (speech) as an MP3 file named 'output.mp3'
tts.save('output.mp3')

#Print a message confirming that the audio file has been saved
print("Audio saved as output.mp3")
