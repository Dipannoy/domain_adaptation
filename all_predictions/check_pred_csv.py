import pandas as pd
import csv
from sklearn.metrics import mean_absolute_error as mae

df = pd.read_csv('./schnet/prediction_noda_schnet_dblbvm_200_hfopt0.053.csv')

target = df['target']
y = df['prediction']
y_arr = []
for i in y:
  i = str(i)
  y_mod=i.replace("[","")
  y_mod=y_mod.replace("]","")
#   print(y_mod)
  y_arr.append(float(y_mod))
print(mae(target, y_arr))