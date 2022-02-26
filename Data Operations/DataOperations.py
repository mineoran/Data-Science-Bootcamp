#Required Python Packages;
import csv
import json
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class DataOperations():
    
    """
       The Data Operations class contains functions 
       that are created to analyze and export data in different formats to dataframes.
       
    """  
    
    def __init__(self,data = None):
     #  """ *args: assign different types of dataset. """
        self.data = data        
        

    def check_format(self):
        """Determines whether the data entered in the 
           check_format function is in json, csv or numpy array format. """
        
        if isinstance(self.data,np.ndarray):
            self.df = pd.DataFrame(self.data)
            return self.df
        
        elif isinstance(self.data,pd.DataFrame):
            self.df = self.data
            return self.df
        
        elif type(self.data) == type(None):
            random_numpy = {"A" : np.random.randn(20),
                            "B" : np.random.randn(20),
                            "C" : np.random.randn(20)}
            
            self.df = pd.DataFrame(data = random_numpy , columns = random_numpy.keys())
            return self.df
        else:
            
            path = self.data.split(sep = ".")
            filetype = path[-1]
            if filetype == "csv":
                self.df = pd.read_csv(self.data)
                return self.df
            elif filetype == "json":
                self.df = pd.read_json(self.data)
                return self.df
            else:
                print("Unknown data type")

    def des(self):  
        """to check the statistical analysis of the data"""
        data = self.check_format()
        return data.describe()


    def datavisualize(self):
        """Prints histogram and boxplot for two random numerical columns of the given dataframe."""
        sns.barplot(data=self.check_format(), x="Domestic Sales (in $)", y="Title") #HolywoodMovies.csv
        plt.title("The top 4 best highest grossing movies of all time")
        print("******")
        chart = self.check_format().boxplot()
        chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
        plt.ylabel('Count', fontsize=12)
        plt.show()











































# import csv
# import json
# import numpy as np
# from numpy import random
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# class DataOperations():
#     def check_format(self, filedata):

#         if (filedata == json):
#             df = pd.read_json(filedata, encoding="UTF-8")
#             return df
#         elif ValueError:
#             df = pd.read_csv(filedata)
#             print(df.head(5))
#             return df
#         else:
#             (filedata == pd.DataFrame)
#             df = pd.DataFrame(filedata, index =True)
#             print(df)  
#     def check_set(self,_ ):
#         if (_ == ""):
#             data = np.random.rand(3, 3)
#             df = pd.DataFrame(data,  columns = ['Column_A','Column_B','Column_C'])
#             print(df)
#         else:
#             print("Not true")

# class DataAnalysis(DataOperations):
#     def info(self, df): # checking for info dataset
#         info = df.info()
#         return info
#     def des(self, df): # checking for description max and min 
#         des = df.describe()
#         return des
#     def null_values(self,df): # checking for null values
#         return df.isnull().sum().sort_values(ascending=False)
#     def corr(self,df): # checking the correlation of dataset
#         return df.corr()


# class DataVisualization(DataOperations):
#     def datavisual(self,df):
#         sns.barplot(data= df, x="Domestic Sales (in $)", y="Title")
#         plt.title("The top 4 best highest grossing movies of all time")
#         print("**********************************************")
#         chart = df.boxplot()
#         chart.set_xticklabels(chart.get_xticklabels(), rotation = 45)
#         plt.ylabel('Count', fontsize = 12)
#         plt.show()



