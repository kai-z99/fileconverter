from pydub import AudioSegment
from PIL import Image
####################
#AUDIO
####################

def ConvertAudioFile(input_file_location, output_file_location, output_format):
    audio = AudioSegment.from_file(input_file_location)
    audio.export(output_file_location, output_format)
    print(f"File converted and saved as {output_file}")

input_file = "HighPressure_Music.mp3" 
output_file = "HighPressure_Music.wav"  
output_format = "wav" 

#ConvertAudioFile(input_file, output_file, output_format)



####################
#IMAGE
####################
def ConvertImageFile(input_file_location, output_file_location):
    with Image.open(input_file_location) as img:
        img = img.convert("RGB")
        img.save(output_file_location, quality=100)

    print(f"File converted and saved as {output_file_location}")

input_file = "spite.png" 
output_file = "spite_converted.jpg"  

#ConvertImageFile(input_file, output_file)




