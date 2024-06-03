# YouTube MP3 Converter

## Requirements

### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the followings modules.

```
pip install pytube tk pyinstaller
```

### Use a package manager to install [ffmpeg](https://ffmpeg.org/download.html).

Windows: [winget](https://learn.microsoft.com/es-es/windows/package-manager/winget/)
```
winget install ffmpeg
```
Linux: [apt](https://help.ubuntu.com/kubuntu/desktopguide/es/apt-get.html)
```
sudo apt update
sudo apt upgrade
sudo apt install ffmpeg
```

## Build

```
pyinstaller main.py --onefile --noconsole
```

## Usage
### 1. If you just want to use the app, execute the file in ``dist`` folder, make sure to have [ffmpeg](https://ffmpeg.org/download.html) installed.
### 2. Execute as administrador

```
cd dist
```
Windows
```
main.exe
```
Linux
```
./main
```
### 3. If you are going to modify the code, make sure to follow the [requirements](https://github.com/Gokruzk/python_youtube_converter/tree/main?tab=readme-ov-file#requirements) steps and then run ``main.py``
### 4. The files will store into a folder called ``Music Downloaded`` in your ``root`` folder
