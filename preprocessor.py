import pandas as pd
import numpy as np

def preprocess(us_mass_shooting):
    # Let's replace the empty strings with NaN values
    us_mass_shooting = us_mass_shooting.replace(' ', np.nan)
    # Let's replace the question marks (?) with NaN values
    us_mass_shooting = us_mass_shooting.replace('?', np.nan)
    # Let's replace the question marks (.) with NaN values
    us_mass_shooting = us_mass_shooting.replace('.', np.nan)
    
    # check duplicates
    us_mass_shooting.duplicated().sum()
    
    # check missing values
    us_mass_shooting.isna().sum()
    
    # dealing with missing values
    us_mass_shooting['MENTALHEALTHSOURCES'].fillna(us_mass_shooting['MENTALHEALTHSOURCES'].mode()[0], inplace=True)
    us_mass_shooting['MENTALHEALTHNOTES'].fillna(us_mass_shooting['MENTALHEALTHNOTES'].mode()[0], inplace=True)
    us_mass_shooting['WEAPONSOBTAINEDLEGALLY'].fillna(us_mass_shooting['WEAPONSOBTAINEDLEGALLY'].mode()[0], inplace=True)
    
    # drop/delete these columns 
    us_mass_shooting.drop(columns=['LATITUDE', 'LONGITUDE'], inplace=True)
    
    return us_mass_shooting