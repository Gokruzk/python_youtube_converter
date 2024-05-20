# YouTube MP3 Converter

## Requirements

1 Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the followings modules.

```
pip install pytube tk pyinstaller
```

1.1 If you are using Windows, use the package manager [winget](https://learn.microsoft.com/es-es/windows/package-manager/winget/) to install the following module
```
winget install ffmpeg
```

2 Add ffmpeg to path in environmet variables
```
C:\Users\[user]\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.0-full_build\bin
```

## Build
```
pyinstaller main.py --onefile --noconsole
```

## Usage
1. If you just want to use the app, execute the file in ``dist`` folder
2. If you are going to modify the code, make sure to follow the installations steps and then run ``main.py``
3. The music will store into a folder called ``Music Downloaded`` in your ``root`` folder

## License

[MIT](https://choosealicense.com/licenses/mit/)
