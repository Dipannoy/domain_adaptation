import pandas as pd
import numpy as np
import os,sys

import os,sys


cwd=os.getcwd()


def list_generator(csv_file,index,value_list):
    lst_dict=[]
    df=pd.read_csv(csv_file)
    for entries in value_list:
        dict_in=pd.Series(df[entries].values,index=df[index]).to_dict()
        lst_dict.append(dict_in)
    return df,lst_dict

df_san,dict_san=list_generator('optimized_oqmd_pbe_hse_features.csv','correct_formula',['a','bg_pbe','bg_hse'])
df_alex,dict_alex=list_generator('nominal_summary.csv','compound',['lattice_const','PBE_bg','HSE06_bg'])

lst_final=[]
for compounds in df_alex.compound.unique().tolist():
    if compounds in df_san.correct_formula.unique().tolist():
        a_san=dict_san[0][str(compounds)];pbe_bg_san=dict_san[1][str(compounds)];hse_bg_san=dict_san[2][str(compounds)]
        a_alex=dict_alex[0][str(compounds)];pbe_bg_alex=dict_alex[1][str(compounds)];hse_bg_alex=dict_alex[2][str(compounds)]
        lst_final.append([compounds,a_san,a_alex,pbe_bg_san,pbe_bg_alex,hse_bg_san,hse_bg_alex])
heading=['compound','lattice','lattice_zun','PBE_bg','PBE_bg_zunger','HSE06_bg','HSE06_bg_zunger']
df_final=pd.DataFrame(lst_final,columns=heading)
df_final.to_csv('zunger_lattice_bandgap_calculations.csv')
