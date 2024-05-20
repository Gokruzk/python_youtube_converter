import os
import subprocess
from popup import popups
from pathlib import Path

home = Path.home()
download_folder = Path(home, "Music Downloaded")
os.chdir(download_folder)


def convert(input_file, output_file):
    # ffmpeg command to convert .mp4 to .mp3
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', str(input_file),
        '-vn',
        '-acodec', 'libmp3lame',
        '-ab', '192000',
        '-ar', '44100',
        '-y', str(output_file)
    ]
    try:
        # execute command
        result = subprocess.run(ffmpeg_cmd, check=True)
        # show message
    except subprocess.CalledProcessError as e:
        print(f'Error during conversion: {e}')
