import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color('#fff')
layout = [
    [sg.Text("FTI UNISKA ANJAYYYY", font=('helvatica', 25))],
    [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=('Courier', 15,"italic","bold","underline"))],
    [sg.Text("UNISKA MAB BANJARMASIN")],
]

window = sg.Window(title='Profile', layout=layout, size=(600, 300), font=('Georgia', 20))
window()
window.close()
