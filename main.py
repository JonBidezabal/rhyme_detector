from get_transcription import get_text
from create_file import create_text_file

def main():
    audio_file = "audio.wav"  
    transcription = get_text(audio_file)
    
    if transcription:
        create_text_file(transcription)
    print("Texto transrito:", transcription)

if __name__ == "__main__":
    main()