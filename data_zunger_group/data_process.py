import pandas as pd
import csv

# df = pd.read_csv('summary_bvm_calculations.csv')
# df2 = pd.read_csv('combined_features_1143_dataset.csv')
df = pd.read_csv('nominal_summary.csv')

# print(df)

tr_list = []
index = 0
for i in df.index:
    tr=[]
    tr.append(df['compound'][i]+'.cif')
    tr.append(index)
    tr.append(df['PBE_bg'][i])
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

with open('targets_nominal.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(header) 

    write.writerows(tr_list) 
    
    
       <a href="https://docs.google.com/document/d/1PxPtNu-tVXi-froQWcGFXxjqiEVhT8ChxZYgj76cJ_Q/edit?usp=sharing">Poster Session 1</a>
         <a href="https://docs.google.com/document/d/1v731aj99UMGMdCxaIhlsnC1TH8cFgS0_gwJynFRZGAk/edit?usp=sharing">Poster Session 2</a>

