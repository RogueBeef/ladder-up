'''
This program (will) commence a tool for entering cable, ladder & system identity data for the purpose of calculating containment sizes and printing CSV files of containment routing information.

it will take in CSV files for cable data (ladder data will be default for now)




CONTAONMENT CALC NEXT STEPS:
----------------------------

- create a test project, auto-load for now
/ - ladder selection to select on click
- circuits on ladder to be seperate


I NEED TO CREATE TWO LISTS THAT WILL SERVE AS THE PROJECT DATA
LIST 1 IS SERIES OF LADDERS, NAMES, REFS, YUPES ETC.
LIST 2 IS SERIES OF CIRCUITS.
LADDERS CREATED
CIRCUITS CREATED INDEPENDANTLY
LADDER WILL HAVE A CIRCUITS-ON-LADDER LIST TO HOLD DATA
THIS MEANS CIRCUITS CAN BE LOADED IN SEPERATELY.
HOW THEN DO I MANAGE IF SOMEONE DELETES A CIRCUIT.
    WILL NEED A WARNING POPUP TO STATE THIS CIRCUIT IS ON THESE LADDERS.

TO EDIT LADDER / CIRCUIT DETAILS, PUT IN THE SAME REF



'''

import numpy as np
import matplotlib.pyplot as plt
import pickle
import PySimpleGUI as sg

#from matplotlib.ticker import NullFormatter  # useful for `logit` scale - NOT SURE IF NEEDED
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import matplotlib
#matplotlib.use('TkAgg')




def loadData(cableList, cleatList, ladderList):
    '''loads cable, cleat & ladder data from pickle files'''

    with open('cabledata.pickle', 'rb') as handle:
        cableList = pickle.load(handle)

    with open('cleatdata.pickle', 'rb') as handle:
        cleatList = pickle.load(handle)

    with open('ladderdata.pickle', 'rb') as handle:
        ladderList = pickle.load(handle)

    return cableList, cleatList, ladderList


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

        ldWidth = int(ldWidth) 
        ldWidth -=5 # accounts for how much smallers ladders are than their stated falue

    def __str__(self): # string for ladder name, used in list boxes
        return (self.ldRef)

#    def __str__(self): # string for ladder full details, on hold for now
#        return (f'Instance of ladder class comprising:\nReference - {self.ldRef} \nType - {self.ldType}\nWidth - {self.ldWidth}\nHeight - {self.ldHeight}\nWeight - {self.ldWeight}\nCircuits - {self.circuits}\nPhysical fill - {self.physicalFill}\nElectrical fill - {self.electricalFill}')

    def addCable(self, circuit):
        self.circuits.append(circuit)
        #print(self.circuits)
        #print(f'self.circuit len = {len(self.circuits)}')
        #self.physicalFill+= cable[1]
        self.calcFill()
        return #print(f'Physical fill = {self.physicalFill}')

    def calcFill(self):
        tempFill = 0
        #print(len(self.circuits))
        for i in self.circuits:
            #print('in for loop')
            if i[1][2] == '1': # i.e. multicore
                tempFill+= i[2][1]
                #print(tempFill)
        self.physicalFill = tempFill
        return



    def drawLadder(self, ldRef, ldWidth):
        '''Plots ladder '''
        
        # Ladder particulars & constants:
        ldWidth = ldWidth
        ldHeight = 120
        ldDepth = -30
        ldBot = -22
        ldLS = -25
        ldRS = ldWidth+25
        ladderName = ldRef + ' - ' +str(ldWidth) + 'mm Heavcy Duty Ladder'
        cableQuantity = 1

        # build ladder frame:
        leftWall = plt.Line2D((ldLS, 0, 0, ldLS), (ldDepth, ldDepth, ldHeight, ldHeight), c='k', lw=1.5)
        ladderRung = plt.Line2D((0, ldWidth, ldWidth, 0), (0, 0, ldBot, ldBot), c='k', label=ladderName, lw=1.5)
        rightWall = plt.Line2D((ldRS, ldWidth, ldWidth, ldRS), (ldDepth, ldDepth, ldHeight, ldHeight), c='k', lw=1.5)
        spaceForLegend = plt.Line2D((-40,-40), (0,200+50*cableQuantity), c='w', lw=0.1)
        
        # build cables:

        #plt.axes()
        plt.figure(ldRef)
        plt.title(ldRef)
        plt.gca().add_line(leftWall)
        plt.gca().add_line(ladderRung)
        plt.gca().add_line(rightWall)
        plt.gca().add_line(spaceForLegend)
        plt.legend(loc=2)
        plt.axis('scaled')

        plt.show()

# class Ladder end

class Circuit:
    '''
    Main circuit configuration class
    Circuit configuration is defined as:
        X.Y.Z = X parallel conductors
                Y cables comprising each parallel path
                Z cores per cable
        e.g. 10x4x1 = 10 parallel conductors, 4 cables per circuit, 1 core per cable (therefore singles)

    CPCs omitted for now, can be manually inputted if needed for spacing

    For circuit data, user can either read in circuits from excel (learn pandas) or enter manually, either way I need a data structure for circuits.

    - - ctID - unique ID generated upon creating, could this be the name of the class identity?
    0 - ctRef - the name of the circuit from tables e.g. 
    1 - ctFrom
    2 - ctTo
    3 - ctConfig
    4 - ctCSA
    5 - 

    instead of assigning all the cable parameters, should i tie them into one of the cbIDs from the cable data? - this will give more governance (validity ensurance) - yes
    '''
    def __init__(self, cbID, cbFrom, cbTo, cbConfig, cbCSA, cbType, cbDiameter=0, cbWeight=0, cbBendRadii=0):
        self.cbID = cbID
        self.cbFrom = cbFrom
        self.cbTo = cbTo
        self.cbConfig = cbConfig
        self.cbCSA = cbCSA
        self.cbType = cbType
        self.cbDiameter = cbDiameter
        self.cbWeight = cbWeight
        self.cbBendRadii = cbBendRadii

    def __str__(self): # string for circuit name, used in list boxes
        return (self.cbID)

    def getDiameter(type, CSA):
        '''Lookup for diameter'''
        # returns diameter of single cable

# circuit class end

def identifyCable(cableList):
    for i in cableList:
        # locate cable ID within cable list and return cable ID in place of size, cores, type
        pass


def testLadderPlot():

    print (testLadder)
    testLadder.drawLadder('MSB-01', 900)


#def main():

cableList = None
cleatList = None
ladderList = None
loadData(cableList, cleatList, ladderList)
# creating test ladders
testLadder = Ladder('MSB-01', 'Heavy Duty', 900)
#plotty = testLadder.drawLadder('MSB-01', 900)
ladders = []
ladders.append(Ladder('MSB-01', 'Heavy Duty', 900))
ladders.append(Ladder('MSB-02', 'Heavy Duty', 900))
ladders.append(Ladder('MSB-03', 'Heavy Duty', 900))

circuits = []
testCircuit = ('PDU-N1-1-2', 'PDU-N1-1', 'RB-MPOE1-02-2A', ('1','1','4c'), '120', 'N2XH Enhanced Flex') # SHOULD I MAKE A TYPE DECTIONARY?
circuits.append(Circuit('PDU-N1-1-2', 'PDU-N1-1', 'RB-MPOE1-02-2A', ('1','1','4c'), '120', 'N2XH Enhanced Flex'))

selectedLadder = 'None'


def getCircuits():
    if selectedLadder == 'None': return ['Select a ladder']
    else:
        tempList = []
        for i in selectedLadder.circuits:
            tempList.append(i)
        return tempList



#ladderRef = 'Test'
#ladders[1].drawLadder()



#testCircuit1 = ('MSB-01-01', '2x1x4c', cbID002)
#testCircuit2 = ('MSB-01-02', '2x1x4c', cbID002)


    #-------- START OF GUI AREA---------#


col2 = sg.Column([[sg.Frame('Add / Delete Circuits', [ # look to get rid of this unnecessary column
                            [sg.Text('Selected ladder: ', size=(15, 1)),sg.Text(size=(50,1), key='-SELECT-')],
                            
                            [sg.Text('Circuit Ref:', size=(15, 1)), sg.Input(key = '-INC1-', size=(15, 1))],
                            [sg.Text('From / Origin:', size=(15, 1)), sg.Input(key = '-INC2-', size=(15, 1))],
                            [sg.Text('To / Destination:', size=(15, 1)), sg.Input(key = '-INC3-', size=(15, 1))],
                            [sg.Text('Configuration: (X parallel conductors, Y cables in circuit, Z cores per cable)', size=(60, 1))],
                            [sg.Text('X:', size=(2, 1)), sg.Input(key = '-INC4-', size=(5, 1)), sg.Text('Y:', size=(2, 1)), sg.Input(key = '-INC5-', size=(5, 1)), sg.Text('Z:', size=(2, 1)), sg.Input(key = '-INC6-', size=(5, 1))],
                            [sg.Text('CSA:', size=(15, 1)), sg.Input(key = '-INC7-', size=(15, 1))],
                            [sg.Text('Type:', size=(15, 1)), sg.Input(key = '-INC8-', size=(15, 1))],
                            ])],
                            [sg.Frame('Circuit Management', [
                            [sg.Text('Search:', size=(15, 1))],
                            [sg.Input(size=(20, 1), enable_events=True, key='-CINPUT-')],
                            [sg.Text('Circuits: ', size=(15,1))], [sg.Listbox(circuits, size=(30,4), key='-CCTS-')],
                            [sg.Button('Add to ladder', size=(15, 1))],
                             ])], ], pad=(0,0))                                                      

col1 = sg.Column([
    # Ladder add/delete frame
    [sg.Frame('Ladder add / delete',[
    [sg.Text('Ladder Ref:', size=(15, 1)), sg.Input(key = '-IN1-', size=(15, 1))], # can use get methods to retrieve current value
    [sg.Text('Duty:', size=(15, 1)), sg.OptionMenu(('Extra Heavy Duty', 'Heavy Duty', 'Medium Duty'), default_value = 'Extra Heavy Duty', key = '-IN2-', size=(15, 1))],
    [sg.Text('Size:', size=(15, 1)), sg.OptionMenu((900, 750, 600, 450, 300, 225, 150), default_value = 900, key = '-IN3-', size=(15, 1))],
    [sg.Button('Add Ladder', size=(15, 1)),sg.Button('Delete Ladder', size=(15, 1))],
    ])],
    # Ladder selection frame (maybe move delete here?)
    [sg.Frame('Ladder Selection', [
    [sg.Text('Search:', size=(15, 1))],
    [sg.Input(size=(20, 1), enable_events=True, key='-LINPUT-'), sg.Button('Refresh L', size=(15, 1))],
    [sg.Listbox(ladders, size=(30, 4), enable_events=True, key='-LLIST-')]
    ])],
    # Circuit management
    [sg.Frame('Circuits on Ladder', [
    
    
    [sg.Listbox(['All cct function here later'], size=(30, 4), enable_events=True, key='-CLIST-')],
    [sg.Button('Remove circuit', size=(15, 1))]


                             ])], ], pad=(0,0))

col3 = sg.Column([[sg.Frame('Functions',
                            [[sg.Column([[sg.Button('Plot ladder'), sg.Button('Export calculation'), sg.Button('Load project'),sg.Button('Save project'),sg.Button('Refresh') ]],
                                        size=(850,40), pad=(0,0))]])]], pad=(0,0))

''' - to go in cable data:
Circuits on ladder:
list of them

Populate from existing circuit
search


Circuit ID []
From []
To []
Configuration (X parallel conductors, Y cables in circuit, Z cores per cable)
X-[] Y-[] Z-[]
CSA []
Type []

Add

'''



# The final layout is a simple one
layout = [[col1, col2],
          [col3]]

window = sg.Window('Containment Calculator', layout, finalize=True,)

#fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

while True: # MAIN GUI WINDOW LOOP AWAITING INPUT
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'Plot ladder':
        testLadderPlot()
        #insert plot func
        pass
    if event == 'Add Ladder':
        print('Adding ladder...')
        values['-IN1-'] = ladders.append(Ladder(values['-IN1-'], values['-IN2-'], values['-IN3-']))
    if event == 'List':
        for i in ladders:
            print(i)
    if event == 'Refresh':
        print('refreshing...')
        window['-LLIST-'].update(ladders)
        #window['-CLIST-'].update(addfunc?)
        window['-LADCCTS-'].update()

    
    if values['-LINPUT-'] != '':                         # if a keystroke entered in search field
        search = values['-LINPUT-']
        new_values = []
        for i in ladders:
            if search in i.ldRef: # replace with getter function of string later, str(i) ?
                new_values.append(i)
        window['-LLIST-'].update(new_values)     # display in the listbox
    
    # if a list item is chosen
    if event == '-LLIST-' and len(values['-LLIST-']):
        selectedLadder = values['-LLIST-'][0]
        sg.popup('Selected ', str(selectedLadder))
        window['-SELECT-'].update(str(selectedLadder)) # again replace with string getter later
        

window.close()

    #-----------END OF GUI AREA---------#



#if __name__ == "__main__":
#    main()


# -----UNUSED CODE-----


#       --- USING THE OLD ONLINE PLOTTING MODULE ---
# def drawCables(cable):
#     '''If "circle", a circle is drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with respect to the axes' sizing mode'''
    
#     cleatWidth = calcCleatSize(cable)

#     fig.add_shape(type="rect",
#         x0=(0), y0=(0),
#         x1=(cleatWidth), y1=(cleatWidth),
#         line_color="red",
# ) # cleat

#     print(cleatWidth)
#     print(cable)
#     print(cleatWidth-cable)
#     centreNudge = (cleatWidth-cable)/2
#     fig.add_shape(type="circle",
#         x0=(centreNudge), y0=(centreNudge),
#         x1=(centreNudge+cable), y1=(centreNudge+cable),
#         line_color="red",
# ) # cable, (cleatWidth-cable)/2 is centering cable in cleat - not perfect yet...

# def calcCleatSize(cable):
#     '''Later this needs to reference a catalogue and return the true sizes'''
#     return cable*1.2

# size = 900

# #drawLadder(size)

# #cable = input('Enter cable diameter ')
# cable = 75
# #drawCables(cable)

# #fig.update_shapes(dict(xref='x', yref='y'))
# #fig.show()