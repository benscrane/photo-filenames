import os
from PIL import Image, ExifTags

def paddedInc(inc, len = 3):
    return str(inc).rjust(len, "0")

directory = os.getcwd()
for filename in os.listdir(directory):
    [ fileroot, filetype ] = filename.split(".")
    if len(fileroot) != 20 and filename.startswith(("DCS", "DSC")):
        inc = 00
        img = Image.open(filename)
        exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
        dateTime = exif["DateTimeOriginal"]
        [date, time] = dateTime.split(" ")
        arr = date.split(":") + time.split(":")
        newName = "DCS" + "".join(arr) + paddedInc(inc) + "." + filetype
        while (os.path.exists(newName)):
            inc += 1
            newName = "DCS" + "".join(arr) + paddedInc(inc) + "." + filetype
        print(newName)
        os.rename(filename, newName)