import pandas as pd

def numeric(df):
    df.replace({'cut':{'Fair':1, 'Good':2, 'Very Good':3, 'Ideal':4, 'Premium':5,}}, inplace=True)
    pass