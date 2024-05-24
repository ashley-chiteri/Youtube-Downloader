import tkinter as tk
import ttkbootstrap
import customtkinter
from tkinter import messagebox

from pytube import YouTube

print("hello world")

def start_download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback = on_progress)
        video = ytObject.streams.get_highest_resolution()

        #set the title to the video's title
        finishLabel.configure(text=ytObject.title , text_color="white")
        d_percentage.pack()
        progressBar.pack(padx=10, pady=10)
        video.download()
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.configure(text="Download Error", text_color="red")
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    d_percentage.configure(text = per + "%")
    d_percentage.update()

    # update 
    progressBar.set(float(percentage_of_completion) / 100)

#Our app frame
root = ttkbootstrap.Window(themename="solar")
root.title("Youtube Downloader")
root.geometry("720x480")

#UI elements
title = tk.Label(root, text="Insert a youtube link", font="18")
title.pack(padx=10, pady=15)

#link input
url_var = tk.StringVar()
link = ttkbootstrap.Entry(root, font="sans-serif, 18", textvariable="url_var")
link.pack(pady=10)

#after downloading..
finishLabel = customtkinter.CTkLabel(root, text="")
finishLabel.pack()

#download progress
d_percentage = customtkinter.CTkLabel(root, text="0%")


progressBar = customtkinter.CTkProgressBar(root, width= 200)
progressBar.set(0)

#download button
downloadBtn  = ttkbootstrap.Button(root, text="Download", command=start_download, bootstyle="warning")
downloadBtn.pack(pady=10)

#app main loop
root.mainloop()