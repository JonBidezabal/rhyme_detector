import speech_recognition as transcriptor

def get_text(audio_file):
    try:
        recognizer = transcriptor.Recognizer()
        with transcriptor.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="es-ES")  
        return text
    except transcriptor.UnknownValueError:
        return "No se pudo entender el audio"
    except transcriptor.RequestError as e:
        return f"Fallo en la transcripción, {str(e)}"