from pytube import YouTube  # Import the YouTube class from the pytube library

def downloadVideo(savePath, link):
    """
    Download a YouTube video given its URL.

    Args:
        savePath (str): The directory where the video will be saved.
        link (str): The URL of the YouTube video.

    Returns:
        None
    """
    try:
        yt = YouTube(link) # Create a YouTube object with the provided URL
    except Exception as e:
        print("Error creating Youtube object:", e) # Print error message if connection fails

    #  Get all streams and filter for mp4 files
    mp4_streams = yt.streams.filter(file_extension='mp4')

    # Get the video with the highest resolution
    d_video = mp4_streams[-1]

    try:
        # Download the video to the specified savePath
        d_video.download(output_path=savePath)
        print('Video downloaded successfully!') # Print success message
    except Exception as e:
        print("Error downloading video:", e) # Print error message if download fails