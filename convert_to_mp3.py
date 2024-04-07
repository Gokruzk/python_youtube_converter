import subprocess


def convert(input_file, output_file):
    #ffmpeg command to convert .mp4 to .mp3
    ffmpeg_cmd = f'ffmpeg -i {input_file} -vn -acodec libmp3lame -ab 192000 -ar 44100 -y {output_file}'
    try:
        subprocess.run(f'{ffmpeg_cmd}', shell=False)
        print('Successfully converted')
    except subprocess.CalledProcessError as e:
        print(e)