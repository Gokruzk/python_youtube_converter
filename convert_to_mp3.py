import os
import subprocess
from popup import popups
from pathlib import Path

download_folder = Path(Path.home(), "Music_Downloaded")


def convert(input_file: str, output_file: str):
    input_folder = Path(download_folder, input_file)
    output_folder = Path(download_folder, output_file)
    # show message
    popups('Convertion', 'Converting to MP3')
    # ffmpeg command to convert .mp4 to .mp3
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_folder,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ab', '192000',
        '-ar', '44100',
        '-y', output_folder
    ]
    try:
        # execute command
        subprocess.run(ffmpeg_cmd, check=True)
        # show message
        popups('Convertion', 'Successfully converted to MP3')
    # except subprocess.CalledProcessError as e:
    except Exception as e:
        popups('Convertion error', e)
