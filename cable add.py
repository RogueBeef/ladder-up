'''
so i need to keep track of twp numbers in a class, physical spatial takeup and thermal spatial takeup

these should be class instance variables

when adding or subtrscting a cable, thats when the calculation happens

plotting happens also then, and when cresting a new instsnce of ladder
'''

		

class Ladder:
    '''
    Main containment system class
    '''
    def __init__(self, ldRef, ldType, ldWidth, ldHeight=0, ldWeight=0, circuits=[], physicalFill=0, thermalFill=0):
        self.ldRef = ldRef
        self.ldType = ldType
        self.ldWidth = ldWidth
        self.ldHeight = ldHeight
        self.ldWeight = ldWeight
        self.circuits = circuits
        self.physicalFill = physicalFill
        self.thermalFill = thermalFill

        ldWidth -=5 # accounts for how much smallers ladders are than their stated falue

    def __str__(self):
        return (f'Instance of ladder class comprising:\nReference - {self.ldRef} \nType - {self.ldType}\nWidth - {self.ldWidth}\nHeight - {self.ldHeight}\nWeight - {self.ldWeight}\nCircuits - {self.circuits}\nPhysical fill - {self.physicalFill}\nThermal fill - {self.thermalFill}')

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
    		

testLadder = Ladder('MSB-01', 'Heavy Duty', 900)

print(testLadder)

#test mcable 1(multicore): size, diameter - add arrangement later


cbID002 =  (500, 112.3) # ID, size, OD - may need.to.rethink how to store the cable data

#circuit data - cct-ref, arrangement(xyz - parallel stream, cables/stream, cores/cable), size
testCircuit1 = ('MSB-01-01', '2x1x4c', cbID002)
testCircuit2 = ('MSB-01-02', '2x1x4c', cbID002)

testLadder.addCable(testCircuit1)
testLadder.addCable(testCircuit2)
#print(testLadder.circuits)
#print('')
#print(testLadder.physicalFill)

print('')

print(testLadder)

# function works, needs addition to deal with single-core & some optimising