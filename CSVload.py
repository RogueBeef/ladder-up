import csv
import pickle

def importCableData():
    '''Takes data from CWF file 'cabledata', exports as list of rows-lists as pickle file'''
    cableList = []

    with open('cabledata.csv', 'r') as file: # write to list
        reader = csv.reader(file)
        rowcount =1
        for row in reader:
            if rowcount ==1:
                rowcount+=1
            else:
                cableList.append(tuple(row))

    with open('cabledata.pickle', 'wb') as handle: # save
        pickle.dump(cableList, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('cabledata.pickle', 'rb') as handle: #load test
        cableListCopy = pickle.load(handle)
    # Load test:
    print(cableList == cableListCopy)
    #Load example:
    print(cableListCopy[22])


def importCleatData():
    '''Takes data from CWF file 'cleatdata', exports as list of rows-lists as pickle file'''
    cleatList = []

    with open('cleatdata.csv', 'r') as file:
        reader = csv.reader(file)
        rowcount =1
        for row in reader:
            if rowcount ==1:
                rowcount+=1
            else:
                cleatList.append(tuple(row))
    
    with open('cleatdata.pickle', 'wb') as handle:
        pickle.dump(cleatList, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('cleatdata.pickle', 'rb') as handle:
        cleatListCopy = pickle.load(handle)
    # Load test:
    print(cleatList == cleatListCopy)
    #Load example:
    print(cleatListCopy[22])


def importLadderData():
    '''Takes data from CWF file 'ladderdata', exports as list of rows-lists as pickle file'''
    ladderList = []

    with open('ladderdata.csv', 'r') as file:
        reader = csv.reader(file)
        rowcount =1
        for row in reader:
            if rowcount ==1:
                rowcount+=1
            else:
                ladderList.append(tuple(row))
    
    with open('ladderdata.pickle', 'wb') as handle:
        pickle.dump(ladderList, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('ladderdata.pickle', 'rb') as handle:
        ladderListCopy = pickle.load(handle)
    # Load test:
    print(ladderList == ladderListCopy)
    #Load example:
    print(ladderListCopy[:])


#importCableData()
#mportCleatData()
#importLadderData()