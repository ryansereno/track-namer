from mutagen.easyid3 import EasyID3
import os

print("input directory for processing: ")
path = input()
os.chdir(path)

file_list = filter((lambda x: '.mp3' in x), os.listdir(path))

for file in file_list:
        print("file: "+file)
        if file.endswith(".mp3"): 
                try:
                        current = EasyID3(file)
                        newname = current["title"][0] + ".mp3"
                        newname.replace(" ", "_")
                        del current
                        print("renaming "+file+" to "+newname)
                        os.rename(file, newname)
                except:
                        print("there was an error")
