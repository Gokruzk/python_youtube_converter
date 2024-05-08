import os
from pytube import YouTube
from tkinter import messagebox as Messagebox
from convert_to_mp3 import convert
from popup import popups


def check_url(url):
    flag = 'youtu' == url[8:13] or 'youtu' == url[12:17]
    return flag


def rename_file(file):
    # remove spaces
    input_file = file.split(" ")
    input_file = "".join(input_file)
    os.rename(file, input_file)
    # extract file name without '.mp4'
    output_file = input_file[0:len(input_file) - 4]
    # create '.mp3' file name
    output_file += '.mp3'
    return [input_file, output_file]


def action(url):
    enlace = url.get()
    print(enlace)
    if check_url(enlace):
        video = YouTube(enlace)
        popups('Download', 'Downloading')
        try:
            descarga = video.streams.get_audio_only()
            descarga.download()
            # get file name
            file = descarga.default_filename
            print(file)
            # rename file
            input_file, output_file = rename_file(file)
            # convert to mp3
            popups('Download', 'Successfully downloaded')
            convert(input_file, output_file)
            # remove mp4 file
            os.remove(input_file)
        except Exception as e:
            popups('Download', 'Download error')
            print(e)
    else:
        popups('Process', 'It\'s not a youtube url')
