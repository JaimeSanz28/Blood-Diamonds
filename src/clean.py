import pandas as pd

def numeric(df):
    df.replace({'cut':{'Fair':1, 'Good':2, 'Very Good':3, 'Ideal':4, 'Premium':5,}}, inplace=True)
    df.replace({'color': {'F':1, 'E':2, 'D':3, 'H':4, 'G':5, 'J':6, 'I':7}}, inplace=True)
    df.replace({'clarity': {'VS2':1, 'SI1':2, 'VS1':3, 'SI2':4, 'VVS2':5, 'VVS1':6, 'IF':7, 'I1':8}}, inplace=True)
    