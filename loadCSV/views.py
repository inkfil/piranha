# Django imports
from django.shortcuts import render
from django.http import HttpResponse

from loadCSV.forms import CsvForm
from loadCSV.functions import handle_uploaded_file, readCSVHeader, readCSVData


# other imports
import numpy as np
import pandas as pd

# Create your views here.

def indexCSV(request):
    return HttpResponse("Hello, world. You're at the loadCSV index.")

def uploadCSV(request):
    if request.method == 'POST':  
        csv = CsvForm(request.POST, request.FILES)  
        if csv.is_valid():
            handle_uploaded_file(request.FILES['file'])
            cols=readCSVHeader(request.FILES['file'].name)
            print(cols)
            return render(request, "dispCSV.html", {'data':cols})
    else:  
        csv = CsvForm()
        return render(request,"loadCSV.html",{'form':csv}) 

def dispCSV(request):
    pass

#______________________________________________________________________________
# Features
#______________________________________________________________________________

def getCols():
    pass

def getColsValues():
    pass

def getColsType():
    pass

def getNumRows():
    pass

def getNumCols():
    pass

def getMissingData():
    pass

#______________________________________________________________________________
# Delimiters
#______________________________________________________________________________

def addDelimeter():
    pass
