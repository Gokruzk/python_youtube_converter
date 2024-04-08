from tkinter import *
from tkinter import messagebox as Messagebox
from download_video import action


def main():
    def popup():
        Messagebox.showinfo('About me', 'Nigell Marcel Jama oyarvide\n2024')

    root = Tk()
    root.config(bd=15)
    root.title('YouTube Converter')

    menubar = Menu(root)
    root.config(menu=menubar)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='About', menu=helpmenu)
    helpmenu.add_command(label='About me', command=popup)
    menubar.add_command(label='Exit', command=root.destroy)

    instrucciones = Label(root, text='Convert videos from YouTube to mp3\n\nInsert url here')
    instrucciones.grid(row=0, column=1)

    videos = Entry(root)
    videos.grid(row=1, column=1)

    button = Button(root, text='Download', command=lambda: action(videos))
    button.grid(row=2, column=2)

    root.mainloop()


if __name__ == '__main__':
    main()