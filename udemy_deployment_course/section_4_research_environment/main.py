import os
import sys
import filecmp

from src import helper

if __name__ == '__main__':

    # get root and data directory of project
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(ROOT_DIR, "data")
    output_dir = os.path.join(ROOT_DIR, "outputs")

    # list of structure types
    STRUCTURE_TYPES = ["forest_fire", "ic_dag", "pref_attach", "small_world", "waxman"]
    # list of implementation
    IMPLEMENTATIONS = ["benchmark", "pybnutil"]
    # always use trial [FIXED_TRIAL] for comparison between BayNet vs pybnutil
    FIXED_TRIAL = 1

    '''Check whether the synthetic data generation pipeline is reproducible'''

    # redirect stdout to a text file
    orig_stdout = sys.stdout
    f = open(os.path.join(output_dir, 'syn_1_reproducibility_checks.txt'), 'w')
    sys.stdout = f

    for imp in IMPLEMENTATIONS:
        for st in STRUCTURE_TYPES:
            print(f'--------{imp}-{st}: reproducibility checks for data and DAGs-------- \n')

            # get the pathnames for the two directories that we are comparing
            comp_dirs = [helper.get_syn_data_pathnames(data_dir, t, imp, st, "syn_data") for t in [1, 2]]
            # recursively compare each folder in the directory
            filecmp.dircmp(comp_dirs[0], comp_dirs[1]).report_full_closure()

            # Read modelstring from the two trials and then compare them using bnlearn, print summary of comparision
            samples = ['0', '1', '2']
            for s in samples:
                _= helper.BNcompare(sample=s,
                                 syn_data_path=comp_dirs)

            print(f'\n--------{imp}-{st}: reproducibility checks structural learning outputs --------\n')

            # get the pathnames for the two directories that we are comparing
            comp_dirs = [helper.get_syn_data_pathnames(data_dir, t, imp, st, "results") for t in [1, 2]]
            # recursively compare each folder in the directory
            filecmp.dircmp(comp_dirs[0], comp_dirs[1]).report_partial_closure()

            print('\n\n\n\n\n\n')
        print('\n\n\n\n\n\n\n')

    sys.stdout = orig_stdout
    f.close()

    '''Compare outputs of the structural generation pipeline using BayNet vs using pybnutil
    
    - Compare the generated data and results (including performance metrics) between the synthetic 
      data generation pipeline from intervene using Baynet vs using pybnutil
    - I will always use "trial 1" for comparision between Baynet vs pybnutil
    - Within trial 1, there are three samples (0,1,2) generated using random seeds (0,1,2). 
      I will compare the data and results of BayNet sample 0, with pybnutil sample 0, ..., 
      BayNet sample 2 with pybnutil sample 2    
    '''

    # redirect stdout to a text file
    orig_stdout = sys.stdout
    f = open(os.path.join(output_dir, 'syn_1_imp_comparison_checks.txt'), 'w')
    sys.stdout = f

    for st in STRUCTURE_TYPES:

        print(f'-------{st}: comparison of data and DAGs between benchmark and pybnutil--------\n')
        # get directories for comparison
        comp_dirs = [helper.get_syn_data_pathnames(data_dir, FIXED_TRIAL, imp, st, "syn_data") for imp in
                     IMPLEMENTATIONS]
        # recursively compare each folder in the directory
        filecmp.dircmp(comp_dirs[0], comp_dirs[1]).report_full_closure()

        # compare DAGs
        samples = ['0', '1', '2']
        for s in samples:
            _=helper.BNcompare(sample=s,
                             syn_data_path=comp_dirs)

        print(f'\n----{st}: comparison of structural learning outputs between benchmark and pybnutil ----\n')

        # get the pathnames for the two directories that we are comparing
        comp_dirs = [helper.get_syn_data_pathnames(data_dir, FIXED_TRIAL, imp, st, "results") for imp in
                     IMPLEMENTATIONS]
        # recursively compare each folder in the directory
        filecmp.dircmp(comp_dirs[0], comp_dirs[1]).report_full_closure()

    sys.stdout = orig_stdout
    f.close()
