#########################################################################################################

contents

#########################################################################################################
Folders

F1. bvm        : It contains cif files for 761 strcutures from OQMD that excludes lanthanides and actinides
F2. optimized  : It consists of the DFT optimized bvm geometries (using the PBE functional)



columns of CSV file meaning:
       "correct_formula" : the ABX3 formula
        "lat_bvm" : lattice constant from BVM, 
        "lat_opt" : lattice constant from DFT, 
        "hf_bvm": formation energy for BVM geometry, 
        "hf_opt": formation energy for DFT geometry, 
         "bvm_oqmd_lat_err": is the percentage error in lattice constant computed as 100*(a_BVM-a_DFT)/a_DFT. 

CSV files:
C1. reliable_training.csv: This contains the information of formation energy and lattice constant from DFT calculations for BVM and DFT optimized
              geometry where the absolute error in BVM lattice constant (wrt DFT optimized) is less than or equal to 5 percent. (499 compounds)

C2. moderate_reliable_training.csv: This contains the information of formation energy and lattice constant from DFT calculations for BVM and DFT optimized
              geometry where the absolute error in BVM lattice constant (wrt DFT optimized) is in between 5 and 10 percent. (102 compounds)

C3. unreliable_training.csv: This contains the information of formation energy and lattice constant from DFT calculations for BVM and DFT optimized
              geometry where the absolute error in BVM lattice constant (wrt DFT optimized) is greater than 10 percent. (159 compounds)


Task:
(a) Reserve any random 50 compounds from each of the above 3 CSV files ( total 150 compounds) as a left out set. For task below we
     will use the remaining compounds in CSV files C1, C2 and C3.

(b) Train the model using remaining (449 compounds) in CSV file 1. (using 90/5/5 or any desired split) and evaluate the model performance 
    on the left out set
(c) Use the remaining compounds in CSV file C1 and C2 (449+52=501) for model training and evaluate the performance on the left out set
(d) Use the remaining compounds in CSV file C1, C2 and C3 (449+52+109=610) for model training and evaluate the performance on the left out set.

The labels for structures could be read from the column 'correct_formula' in the csv files. BVM structures and DFT optimized structure with the same
name could be found in the folder bvm and optimized (F1 and F2 above), respectively.

*** Date: Feb 22, 2023: 
As a first step, we will use strcuture from folder bvm (F1) and our target is 'hf_opt' (formation energy from DFT optimized calculations)

                           


