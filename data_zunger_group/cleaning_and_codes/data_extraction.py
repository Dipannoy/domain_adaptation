import pandas as pd
import numpy as np
import os,sys

import os,sys

from pymatgen.io.vasp import Poscar


def cif_generator(file_input,file_output):
    poscar = Poscar.from_file(file_input)
    structure = poscar.structure
    structure.to(filename=str(file_output)+".cif")

cwd=os.getcwd()

def list_display(csv_file):
    """
    ## Parameters
    csv_file: path of the csv file

    ## Returns
    df: dataframe
    list_cmpd: a list of chemical formula (with index 'compound' in the csv file) 
    """
    df=pd.read_csv(csv_file)
    list_cmpd=df.compound.unique().tolist()
    return df,list_cmpd

def remove_file_extension(lst_in):
    """
    ## Parameters
    lst_in: A list of files with extension (.*)
   
    ## Returns
    lst_out: The list by removing the extension

    """
    lst_out=[]
    for entries in lst_in:
        formula=entries.split('.')[0]
        lst_out.append(formula)
    return lst_out


def list_entry_cleaner(list_in,position):
    """
    To given list this method trims each section of string separated by '_' and only returns the part at the given position. eg. good_bad_ugly if position is 1, it just returns 'bad'
    ## Parameters
    list_in: Input list #type(list)
    position: position #type(int)

    ## Returns
    list_out: output list #type(lst)
    """
    list_out=[]
    for entries in list_in:
        ent=entries.split('_')[int(position)]
        list_out.append(ent)
    return list_out

def common_in_lists(lst1, lst2):
    list_common= list(set(lst1).intersection(lst2))
    list_uncommon=list(set(lst1)^set(lst2))
    return list_common,list_uncommon
    #return list(set(lst1) & set(lst2))

orig_csv_file='bg_summary_orig.csv'
df,compounds_shared=list_display('bg_summary_orig.csv')
print(len(compounds_shared))

polymorphous_list=os.listdir(cwd+'/poscar_all_poly/')
polymorphous_compounds=list_entry_cleaner(remove_file_extension(polymorphous_list),1)
#print(polymorphous_list)
#print(polymorphous_compounds)

no_cif_list=os.listdir(cwd+'/poscar_nominal_pm3m/no_cif/')
no_cif_compounds=list_entry_cleaner(remove_file_extension(no_cif_list),1)
#print(no_cif_compounds)


suxuen_not_used_list=os.listdir(cwd+'/poscar_nominal_pm3m/suxuen_not_used/')
suxuen_not_used_compounds=list_entry_cleaner(remove_file_extension(suxuen_not_used_list),2)
#print(suxuen_not_used_compounds)

suxuen_used_list=os.listdir(cwd+'/poscar_nominal_pm3m/suxuen_used/')
suxuen_used_compounds=list_entry_cleaner(remove_file_extension(suxuen_used_list),1)
#print(suxuen_used_compounds)

#list_common=common_in_lists(suxuen_used_compounds,suxuen_not_used_compounds)
#list_common=common_in_lists(suxuen_not_used_compounds,no_cif_compounds)
list_common,list_uncommon=common_in_lists(suxuen_used_compounds,no_cif_compounds)
#print(len(list_common),list_common,len(list_uncommon),list_uncommon)

lst_nominal=[];lst_poly=[];count_poly=0;count_nominal=0;count_both=0
df,compounds_shared=list_display(orig_csv_file)
dict_lat=pd.Series(df.a.values,index=df['compound']).to_dict()
dict_nominal_pbe=pd.Series(df.nominal_PBE_bg.values,index=df['compound']).to_dict()
dict_nominal_hse=pd.Series(df.nominal_HSE06_bg.values,index=df['compound']).to_dict()
dict_poly_pbe=pd.Series(df.polymorphous_PBE_bg.values,index=df['compound']).to_dict()
dict_poly_hse=pd.Series(df.polymorphous_HSE06_bg.values,index=df['compound']).to_dict()


for i in range(len(polymorphous_compounds)):
    compound=polymorphous_compounds[i];path_compound=cwd+'/poscar_all_poly/'
    if compound in compounds_shared:
        lst_poly.append([compound,dict_lat[str(compound)],dict_poly_pbe[str(compound)],dict_poly_hse[str(compound)]])
        cif_generator(path_compound+polymorphous_list[i],path_compound+compound)
    else:
        pass
heading_poly=['compound','lattice_const','PBE_bg','HSE06_bg']
df_poly=pd.DataFrame(lst_poly,columns=heading_poly)
df_poly.to_csv('polymorphous_summary.csv')

dict_nominal={}
lst1=no_cif_compounds;lst2=no_cif_list;path1=cwd+'/poscar_nominal_pm3m/no_cif/'
for i in range(len(lst1)):
    compound=lst1[i];path_compound=path1
    if compound in compounds_shared:
        if compound not in list(dict_nominal.keys()):
             lst_nominal.append([compound,dict_lat[str(compound)],dict_nominal_pbe[str(compound)],dict_nominal_hse[str(compound)]])
             cif_generator(path_compound+lst2[i],path_compound+compound)
             dict_nominal[str(compound)]=1
        else:
            pass

lst1=suxuen_used_compounds;lst2=suxuen_used_list;path1=cwd+'/poscar_nominal_pm3m/suxuen_used/'
for i in range(len(lst1)):
    compound=lst1[i];path_compound=path1
    if compound in compounds_shared:
        if compound not in list(dict_nominal.keys()):
             lst_nominal.append([compound,dict_lat[str(compound)],dict_nominal_pbe[str(compound)],dict_nominal_hse[str(compound)]])
             cif_generator(path_compound+lst2[i],path_compound+compound)
             dict_nominal[str(compound)]=1
        else:
            pass


lst1=suxuen_not_used_compounds;lst2=suxuen_not_used_list;path1=cwd+'/poscar_nominal_pm3m/suxuen_not_used/'
for i in range(len(lst1)):
    compound=lst1[i];path_compound=path1
    if compound in compounds_shared:
        if compound not in list(dict_nominal.keys()):
             lst_nominal.append([compound,dict_lat[str(compound)],dict_nominal_pbe[str(compound)],dict_nominal_hse[str(compound)]])
             cif_generator(path_compound+lst2[i],path_compound+compound)
             dict_nominal[str(compound)]=1
        else:
            pass

heading_nominal=['compound','lattice_const','PBE_bg','HSE06_bg']
df_single=pd.DataFrame(lst_nominal,columns=heading_nominal)
df_single.to_csv('nominal_summary.csv')
print(df_single.shape)
#print(count_poly,count_nominal)

    
