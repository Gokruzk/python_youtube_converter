import os
import subprocess
from popup import popups
from pathlib import Path


def convert(input_file, output_file):
    # show message
    popups('Convertion', 'Converting to MP3')
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
        popups('Converted', 'Successfully converted to MP3')
    except subprocess.CalledProcessError as e:
        print(f'Error during conversion: {e}')
