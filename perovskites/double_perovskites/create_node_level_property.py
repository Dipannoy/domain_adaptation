import pandas as pd
import csv
import json

# df = pd.read_csv('summary_bvm_calculations.csv')
# df2 = pd.read_csv('combined_features_1143_dataset.csv')
# df = pd.read_csv('combined_features_1143_dataset.csv')
# json_obj = {}
# json_list = {}
# for i in range(0,1143):
#     json_obj[str(df['correct_formula'][i])] = df['pbe_bg'][i]
# # json_obj[df['correct_formula']] = df['pbe_bg']
#     # json_obj["pbe_bg"] = df['pbe_bg'][i]
#     # json_list.append(json_obj)
# # df['Compound'][i]
#     #  = {"compound":str(df[i]['correct_formula']), "pbe_bg":df[i]['pbe_bg']}
#     # json_list.append(json_obj)

# # print(len(json_obj))

# with open("property_pbe_bg.json", "w") as outfile:
#     json.dump(json_obj, outfile)


f2 = open('/home/chris/Desktop/gnn_model/gcnn_keras/notebooks/perovskites/double_perovskites/property_pbe_bg.json')
bg_data = json.load(f2)

for d in bg_data:
    print(bg_data[str(d)])








