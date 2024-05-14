import PySimpleGUI as sg
from controllers import downloader

layout = [  [sg.Text("Enter YT video URL (Link)")],
            [sg.InputText()],
            [sg.Button("Download"), sg.Button("Cancel")]
        ]

window = sg.Window("YT Donwloader", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Cancel":
        break

    downloader.downloadVideo(
        "", 
        values[0]
    )

    print("Hello", values[0], "!")

window.close()