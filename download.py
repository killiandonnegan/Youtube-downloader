from cgitb import text
from email.mime import audio
from importlib.resources import path
from msilib.schema import Error
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.messagebox import showinfo
from turtle import color, down
from moviepy.video.io.VideoFileClip import VideoFileClip
from numpy import place
from pytube import YouTube
from tkinter import messagebox
import os
import webbrowser
import sys

#Functions


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename


def select_path():
    path = filedialog.askdirectory()

    path_label.config(text=path)


def download_mp4():
        try:
            #get link
            get_link = link_field.get()

            if get_link=="":  #check if there is something in link field
                messagebox.showinfo(title="klgrm.xyz", message="Enter a Youtube link.")

            else:
                #get selected path
                user_path = path_label.cget("text")

                #check if path has been selected
                if user_path != "<download path>" and user_path != "":

                    #download video
                    
                    #if user wants mp3
                    if(form.get()==".mp3"):
                            videofile = YouTube(get_link).streams.get_audio_only().download()
                            base, ext = os.path.splitext(videofile)
                            new_file = base + '.mp3'
                            os.rename(videofile, new_file)
                            shutil.move(new_file, user_path)
                            messagebox.showinfo(title="klgrm.xyz", message="Your "+form.get()+" file has been downloaded to "+user_path)
                            
                            
                    #if user wants mp4
                    elif(form.get()==".mp4"):
                            videofile = YouTube(get_link).streams.get_highest_resolution().download()
                            video = VideoFileClip(videofile)
                            video.close()
                            shutil.move(videofile, user_path)
                            messagebox.showinfo(title=None, message="Your "+form.get()+" file has been downloaded to "+user_path)

                    #they have not selected either
                    else:
                            messagebox.showinfo(title="klgrm.xyz", message="Select a file format.")
                
                else: #path has not been selected
                    messagebox.showinfo(title="klgrm.xyz", message="Select your download path.")

        except: #only other error is invalid url
            messagebox.showinfo(title="klgrm.xyz", message="You have entered an invalid URL.")
            

def callback(url):
   webbrowser.open_new_tab(url)


screen = Tk()
title = screen.title("klgrm.xyz - Youtube Downloader")
canvas = Canvas(screen, width=500, height=600, background="#262626")


#logo, and resize using subsample
logo = PhotoImage(file=get_path("tommy4.png")).subsample(3, 3)
canvas.create_image(250, 80, image=logo)


#Enter video link
link_label = Label(screen, text="Enter the link of your video: ", font=('Consolas', 15), bg="#262626", fg="white").place(relx=0.5, rely=0.45, anchor=CENTER)
link_field = Entry(screen, width=50)
link_field.pack()
link_field.place(relx=0.5, rely=0.5, anchor=CENTER)
canvas.create_window(250, 270, window=link_label)
canvas.create_window(250, 300, window=link_field)


#Button to select path
path_label = Label(screen, text="<download path>", bg="#262626", fg="white")
path_label.pack()
path_label.config(font=('Consolas', 15),)
path_label.place(relx=0.5, rely=0.58, anchor=CENTER)
path_button = Button(screen, text="Edit Path", font=('Consolas', 15), command=select_path).place(relx=0.5, rely=0.65, anchor=CENTER)
canvas.create_window(250, 340, window=path_label)
canvas.create_window(250, 370, window=path_button)


#Select file format/extension
format_options = [".mp3", ".mp4"]
form = StringVar(screen)
form.set("Format")
format_menu = OptionMenu(screen, form, *format_options)
format_menu.pack()
format_menu.config(font=('Consolas', 15))
format_menu.place(relx=0.5, rely=0.75, anchor=CENTER)


#Download button
download = Button(screen, text="Download", command=download_mp4, bg="green", font=('Consolas', 15)).place(relx=0.5, rely=0.85, anchor=CENTER)
canvas.create_window(250, 410, window=download)


#Footer
footer = Label(text="klgrm.xyz © 2022", bg="#262626", fg="white", font=('Consolas', 15, UNDERLINE))
footer.pack()
footer.place(relx=0.5, rely=0.95, anchor=CENTER)
footer.bind("<Button-1>", lambda e:
callback("http://klgrm.xyz"))


#Widgets will resize when window adjusted
canvas.pack(fill="both", expand=True)

screen.minsize(500, 600)
screen.maxsize(500, 600)
screen.mainloop()
 