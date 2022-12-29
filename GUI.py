import PySimpleGUI as sg


from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')


#---------------- matplotlib code here for now

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

def draw_figure(canvas, figure): # this comes out after merge
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

#----------------------


class Ladder:
    '''
    Main containment system class
    Ref, Type, Size
    '''
    def __init__(self, ldRef, ldType, ldWidth, ldHeight=0, ldWeight=0, circuits=[], physicalFill=0, electricalFill=0):
        self.ldRef = ldRef
        self.ldType = ldType
        self.ldWidth = ldWidth
        self.ldHeight = ldHeight
        self.ldWeight = ldWeight
        self.circuits = circuits
        self.physicalFill = physicalFill
        self.electricalFill = electricalFill


    def __str__(self): # string for ladder list, make uniqie so both can exist?
        return (self.ldRef)

    # def __str__(self): # string for details
    #     return (f'Instance of ladder class comprising:\nReference - {self.ldRef} \nType - {self.ldType}\nWidth - {self.ldWidth}\nHeight - {self.ldHeight}\nWeight - {self.ldWeight}\nCircuits - {self.circuits}\nPhysical fill - {self.physicalFill}\nElectrical fill - {self.electricalFill}')

# creating test ladders
ladders = []
ladders.append(Ladder('MSB-01', 'Heavy Duty', 900))
ladders.append(Ladder('MSB-02', 'Heavy Duty', 900))
ladders.append(Ladder('MSB-03', 'Heavy Duty', 900))

#------------------------- moving to columns inside here:

col2 = sg.Column([[sg.Frame('Ladder Visualisation:', [[sg.Text(), sg.Column([
                            [sg.Canvas(key='-CANVAS-')],
                             ], size=(525,425), pad=(0,0))]])], ], pad=(0,0))                                                      

col1 = sg.Column([
    # Categories sg.Frame
    [sg.Frame('Ladders:',[
    [sg.Text('Ladder Ref:', size=(15, 1)), sg.Input(key = '-IN1-', size=(15, 1))], # can use get methods to retrieve current value
    [sg.Text('Duty:', size=(15, 1)), sg.OptionMenu(('Extra Heavy Duty', 'Heavy Duty', 'Medium Duty'), default_value = 'Extra Heavy Duty', key = '-IN2-', size=(15, 1))],
    [sg.Text('Size:', size=(15, 1)), sg.OptionMenu((900, 750, 600, 450, 300, 225, 150), default_value = 900, key = '-IN3-', size=(15, 1))],
    [sg.Button('Add Ladder', size=(15, 1)),sg.Button('Delete Ladder', size=(15, 1))],
    [sg.Text('Search:', size=(15, 1))],
    [sg.Input(size=(20, 1), enable_events=True, key='-INPUT-'), sg.Button('Refresh', size=(15, 1))],
    [sg.Listbox(ladders, size=(30, 4), enable_events=True, key='-LIST-')]])],
    # Information sg.Frame
    [sg.Frame('Information:', [[sg.Text(), sg.Column([[sg.Text('Graph:')],
                            
                             ], size=(50,50), pad=(0,0))]])], ], pad=(0,0))

col3 = sg.Column([[sg.Frame('Actions:',
                            [[sg.Column([[sg.Button('Save'), sg.Button('Clear'), sg.Button('Delete'), ]],
                                        size=(450,45), pad=(0,0))]])]], pad=(0,0))

# The final layout is a simple one
layout = [[col1, col2],
          [col3]]


#-------------------------
'''
layout = [
    [
    [sg.Text('Ladder Ref:', size=(15, 1)), sg.Input(key = '-IN1-', size=(15, 1))], # can use get methos to retrieve current value
    [sg.Text('Duty:', size=(15, 1)), sg.OptionMenu(('Extra Heavy Duty', 'Heavy Duty', 'Medium Duty'), default_value = 'Extra Heavy Duty', key = '-IN2-', size=(15, 1))],
    [sg.Text('Size:', size=(15, 1)), sg.OptionMenu((900, 750, 600, 450, 300, 225, 150), default_value = 900, key = '-IN3-', size=(15, 1))],
    [sg.Button('Add Ladder', size=(15, 1)),sg.Button('Delete Ladder', size=(15, 1))],
    [sg.Text('Search:', size=(15, 1))],
    [sg.Input(size=(20, 1), enable_events=True, key='-INPUT-'), sg.Button('Refresh', size=(15, 1))],
    [sg.Listbox(ladders, size=(30, 4), enable_events=True, key='-LIST-')]
],
[sg.Canvas(key='-CANVAS-')]
]
'''
window = sg.Window('Containment Calculator', layout, finalize=True,)

fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'Add Ladder':
        values['-IN1-'] = ladders.append(Ladder(values['-IN1-'], values['-IN2-'], values['-IN3-']))
    if event == 'List':
        for i in ladders:
            print(i)

window.close()

'''
I need to add classes to a list right?
then i can itterate through the list
'''