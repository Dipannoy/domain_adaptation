
#####################################################################################################
CONTENTS OF THE FOLDER
####################################################################################################
This folder contains following subfolders and files

Folder1: cleaning_and_codes  ==> This folder contains data provided by the Zunger group and
                                 codes that generate csv and cif files

Folder 2: nominal_cifs ==> This folder contains all the cif files of the nominal pm3m compound
                           available to us from Zunger group (235 in total)

Folder 3: poly_cifs ==> This folder contains all the cif files of the polymorphous compounds
                           available to us from Zunger group (226 in total)

File 1: nominal_summary.csv ==> This csv file contains name of compound (compound) optimized lattice 
                                constant (lattice_const) Band gap computed using PBE (PBE_bg) and
                                band gap computed using HSE06 (HSE06_bg) for all nominal structures

File 2: poly_summary.csv ==> This csv file contains name of compound (compound) optimized lattice 
                             constant (lattice_const) Band gap computed using PBE (PBE_bg) and
                             band gap computed using HSE06 (HSE06_bg) for all polymorphous structures
     
File 3: Zunger_lattice_bandgap_calculations.csv ==> This folder contains the comparision between lattice
                                         constants and band gap computed from us vs the ones obtained from
                                         Zunger group for compounds that were common (142)
#######################################################################################################
TASK
########################################################################################################

Step 1: Load the saved Schnet model that was trained earlier for predicting PBE band gaps of OQMD compounds.

Step 2: Read the csv file "poly_summary.csv" (File 2) 

Step 3: Use the column 'compound' in the csv file "poly_summary.csv" to predict the band gap.
        The corresponding cif files could be found in the folder 'poly_cifs' (Folder 2). 
        For example, for a compound AgGeCl3 in "poly_summary.csv" the corresponding cif file is found
        in the folder poly_cifs with the name AgGeCl3.cif.
        [Our expectation is that the predicted band gap is close to 'PBE_bg' (target property)]

#####################################################################################################
CONTENTS OF THE FOLDER
####################################################################################################
This folder contains following subfolders and files

Folder1: cleaning_and_codes  ==> This folder contains data provided by the Zunger group and
                                 codes that generate csv and cif files

Folder 2: nominal_cifs ==> This folder contains all the cif files of the nominal pm3m compound
                           available to us from Zunger group (235 in total)

Folder 3: poly_cifs ==> This folder contains all the cif files of the polymorphous compounds
                           available to us from Zunger group (226 in total)

File 1: nominal_summary.csv ==> This csv file contains name of compound (compound) optimized lattice 
                                constant (lattice_const) Band gap computed using PBE (PBE_bg) and
                                band gap computed using HSE06 (HSE06_bg) for all nominal structures

File 2: poly_summary.csv ==> This csv file contains name of compound (compound) optimized lattice 
                             constant (lattice_const) Band gap computed using PBE (PBE_bg) and
                             band gap computed using HSE06 (HSE06_bg) for all polymorphous structures
     
File 3: Zunger_lattice_bandgap_calculations.csv ==> This folder contains the comparision between lattice
                                         constants and band gap computed from us vs the ones obtained from
                                         Zunger group for compounds that were common (142)
#######################################################################################################
TASK
########################################################################################################

Step 1: Load the saved Schnet model that was trained earlier for predicting PBE band gaps of OQMD compounds.

Step 2: Read the csv file "poly_summary.csv" (File 2) 

Step 3: Use the column 'compound' in the csv file "poly_summary.csv" to predict the band gap.
        The corresponding cif files could be found in the folder 'poly_cifs' (Folder 2). 
        For example, for a compound AgGeCl3 in "poly_summary.csv" the corresponding cif file is found
        in the folder poly_cifs with the name AgGeCl3.cif.
        [Our expectation is that the predicted band gap is close to 'PBE_bg' (target property)]


