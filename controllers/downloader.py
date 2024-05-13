from pytube import Youtube

# Path of where you will save your video 
# Set your own path
SAVE_PATH = ""

# Link of the video to download
link = ""

try:
    yt = Youtube(link)
except:
    print("Connection Error")

#  Get all streams and filter for mp4 files
mp4_streams = yt.streams.filter(file_extension='mp4').all()

# Get the video with the highest resolution
d_video = mp4_streams[-1]

try:
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except:
    print("Some Error!")