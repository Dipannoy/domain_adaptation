import pandas as pd
import numpy as np
import os,sys

cwd=os.getcwd()

def list_display(csv_file):
    """
    ## Parameters
    csv_file: path of the csv file

    ## Returns
    list_cmpd: a list of chemical formula (with index 'correct_formula' in the csv file) 
    """
    df=pd.read_csv(csv_file)
    list_cmpd=df.correct_formula.unique().tolist()
    return list_cmpd

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

def is_element(string,element_list):
    """
    A function to return True(False) if the element exist(doesn't exit) in the string 
    ## Paramters
    string: word or string (type str)
    element_list: list of letter/word/string (type str)

    ## Returns
    True/False (type boolean)

    """
    for entry in element_list:
        if entry in string:
            return True
    return False



lst_oqmd_only=list_display('only_oqmd_not_bvm.csv')
common_lst=list_display('common_in_bvm_oqmd.csv')

all_bvm_lst=remove_file_extension(os.listdir(cwd+'/814_bvm_cubic_cif/'))

def ml_predictions(csv_file):
    df=pd.read_csv(csv_file)
    dict_ml=pd.Series(df.prediction.values,index=df['ids']).to_dict()
    return dict_ml


def return_list(main_list,exclude_formula,exclude_elements,dict_ml):
    """
    A function that returns a list that is not contained in given exclude list and in addition doesn't contain certain list of elements
    ## Parameters
    main_list: list of formulas 
    exclude_formula: list of forumulas that are to be excluded from main_list
    exclude_elements: list of elements that should be excluded

    ## Returns:
    list_out: list of formulas that do not contain the restrictions applied using exclude_formula and exclude_elements
    """
    lst_out=[]
    for entries in main_list:
        if entries not in exclude_formula:
            if is_element(entries,exclude_elements) is False:
                ml_pred=dict_ml[str(entries)]
                lst_out.append([entries,ml_pred])
    return lst_out


#print(all_bvm_lst)
#print(remove_file_extension(all_bvm_lst))
dict_ml=ml_predictions(cwd+'/schnet/result/unseen/814_bvm_cubic_prediction_job_predicted_outputs.csv')
heading=['correct_formula','ML_prediction']
final_list=return_list(all_bvm_lst,common_lst+lst_oqmd_only,['Hg','Tl'],dict_ml)
df_out=pd.DataFrame(final_list,columns=heading)
df_out.to_csv('list_bvm_no_Tl_no_Hg.csv')

