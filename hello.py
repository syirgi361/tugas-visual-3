import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#ffff00")
window = sg.Window(title="prifile",
         layout=[[sg.Text("FTI UNISKA")],
                 [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
                 [sg.Text("UNISKA MAB BANJARMASIN")]],
                   size=(500,500),
                   font=("times",20))
window()
window.close()