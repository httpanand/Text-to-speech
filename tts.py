from gtts import gTTS

#inputs
text = input("Enter text to convert to speech : ")
language = input("Enter language of text : ")


tts = gTTS(text=text, lang=language, slow=False)
tts.save("output_tts.mp3")

  
