import pandas as pd
import generate

def readCSV(filename):
    csvFile = pd.read_csv(filename)
    
    rows = len(csvFile)
    
    data = [ dict(csvFile.iloc[i,:]) for i in range(0,rows) ]

    return data

def writeCSV(filename_write,filename_read,mathExpression):
    
    function = generate.generateEquation(mathExpression)
    data = readCSV(filename_read)
    responseList = []
    
    for i in range(0,len(data)):
        
        [id,*args] = data[i].values()
        
        value = function(*args)
        responseList.append(tuple((int(id),value)))

    df = pd.DataFrame({'ID': [ responseList[i][0] for i in range(0,len(responseList))],
                        'strength':[ responseList[i][1] for i in range(0,len(responseList))]})

    df.to_csv(filename_write,sep= ',', encoding='utf-8',index=False)
    