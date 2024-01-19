from pytube import YouTube
from moviepy.editor import VideoFileClip,AudioFileClip
import os

# Set Paths
MP4_PATH = "downloads\\MP4"
MP3_PATH = "downloads\\MP3\\"
TEMP_PATH = "temp"

# Function for checking whether the directories exist and creating them if not.
def check_dir():
    if not os.path.exists(MP4_PATH):
        os.makedirs(MP4_PATH)
    if not os.path.exists(MP3_PATH):
        os.makedirs(MP3_PATH)
    if not os.path.exists(TEMP_PATH):
        os.makedirs(TEMP_PATH)


def download_video(url):
    check_dir()
    
    #Get the YouTube Video
    video = YouTube(url)
    stream = video.streams.get_by_itag(22)
    
    try:
        #Try to download it to the path.
        stream.download(MP4_PATH)
    except Exception as e:
        print('An exception occurred')
        print(e)

        
def download_audio(url):
    check_dir()
    
    #These characters are not allowed in a file name
    invalid_chars = '\\/:*?"<>|'
    
    #Get the video
    init_video = YouTube(url)
    stream = init_video.streams.get_by_itag(22)
    
    #Set the name to the title of the video and remove all invalid characters
    name = init_video.title
    for char in invalid_chars:
        name = name.replace(char,'')
    
    try:
        #Try to download as a temporary MP4
        stream.download(TEMP_PATH,"temp.mp4")
    except Exception as e:
        print('An exception occurred')
        print(e)

    #Setup video for conversion       
    video = VideoFileClip('temp\\temp.mp4')
    
    #Convert into audio
    audio = video.audio
    
    #Write that audio to the mp3 path with the name
    audio.write_audiofile(f"{MP3_PATH}{name}.mp3")
    
    #remove the temporary file, making sure to close the other files in order to avoid an error of not being able to access.
    video.close()
    audio.close()
    os.remove('temp\\temp.mp4')
    
    