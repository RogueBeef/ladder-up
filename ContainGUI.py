import PySimpleGUI as sg


testLadders = ('MSB-01','MSB-02','MSB-03','LR-01','LR-02','LR-03','EG-01')
testCircuits = ('MSB-01-01','MSB-02-01','MSB-03-01','LR-01-03','LR-01-02','LR-01-01','EG-01-01')


layout = [  [sg.Text('Ladder selection:'),],
            [sg.Listbox(sorted(testLadders), size=(20, 10), key='-LAD-', enable_events=True)]
            [sg.Text('Circuit selection:'),],
            [sg.Listbox(sorted(testCircuits), size=(20, 10), key='-CABLE-', enable_events=True)]
             ]

window = sg.Window('Pick a color', layout)

while True:                  # the event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values['-LAD-']:    # if something is highlighted in the list
        print('Plot ladder within here')
    #if values['-CCT-']:    # if something is highlighted in the list
     #   print('Bring up cabls within cable list')
window.close()


