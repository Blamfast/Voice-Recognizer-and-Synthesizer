import tkinter as tk
import speech_recognition as sr
import pyaudio
import pyttsx3

engine = pyttsx3.init()
def dire(texte):
    engine.say(texte)
    engine.runAndWait()

def lister_micros():
    p = pyaudio.PyAudio()
    infos = []
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxInputChannels'] > 0:  # si c'est un périphérique d'entrée
            infos.append(info)
    return infos

def ecouter():
    index_micro = liste_micros.curselection()[0]  # récupérer l'index du microphone sélectionné
    index_micro = micros[index_micro]['index']  # récupérer l'index pyaudio correspondant

    r = sr.Recognizer()
    with sr.Microphone(device_index=index_micro) as source:
        audio = r.listen(source)
        try:
            texte = r.recognize_google(audio, language='fr-FR')
            output_label.config(text="Vous avez dit : {}".format(texte))
            dire(texte)
        except sr.UnknownValueError:
            output_label.config(text="Le programme n'a pas compris l'audio")
            dire(texte)
        except sr.RequestError as e:
            output_label.config(text="Erreur de service ; {0}".format(e))
            dire(texte)

fenetre = tk.Tk()

micros = lister_micros()

liste_micros = tk.Listbox(fenetre, width=50)  # ajuster la largeur à votre convenance
for m in micros:
    liste_micros.insert(tk.END, m['name'])
liste_micros.pack()

bouton = tk.Button(fenetre, text="Cliquez et parlez", command=ecouter)
bouton.pack()

output_label = tk.Label(fenetre, text="")
output_label.pack()

fenetre.mainloop()
