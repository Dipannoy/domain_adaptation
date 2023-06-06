import pandas as pd
import csv

# df = pd.read_csv('summary_bvm_calculations.csv')
df = pd.read_csv('combined_features_1143_dataset.csv')
df2 =  pd.read_csv('targets_943.csv')
# df = pd.read_csv('targets_745.csv')
# df = df2.sample(n=943)

# # print(df)

tr_list = []
index = 0
# for i in df.index:
#     tr=[]
#     tr.append(df['correct_formula'][i]+'.cif')
#     tr.append(index)
#     tr.append(df['hf_opt'][i])
#     # formla = df['correct_formula'][i]
#     # val = df2[df2['correct_formula'] == formla]['pbe_bg'].values
#     # print(val)
#     # if(len(val)>0):
#     #     tr.append(val[0])

#     #     index = index+1``
#     #     tr_list.append(tr)
#     index = index+1
#     tr_list.append(tr)

header = ['file_name','index', 'label']

# with open('targets_943.csv', 'w') as f: 
#     write = csv.writer(f) 
#     write.writerow(header) 

#     write.writerows(tr_list) 

c = 0
for i in df.index:
    tr=[]
    # tr.append(df['correct_formula'][i]+'.cif')
    # tr.append(index)
    # tr.append(df['hf_opt'][i])
    formla = df['correct_formula'][i]+'.cif'
    val = df2[df2['file_name'] == formla]['label'].values
    # print(val)
    if(len(val)==0):
    #     tr.append(val[0])
    # else:
        tr.append(df['correct_formula'][i]+'.cif')
        tr.append(index)
        tr.append(df['hf_opt'][i])
        tr_list.append(tr)

    #     index = index+1``
    #     tr_list.append(tr)
    index = index+1
    # tr_list.append(tr)

with open('targets_test_200.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(header) 

    write.writerows(tr_list) 


    