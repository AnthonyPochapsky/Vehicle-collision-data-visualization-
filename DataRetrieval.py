import csv
import pandas as pd

def getData():
    df=pd.read_csv('TorontoTrafficCollisions.csv')
    #Retain collision records recorded in March 2024 consisting of 5278 different records
    df = df.drop(df[df.OCC_YEAR != 2024].index)
    df = df.drop(df[df.OCC_MONTH != "March"].index)

    collision_info=[]
    for i in range(663936,669215):
        if (df['NEIGHBOURHOOD_158'][i] != "NSA") and (df['LONG_WGS84'][i] != 0) and (df['LAT_WGS84'][i] != 0):
            collision_info.append([str(df['LONG_WGS84'][i]),str(df['LAT_WGS84'][i]),str(df['OCC_DATE'][i]),str(df['NEIGHBOURHOOD_158'][i]),str(df['FATALITIES'][i]),str(df['INJURY_COLLISIONS'][i])])
    return collision_info
    