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
    stream = yt.streams.get_by_itag(137)

    try:
        # Download the video to the specified savePath
        stream.download(output_path=savePath)
        print('Video downloaded successfully!') # Print success message
        return True
    except Exception as e:
        print("Error downloading video:", e) # Print error message if download fails
        return False