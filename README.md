# YouTube MP3 Converter

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the followings modules.

```
pip install pytube tk pyinstaller Gyan.FFmpeg
```

5. Add ffmpeg to path in environmet variables
```
C:\Users\[user]\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.0-full_build\bin
```

## Build
```
> pyinstaller main.py --onefile --noconsole
```

## Usage
1. If you just want to use the app without open the code, execute 4 and 5 step, then execute the file in ``dist`` folder
2. If you modify the code, just run ``main.py``
3. The music will store into a folder called ``Music Downloaded`` in your ``root`` folder

## License

[MIT](https://choosealicense.com/licenses/mit/)
