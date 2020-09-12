from django import forms

class CsvForm(forms.Form):  
    filetitle = forms.CharField(label="Enter file name",max_length=50)  
    #lastname = forms.CharField(label="Enter last name", max_length = 10)  
    #email = forms.EmailField(label="Enter Email")  
    file = forms.FileField() # for creating file input  