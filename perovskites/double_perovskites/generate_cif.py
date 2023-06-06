import json
from pymatgen.core.structure import Structure
import csv

def get_data(filename):
    with open(filename,'r') as f:
        data = json.load(f)
    return data

def write_data(write_file, write_dict):
    with open(write_file,'w') as f:
        json.dump(write_dict,f)
     
data_dict = get_data('bvm_cubic_structs_051823.json')
header = ['file_name','index', 'label']

index = 0
tr_list=[]
for cmpd in data_dict.keys():
    # structure = Structure.from_dict(data_dict[cmpd]['bvm_structure'])
    file_name = cmpd+'.cif'
    # structure.to(filename="bvm_cubic_cifs/"+file_name)
    tr=[]
    tr.append(file_name)
    tr.append(index)
    tr.append(0)
    tr_list.append(tr)
    index=index+1
    # break

with open('targets_bvm_cubic.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(header) 

    write.writerows(tr_list) 