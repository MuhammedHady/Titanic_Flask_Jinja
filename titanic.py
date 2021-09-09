#########################################################################
########                   Adding Libraries                      ########
#########################################################################
from os import name
import re
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd    
import openpyxl
import csv
import numpy as np

#########################################################################
########                Numpy & Pandas Coding                    ########
#########################################################################

### Read CSV file
with open('titanic.csv', newline='\n') as csvfile:
    my_list = list(csv.reader(csvfile))
data = np.array(my_list)       ### Converting list to array
List=data[0]
Males=[]
Females=[]
Survivors=[]
LostChild=[]

num_of_arrays=data.shape[0]
print(num_of_arrays)

Males.append(List)             ### Adding indicators for Males file
Females.append(List)		   ### Adding indicators for Females file
Survivors.append(List)		   ### Adding indicators for Survivors file
LostChild.append(List)		   ### Adding indicators for LostChild file

### Getting all males formated as excel sheet 
for x in range (1,num_of_arrays):
	z = data[x,4]
	if z == 'male':
		y = data[x]
		Y = y.tolist()
		Males.append(Y)
print(Males)
pd.DataFrame(Males).to_csv("Males.csv")

### Getting all females formated as excel sheet
for x in range (1,num_of_arrays):
	z = data[x,4]
	if z == 'female':
		y = data[x]
		Y = y.tolist()
		Females.append(Y)
print(Females)
pd.DataFrame(Females).to_csv("Females.csv")

### Getting all survivors formated as excel sheet
for x in range (1,num_of_arrays):
	z = data[x,1]
	if z == '1':
		y = data[x]
		Y = y.tolist()
		Survivors.append(Y)
print(Survivors)
pd.DataFrame(Survivors).to_csv("Survivors.csv")

### Getting all LostChild formated as excel sheet
for x in range (1,num_of_arrays):
    q = data[x,1] 
    if q == '0':
        z = data[x,5]
        if z <= '17':
		        y = data[x]
		        Y = y.tolist()
		        LostChild.append(Y)
print(LostChild)
pd.DataFrame(LostChild).to_csv("LostChild.csv")

### Getting the Persentage of Survivors
Num_of_Survivors=len(Survivors)
print("\n Survivors : ",Num_of_Survivors)

Num_of_Passengers=len(my_list)-1
print("\n All Titanic Passengers : ",Num_of_Passengers)

Persentage = ( Num_of_Survivors / Num_of_Passengers ) * 100
PPP = '%.2f'%Persentage
print ("\n Survivors Persentage : %.2f"%Persentage,"%")

#########################################################################
########                 Flask & Jinja Coding                    ########
#########################################################################

### Adding Flask 
app = Flask('__name__')	

### Creating Main Page
@app.route('/')                                        
def mainpage():
    return render_template("Main.html",
                            title='Titanic Statistics',
                            page_head = ' Titanic Statistics ',
                            description = ' This is a Detailed Titanic Accident statistics ')

### Creating Survivors Page
@app.route('/Survivors' , methods=['GET', 'POST']) 
def Surviv():
    return render_template("Survivors.html",
                            title= 'Survivors',
                            page_head = ' The Survivors ',
                            description = ' This page shows all the titanic survivors ',
                            S_Data= Survivors)

### Creating Females Page
@app.route('/Females' , methods=['GET', 'POST']) 
def Femal():
    return render_template("Females.html",
                            title= 'Females',
                            page_head = ' The Females ',
                            description = ' This Page Shows All The Titanic Female passengers ',
                            F_Data= Females)

### Creating Males Page
@app.route('/Males' , methods=['GET', 'POST']) 
def Mal():
    return render_template("Males.html",
                            title= 'Males',
                            page_head = ' The Males ',
                            description = ' This Page Shows All The Titanic Male passengers ',
                            M_Data= Males)

### Creating Lost Childern Page
@app.route('/Lost Childern' , methods=['GET', 'POST']) 
def LSC():
    return render_template("Lost Childern.html",
                            title= 'Lost Childern',
                            page_head = ' The Lost Childern ',
                            description = ' This Page Shows All The Titanic Lost Childern ',
                            LC_Data= LostChild)

### Creating Survivors Persentage Page
@app.route('/Survivors Persentage' , methods=['GET', 'POST']) 
def SP():
    return render_template("Survivors Persentage.html",
                            title= 'Survivors Persentage',
                            page_head = ' The Survivors Persentage ',
                            description = ' This Page Shows The Survivors Persentage ',
                            SP_Data= PPP )

### Activating Flask on Port 5000 + Debuging mode
if __name__ == '__main__':
    app.run(debug=True, port=5000)

