import pandas as pd
import numpy as np

msft= pd.read_csv("sample.csv")   #creating an object to read the excel sheet
#print(msft.head())                # to print the excel sheet

df=msft.head()

df.to_excel("sample.xlsx")    #to convert it to json file

df=pd.read_excel("sample.xlsx")    #to read json file

print(df.head())                   #print json file