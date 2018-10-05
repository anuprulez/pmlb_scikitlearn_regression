'''
Penn State Machine Learning Benchmark Regression Datasets
'''

import sys
import time
import pandas as pd
from sklearn import linear_model
from matplotlib import pyplot as plt


class Regression_Analysis:

    def __init__(self, files_list):
        """ Init method. """
        self.files_list = files_list

    def read_files(self, file_name):
        """
        Read the data files and return data and targets
        """
        #file_name = str = unicode(file_name, errors='replace')
        file_name = "data/" + str(file_name)
        print(file_name)
        data_file = pd.read_csv(file_name, encoding="")
        print(data_file)
        return data_file
       
    def analyze_dataset(self):
        """
        Read the data files and return data and targets
        """
        for file_item in self.files_list:
           data = self.read_files(file_item)
           print(data)


if __name__ == "__main__":

    if len(sys.argv) != 1:
        print( "Usage: analyze_regression_datasets.py" )
        exit( 1 )
    start_time = time.time()
    files_list = ["192_vineyard.tsv"]
    analysis = Regression_Analysis(files_list)
    analysis.analyze_dataset()
    end_time = time.time()
    print ("Program finished in %s seconds" % str( end_time - start_time ))
