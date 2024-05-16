import PySimpleGUI as sg # Import the PySimpleGUI library as sg
from controllers import downloader # Import the downloader module from the controllers package

def set_user_interface():
    # Define the layout of the GUI window using PySimpleGUI elements
    layout = [  [sg.Text("Enter YT video URL (Link)")], # Text element prompting user to enter a YouTube video URL
                [sg.InputText()], # Input field for the user to enter the URL
                [sg.Button("Download"), sg.Button("Cancel")] # Download and Cancel buttons
            ]

    # Create a PySimpleGUI window with the specified layout
    window = sg.Window("YT Donwloader", layout) # Title the window as "YT Downloader"

    # Loop to handle events and interact with the GUI
    while True:
        event, values = window.read() # Read events and values from the window

        # If the window is closed or the user clicks the "Cancel" button, exit the loop
        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        # Call the downloadVideo function from the downloader module with the provided URL
        YT_video = downloader.downloadVideo(
            "src/videos/", # Save path
            values[0], # URL provided by the user
            137 # Itag to choose the video resolution
        )

        if YT_video:
            # Print message to confirm the downloaded video
            print("YT video from link:", values[0], "was downloaded successfully")
        else:
            # Print message saying something went wrong downloading the video
            print("Something unexpected happened, please try again later.")
        

        

    window.close() # Close the PySimpleGUI window when the loop exits