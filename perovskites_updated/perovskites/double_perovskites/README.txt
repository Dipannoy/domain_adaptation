#########################################################################################################

contents

#########################################################################################################
Folders

F1. bvm        : It contains cif files for 745 strcutures from OQMD that excludes lanthanides and actinides, Hg and Tl
F2. optimized  : It consists of the DFT optimized bvm geometries (using the PBE functional)



columns of CSV file meaning:
       "correct_formula" : the ABX3 formula
        "lat_bvm" : lattice constant from BVM, 
        "lat_opt" : lattice constant from DFT, 
        "A": Element at A site,
        "A'": Element at A' site,
        "B": Element at B site,
        "B'": Element at B' site,
        "X": Element at X site,
        "hf_opt": formation energy for DFT geometry, 
         "bvm_oqmd_lat_err": is the percentage error in lattice constant computed as 100*(a_BVM-a_DFT)/a_DFT. 

CSV files:
C1. reliable_training.csv: This contains the information of formation energy and lattice constant from DFT calculations for BVM and DFT optimized
              geometry where the absolute error in BVM lattice constant (wrt DFT optimized) is less than or equal to 5 percent. (651 compounds)

C2. moderate_reliable_training.csv: This contains the information of formation energy and lattice constant from DFT calculations for BVM and DFT optimized
              geometry where the absolute error in BVM lattice constant (wrt DFT optimized) is in between 5 and 10 percent. (89 compounds)

C3. unreliable_training.csv: This contains the information of formation energy and lattice constant from DFT calculations for BVM and DFT optimized
              geometry where the absolute error in BVM lattice constant (wrt DFT optimized) is greater than 10 percent. (5 compounds)

C4: summary_bvm_calculations.csv: This file contains all the above information combined. C1, C2 and C3 are subsets of C4.

Jupyter notebook
J1. double_perovskites_030123.ipynb : Jupyter notebook to generate figures and partition the dataframes


Task:
(a) Use the converged model that was trained for predicting the hf_opt of single_ABX3 perovskites. (trained using reliable+unreliable+moderate bvm structures)
    to predict hf_opt of these double perovskites. The label of the structures found in the folder bvm could be read from the file summary_bvm_calculations.csv.
    In most of the cases, the structures have lattice constant closer to DFT optimized, we probably don't need to create a left-out set by mixing reliable
    unreliable and moderate.

(b) If task (a) has test set accuracy of < 0.1 eV/atom, this will be a good news. 

(c) For next task, we will use strutures from bvm to retrain the model to predict hf_opt.

                           


