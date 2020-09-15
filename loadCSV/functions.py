def handle_uploaded_file(f):  
    with open('static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

def readCSVHeader(filename):
    import csv
    import pandas as pd
    return pd.read_csv('static/upload/'+filename, nrows=0).columns.tolist()
    #pd.read_csv('test.csv', index_col=0, nrows=0).columns.tolist()

def readCSVData(filename):
    import csv
    import pandas as pd
    return pd.read_csv('static/upload/'+filename)

    