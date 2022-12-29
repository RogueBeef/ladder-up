'''
there are 5 sections to pysimpleGUI
'''
#1 - importing
import PySimpleGUI as sg
#sg.set_options(font='Default 12', keep_on_top=False)

#2 - layout - defines interior of window - is a list of lists

layout = [
            [sg.Text('Hello World!')],
            [sg.Button('Ok')],
            [sg.Button('Ok')],
            [sg.Button('Ok'), sg.Button('Ok')],
]
# each imbedded list is a row within the program

# 3 - window

window = sg.Window('title', layout)

# 4 - event loop / handling
event, value = window.read()

# 5 - close

window.close()