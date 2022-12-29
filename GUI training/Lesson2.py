import PySimpleGUI as sg


layout = [[sg.Text('Do you want to continue?')],
[sg.Button('Yes'), sg.Button('No')]]

# window = sg.Window('Title', layout) # you can also place your layout in the window call instead of referencing through a layout

# event, values = window.read()

# print(event) # events are keys which equal the button text

# window.close() # this is the x button on headder



window = sg.Window('Title', layout)

while True: # thispersistant window will receive continuous inputs
    event, values = window.read()
    if event ==sg.WIN_CLOSED:
        break
    elif event == 'Yes':
        print('indeed')
    elif event == 'No':
        print('too bad')
    print(event)
window.close()

#sg.theme_previewer()