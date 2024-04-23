import os


def create_text_file(transcription):

    directory = "transcriptions"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, "transcription.md")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("# Transcripción de Audio\n\n")
        file.write("```plaintext\n")
        file.write(transcription + "\n")
        file.write("```\n")
        print(f"Archivo Markdown creado en {file_path}")