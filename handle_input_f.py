import json as js 
import sys

def handle_input(arrays,user):

    if user == 'Q':
        out_file = open("testing.json", "w") 
        js.dump(arrays, out_file, indent = 6) 
        out_file.close()
        sys.exit()

    inputing = []

    for value in user:
        inputing.append(value)

    xAxis = inputing[0] #C
    yAxis = inputing[1] #2

    
    yAxis = int(yAxis)
    yAxis = yAxis - 1
    letters = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I']

    if xAxis in letters:
        xAxis = letters.index(xAxis)

    xAxis 
        
    inputted = (xAxis,yAxis)
    return inputted