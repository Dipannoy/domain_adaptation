import os
import csv
import pandas as pd
 
# Get the list of all files and directories
path = "/home/chris/Desktop/gnn_model/gcnn_keras/notebooks/perovskites/double_perovskites/all_other_bvm_cifs"
dir_list = os.listdir(path)
 
# print("Files and directories in '", path, "' :")
 
# prints all files
# print(len(dir_list))

df = pd.read_csv('targets_bg_test.csv')

tr_list = []
index = 0
for i in df.index:
    tr=[]
    try:
        

        # val = dir_list.index(df['file_name'][i])

        # print(val)

        tr.append(df['file_name'][i].split('.')[0])
        tr_list.append(tr)

        # tr.append(i.split('.')[0])
        # tr.append(index)
        # tr.append(0)
        # formla = df['correct_formula'][i]
        # val = df2[df2['correct_formula'] == formla]['pbe_bg'].values
        # print(val)
        # if(len(val)>0):
        #     tr.append(val[0])

        #     index = index+1
        #     tr_list.append(tr)
        index = index+1
        # tr_list.append(tr)
    except:
        tr.append(df['file_name'][i])
        tr_list.append(tr)

# header = ['file_name','index', 'label']

with open('dp_400_addtional.csv', 'w') as f: 
    write = csv.writer(f) 
    # write.writerow(header) 

    write.writerows(tr_list) 