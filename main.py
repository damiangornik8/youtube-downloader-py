# # # # # # # #
# 
# Youtube Audio and Video Downloader 
# 
# # # # # # # #
# 
# author: Damian Gornik
# 
# # # # # # # #
# 
# Before programme running, you need to install Pytube Module with command below:
# 
# $ pip install pytube
# 
# # # # # # # #

# from PYTUBE Module import YouTube Segment
from pytube import YouTube

# import Random Module, in order to get a random numbers to name a thumbnails
import random

# Import OS Module to convert videos into audio files
import os

# Define Class Downloader
class downloader:
    
    # YouTube Video Link to download
    vidLinkInput = ''

    # Initiate all Variables
    def __init__(self, vidLinkInput):
        self.vidLinkInput = vidLinkInput;

    # Download File as Video (in mp4 format) Function
    def downloadVid(self):
        
        # Informs the user that video is under downloading process
        print ("Video Downloading...")
        
        # Get YouTube Video Link from the user
        yt = YouTube(vidLinkInput)

        # Print out Video Title     
        print ("Title: ", yt.title)

        # Get all Video Files
        yt.streams
                # Select mp4 file format
                .filter(file_extension='mp4')
                # Order files by resolution 
                .order_by('resolution')
                # Get Video File in the highest possible res
                .first()
                # Download Video File
                .download()

        # Informs the user that the downloading process has been finished
        print("Video Downloaded!")

    # Download File as Audio (in mp3 format) Function
    def downloadAudio(self):
        # Informs the user that video is under downloading process
        print ("Audio Downloading...")
        
        # Get YouTube Video Link from the user
        yt = YouTube(vidLinkInput)

        # Print out Video Title     
        print ("Title: ", yt.title)

        # Get all Video Files
        yt.streams
                # Select mp4 file format
                .filter(file_extension='mp4')
                # Order files by resolution 
                .order_by('resolution')
                # Get Video File in the highest possible res
                .first()
                # Download Video File
                .download()

        # Informs the user that the downloading process has been finished
        print("Video Downloaded!")

        # Converting video file (mp4) into audio record (mp3)
        os.rename((yt.title+'.mp4'), (yt.title+'.mp3'));

    def downloadVidThumb(self):
        # Informs the user that video thumbnail is under downloading process
        print ("Thumbnail Downloading...")
        
        # Get YouTube Video Link from the user
        yt = YouTube(vidLinkInput)

        # Print out Video Title     
        print ("Title: ", yt.title)

        # Create a random name for a video thumbnail
        thumbnailName = random.randrange(1,10000)
        # Get a randomly generated name and join it with '.jpg' picture format
        thumbnailNameFull = str(thumbnailName) + '.jpg'
        # Download a Video Thumbnail
        urllib.request.urlretrieve(yt.thumbnail_url,thumbnailNameFull)

        # Informs the user that the downloading process has been finished
        print("Thumbnail Downloaded!")

# List of all Menu Choices
vidExtListChoice = ['1) Video (mp4)', '2) Audio (mp3)', '3) Thumbnail'];

# Get YouTube Video Link from the user
vidLink = input("Enter video link: ");

i = 0; 

# Display all downloading options available by 'for' loop  
for choice in vidExtListChoice:
    print (vidExtListChoice[i]);
    i += 1;

# Ask the user for what he want download to 
vidExt = int(input("Choose what you want to download [Type a Number]: ")) - 1;

# Initialize a Downloader Class
video = downloader(vidLink);

# Start a downloader class depending on choice made by user
if vidExt == 0:
    video.downloadVid();
elif vidExt == 1:
    video.downloadAudio();
elif vidExt == 2:
    video.downloadVidThumb();
