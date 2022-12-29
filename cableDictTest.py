'''test for having saved data in dict for better referencnig access'''



#key: cbID	(cbType, cbCores, cbCSA(mm), cbDiameter, cbWeight(kg/m), cbArrangement)

cbDict = { 
'cb000' : ('Cu/XLPE/LSZH/AWA/LSZH', '1c', 50, 17.5, 0.8, 'Single'),
'cb001' : ('Cu/XLPE/LSZH/AWA/LSZH', '1c', 70, 20.2, 0.96, 'Single'),
'cb002' : ('Cu/XLPE/LSZH/AWA/LSZH', '1c', 95, 22.3, 1.24, 'Single')
}

def runDictTest():
    print(cbDict['cb001'])
    options0 = []
    for i in cbDict:
        if cbDict[i][0] not in options0:
            options0.append(cbDict[i][0])
            print(i, 'added')
    print(options0) # this is how i would list the options for cable selection
#runDictTest()

# if using a list:  

cbList = [
['cb000', 'Cu/XLPE/LSZH/AWA/LSZH', '1c', 50, 17.5, 0.8, 'Single'],
['cb001', 'Cu/XLPE/LSZH/AWA/LSZH', '1c', 70, 20.2, 0.96, 'Single'],
['cb002', 'Cu/XLPE/LSZH/AWA/LSZH', '1c', 95, 22.3, 1.24, 'Single']
]

print(cbList[1])
options1 = []
for i in range(len(cbList)):
    print(cbList[i])
    if cbList[i][1] not in options1:
        options1.append(cbList[i][1])
        print(i, 'added')
print(options1) # this is how i would list the options for cable selection

# could work as a list of tups or a dictionary. single dict would be cleaner i believe. work as is for now and hold in mind if list becomes too challenging.