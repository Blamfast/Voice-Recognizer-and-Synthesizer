# Reconnaissance Vocale avec Interface Graphique et Synthèse Vocale

Ce projet fournit une interface utilisateur simple pour transcrire l'audio provenant d'un microphone sélectionné par l'utilisateur en texte, en utilisant l'API Google Speech Recognition, et pour lire ce texte à haute voix en utilisant la synthèse vocale.

## Fonctionnalités

* Liste et sélection de tous les microphones disponibles sur le système.
* Bouton pour démarrer l'écoute du microphone sélectionné.
* Transcription de l'audio en texte en utilisant l'API Google Speech Recognition.
* Lecture du texte transcrit à haute voix en utilisant la synthèse vocale.
* Affichage du texte transcrit ou des messages d'erreur dans l'interface graphique.

## Dépendances

Ce projet utilise les bibliothèques Python suivantes :

* [Tkinter](https://docs.python.org/fr/3/library/tkinter.html) pour l'interface utilisateur graphique.
* [speech_recognition](https://pypi.org/project/SpeechRecognition/) pour la reconnaissance vocale.
* [pyaudio](https://pypi.org/project/PyAudio/) pour l'accès aux périphériques audio.
* [pyttsx3](https://pypi.org/project/pyttsx3/) pour la synthèse vocale.

Vous pouvez installer `speech_recognition`, `pyaudio`, et `pyttsx3` avec pip :
`pip install SpeechRecognition pyaudio pyttsx3`

Sur certains systèmes, l'installation de `pyaudio` peut nécessiter des paquets supplémentaires. Par exemple, sur Ubuntu, vous pourriez avoir besoin de `portaudio19-dev` :
`sudo apt-get install portaudio19-dev`


## Utilisation

Après avoir cloné le projet, vous pouvez le lancer avec Python :
`python main.py`

Une fenêtre apparaîtra, montrant la liste des microphones disponibles. Sélectionnez un microphone, puis cliquez sur le bouton "Cliquez et parlez". Parlez dans le microphone, et votre parole sera transcrit en texte, lu à haute voix, et affiché dans la fenêtre.

## To Do

- Utiliser la reconnaissance vocale pour créer un prompt utilisable dans l'API ChatGPT
- Lecture du résultat retourné par ChatGPT par la synthèse vocale

## Contact

Si vous avez des questions ou des suggestions, n'hésitez pas à [ouvrir un ticket](https://github.com/Blamfast/Voice-Recognizer-and-Synthesizer/issues).


