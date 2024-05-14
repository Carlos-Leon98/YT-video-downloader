from pytube import Youtube

def downloadVideo(savePath, link):
    try:
        yt = Youtube(link)
    except:
        print("Connection Error")

    #  Get all streams and filter for mp4 files
    mp4_streams = yt.streams.filter(file_extension='mp4').all()

    # Get the video with the highest resolution
    d_video = mp4_streams[-1]

    try:
        d_video.download(output_path=savePath)
        print('Video downloaded successfully!')
    except:
        print("Some Error!")