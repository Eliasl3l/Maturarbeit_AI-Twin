# Maturaarbeit_TalkingCharacter
Dieser Code soll es möglich machen eine Konversation mit einer digitalen Person zu haben.

## Die App ist in 4 Teile unterteilt:
- SpeechToText 
Funktion welche das gesprochene der Person aufnimmt und in Text umwandelt mithilfe von google speechrecognition
- languageProcessing
Funktion welche passend zum umgewandelten Text eine Antwort generiert
- TextToVideo
Funktion welche zu der generierten Antwort eine audio file des gesprochenen Textes generiert und ein Video einer Person die diesen spricht.
- main 
Funktion welche die 4 Funktionen mithilfe von flowstatements durchgehend hintereinander laufen lässt und die audio files nach dem abspielen löscht. 