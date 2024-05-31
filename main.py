from pydub import AudioSegment
from PIL import Image
import os
####################
#AUDIO
####################

def ConvertAudioFile(input_file_location, output_file_location):
    output_file_extension = os.path.splitext(output_file_location)[1]
    audio = AudioSegment.from_file(input_file_location)
    audio.export(output_file_location, output_file_extension.strip("."))
    print(f"File converted and saved as {output_file}")

input_file = "HighPressure_Music.mp3" 
output_file = "HighPressure_Music.ogg"  

ConvertAudioFile(input_file, output_file)



####################
#IMAGE
####################
def ConvertImageFile(input_file_location, output_file_location):
    input_file_extension = os.path.splitext(input_file_location)[1]
    output_file_extension = os.path.splitext(output_file_location)[1]

    with Image.open(input_file_location) as img:
        if input_file_extension == output_file_extension:
            print(f"error: input and output are both type {input_file_extension}.")
            return
        if output_file_extension == ".jpg":
            img = img.convert("RGB")

        img.save(output_file_location, quality=100)

    print(f"File converted and saved as {output_file_location}")

input_file = "Rotating_earth_(large).png" 
output_file = "Rotating_earth_(large).gif"  

#ConvertImageFile(input_file, output_file)




