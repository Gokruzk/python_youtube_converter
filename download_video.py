import os
from pytube import YouTube
from convert_to_mp3 import convert


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


def action(videos):
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_audio_only()
    descarga.download()
    # get file name
    file = descarga.default_filename
    # rename file
    input_file, output_file = rename_file(file)
    # convert to mp3
    convert(input_file, output_file)
    #remove mp4 file
    os.remove(input_file)