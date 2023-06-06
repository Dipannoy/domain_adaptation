import pandas as pd
import csv

# df = pd.read_csv('summary_bvm_calculations.csv')
# df2 = pd.read_csv('combined_features_1143_dataset.csv')
df = pd.read_csv('addtional_400.csv')

# print(df)

tr_list = []
index = 0
for i in df.index:
    tr=[]
    tr.append(df['correct_formula'][i]+'.cif')
    tr.append(index)
    tr.append(df['hf_opt'][i])
    # formla = df['correct_formula'][i]
    # val = df2[df2['correct_formula'] == formla]['pbe_bg'].values
    # print(val)
    # if(len(val)>0):
    #     tr.append(val[0])

    #     index = index+1
    #     tr_list.append(tr)
    index = index+1
    tr_list.append(tr)

header = ['file_name','index', 'label']

with open('targets_test.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(header) 

    write.writerows(tr_list) 