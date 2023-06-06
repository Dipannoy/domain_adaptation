import pandas as pd
import csv

df = pd.read_csv('reliable_training.csv')
df2 = pd.read_csv('moderate_reliable_training.csv')
df3 = pd.read_csv('unreliable_training.csv')

# print(df)

tr_list = []
index = 0
# for i in df.index:
#     tr=[]
#     tr.append(df['correct_formula'][i]+'.cif')
#     tr.append(index)
#     # tr.append(df['hf_opt'][i])
#     tr.append(df['hf_opt'][i])

#     index = index+1
#     tr_list.append(tr)

# for i in df2.index:
#     tr=[]
#     tr.append(df2['correct_formula'][i]+'.cif')
#     tr.append(index)
#     # tr.append(df['hf_opt'][i])
#     tr.append(df2['hf_opt'][i])

#     index = index+1
#     tr_list.append(tr)

# for i in df3.index:
#     tr=[]
#     tr.append(df3['correct_formula'][i]+'.cif')
#     tr.append(index)
#     # tr.append(df['hf_opt'][i])
#     tr.append(df3['hf_opt'][i])

#     index = index+1
#     tr_list.append(tr)
    

# header = ['file_name','index', 'label']

# with open('targets.csv', 'w') as f: 
#     write = csv.writer(f) 
#     write.writerow(header) 

#     write.writerows(tr_list) 

# df_target = pd.read_csv('targets.csv')

# df_shuffle = df_target.sample(frac=1)

df_shuffle = pd.read_csv('overall_predictions.csv')

for i in df_shuffle.index:
    tr=[]
    tr.append(df_shuffle['correct_formula'][i]+'.cif')
    tr.append(index)
    # tr.append(df['hf_opt'][i])
    tr.append(df_shuffle['pbe_bg'][i])

    index = index+1
    tr_list.append(tr)
    

header = ['file_name','index', 'label']

with open('targets_bg.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(header) 

    write.writerows(tr_list) 
    
    
    
import pandas as pd
import csv

# df = pd.read_csv('summary_bvm_calculations.csv')
# df2 = pd.read_csv('combined_features_1143_dataset.csv')
df = pd.read_csv('targets_745.csv')
df = df.sample(n=200)

# print(df)

tr_list = []
index = 0
for i in df.index:
    tr=[]
    tr.append(df['file_name'][i])
    tr.append(index)
    tr.append(df['label'][i])
    # formla = df['correct_formula'][i]
    # val = df2[df2['correct_formula'] == formla]['pbe_bg'].values
    # print(val)
    # if(len(val)>0):
    #     tr.append(val[0])

    #     index = index+1``
    #     tr_list.append(tr)
    index = index+1
    tr_list.append(tr)

header = ['file_name','index', 'label']

with open('targets_200.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(header) 

    write.writerows(tr_list) 



