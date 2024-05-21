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

## Build
```
pyinstaller main.py --onefile --noconsole
```

## Usage
1. If you just want to use the app, execute the file in ``dist`` folder, make sure to have [ffmpeg](https://ffmpeg.org/download.html)
2. If you are going to modify the code, make sure to follow the requirements steps and then run ``main.py``
3. The music will store into a folder called ``Music Downloaded`` in your ``root`` folder

## License

[MIT](https://choosealicense.com/licenses/mit/)
