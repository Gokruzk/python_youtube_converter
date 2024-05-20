import os
from pathlib import Path
from pytube import YouTube
from tkinter import ttk
from convert_to_mp3 import convert
from popup import popups

# download path
home = Path.home()
download_folder = Path(home, "Music Downloaded")
if not download_folder.exists():
    os.mkdir(download_folder)
os.chdir(download_folder)


def check_url(url):
    flag = 'youtu' == url[8:13] or 'youtu' == url[12:17]
    return flag


def rename_file(file):
    # remove spaces
    input_file = file.split(" ")
    input_file = "".join(input_file)
    os.rename(file, input_file)
    # extract file name without '.mp4'
    output_file = Path(download_folder, file).stem
    output_file = output_file.split(" ")
    output_file = "".join(output_file)
    # create '.mp3' file name
    output_file += '.mp3'
    return [input_file, output_file]


def on_progress(stream, chunk, bytes_remaining, progressbar: ttk.Progressbar):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    progressbar['value'] = pct_completed
    progressbar.update()


def action(url):
    progressbar = ttk.Progressbar(
        orient="horizontal", length=300, mode="determinate")
    progressbar.config(maximum=100)
    progressbar.place(x=30, y=80, width=100)
    enlace = url.get()
    print(enlace)
    if check_url(enlace):
        video = YouTube(enlace, on_progress_callback=lambda stream, chunk,
                        bytes_remaining: on_progress(stream, chunk, bytes_remaining, progressbar))
        try:
            descarga = video.streams.get_audio_only()
            descarga.download()
            # get file name
            file = descarga.default_filename
            input_file = os.path.basename(Path(download_folder, file))
            # rename file
            input_file, output_file = rename_file(input_file)
            # convert to mp3
            convert(input_file, output_file)
            # remove mp4 file
            os.remove(input_file)
            popups('Download', 'Successfully downloaded')
        except Exception as e:
            popups('Download', 'Download error')
            print(e)
    else:
        popups('Process', 'It\'s not a youtube url')
