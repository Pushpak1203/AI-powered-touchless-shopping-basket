# backend/voice_recognition.py

import speech_recognition as sr

def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return {"command": command, "success": True}
    except sr.UnknownValueError:
        return {"command": None, "success": False, "error": "Could not understand audio"}
    except sr.RequestError as e:
        return {"command": None, "success": False, "error": f"API request error: {str(e)}"}
