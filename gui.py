import tkinter as tk
import callbacks as call


### Setting up a Basic GUI
ROOT = tk.Tk()
ROOT.geometry("900x600")
ROOT.title("YouTube Converter")

# Font Size Variables
FONT_SMALL = ('Arial', 14)
FONT_REGULAR = ('Arial', 16)
FONT_LARGE = ('Arial', 20)


#The main function that is called in app.py
def draw_window():
    ROOT.mainloop()


# Setting the text based on if there is a download, or if it's complete
def set_downloading():
    clear_url()
    download_label.config(text="Downloading!")


def set_complete():
    download_label.config(text="Complete! You can now do another video!")

    
def set_error():
    download_label.config("Something went wrong. Try again.")


#Clearing the url box.
def clear_url():
    url_box.delete(0,tk.END)


# On Click event for the mp4 button. Gets the url from the box and calld the download video from callbacks.
def mp4_button_press():
    url = url_box.get()
    set_downloading()
    ROOT.after(100,call.download_video(url))
    set_complete()
    
    
# On Click event for the mp3 button. Gets the url from the box and calld the download audio from callbacks.
def mp3_button_press():
    url = url_box.get()
    set_downloading()
    ROOT.after(100,call.download_audio(url))
    set_complete()


# Setting of the labels and frames.    
title = tk.Label(ROOT, font=FONT_LARGE, text="Youtube Converter")
title.pack()

url_frame = tk.Frame(ROOT)
url_frame.pack()

url_text = tk.Label(url_frame,font=FONT_REGULAR,text="Url of YouTube video: ")
url_text.pack(side=tk.LEFT)
url_box = tk.Entry(url_frame, font=FONT_REGULAR)
url_box.pack(side=tk.LEFT)

button_frame = tk.Frame(ROOT)
button_frame.pack()

#Command has the callback function.
mp4_button = tk.Button(button_frame,font=FONT_REGULAR,text="MP4",command=mp4_button_press)
mp3_button = tk.Button(button_frame,font=FONT_REGULAR, text="MP3",command=mp3_button_press)
mp4_button.pack(side=tk.LEFT, pady=5, padx=5)
mp3_button.pack(side=tk.LEFT, pady=5, padx=5)

download_frame = tk.Frame(ROOT)
download_frame.pack(padx=10,pady=10,fill='x')
download_label = tk.Label(button_frame,font=FONT_LARGE,text="")
download_label.pack()