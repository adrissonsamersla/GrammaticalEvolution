import pandas as pd

def readCSV(filename):
    csvFile = pd.read_csv(filename)
    
    rows = len(csvFile)
    
    data = [ dict(csvFile.iloc[i,:]) for i in range(0,rows) ]

    return data

