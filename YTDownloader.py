from tkinter import *
from pytube import YouTube
from time import sleep

root = Tk()
root.geometry('700x400')

root.title("Simple Youtube Video Downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack(ipadx=10,ipady=10)

link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').pack(ipadx=30,ipady=30)
link_enter = Entry(root, width = 70,textvariable = link).pack(ipadx=1,ipady=1)



def DownloadVideo():
    url =YouTube(str(link.get()))
    title = url.title
    video = url.streams.get_highest_resolution()
    bytes = video.filesize
    mb = round(bytes/1024/1024,2)
    mb_text = "Video is " + str(mb) + " Mb"
    Label(root, text = title, font = 'arial 15').pack(ipadx=10,ipady=10)
    Label(root, text = mb_text, font = 'arial 15').pack(ipadx=10,ipady=10)
    root.update()
    if mb != "":
        video.download()
        Label(root, text = 'DOWNLOADED', font = 'arial 15').pack(ipadx=10,ipady=10)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'yellow', padx = 2, command = DownloadVideo).pack()


root.mainloop()