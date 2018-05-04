import pandas as pd
import numpy as np

def select(df,**kwargs):
    idx = df[df.columns[0]]==df[df.columns[0]]
    for item in kwargs.keys():
        if item in df.columns:
            idx = idx & (df[item]==kwargs[item])
        else:
            return df.head(0)
    return df.loc[idx]

def select_range(df,**kwargs):
    sets = [df.query(item+'>='+str(kwargs[item][0])+' & '+item+'<='+str(kwargs[item][1])).index for item in kwargs]
    intersect = reduce(lambda a,b: a.intersection(b),sets)
    return df.loc[intersect]
