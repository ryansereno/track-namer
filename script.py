import os
from mutagen.easyid3 import EasyID3

# Set the directory containing the MP3 files
directory = "/path/to/mp3/files"

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        # Load the metadata of the MP3 file
        audio = EasyID3(os.path.join(directory, filename))
        # Get the title of the track from the metadata
        trackname = audio['title'][0]
        # Rename the file to the track name
        os.rename(os.path.join(directory, filename), os.path.join(directory, trackname + ".mp3"))

