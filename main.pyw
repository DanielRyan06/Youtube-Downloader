from tkinter import *
from tkinter import ttk
from pytube import YouTube
import os

win= Tk()
win.title('Youtube Downloader')
win.geometry("550x150")

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)
   print(string)
   video_url = string
   yt = YouTube(video_url)
   video_stream = yt.streams.get_highest_resolution()
   video_stream.download(os.getcwd())

label=Label(win, text="", font=("Courier 10 bold"))
label.pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Download",width= 20, command= display_text).pack(pady=20)


win.mainloop()
