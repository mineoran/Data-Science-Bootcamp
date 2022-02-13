import csv
import json
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class DataOperations():

    def check_format(self, filedata):

        if (filedata == json):
            df = pd.read_json(filedata, encoding="UTF-8")
            return df
        elif ValueError:
            df = pd.read_csv(filedata)
            print(df.head(5))
            return df
        else:
            (filedata == pd.DataFrame)
            df = pd.DataFrame(filedata, index=True)
            print(df)
            return df

    def check_set(self,_):
        if (_ == ""):
            data = np.random.rand(3, 3)
            df = pd.DataFrame(
                data,  columns=['Column_A', 'Column_B', 'Column_C'])
            print(df)
        else:
            print("Not true")

    def des(self, df):  # checking for description max and min
        des = df.describe()
        return des

    def null_values(self, df):  # checking for null values
        return df.isnull().sum().sort_values(ascending=False)

    def corr(self, df):  # checking the correlation of dataset
        return df.corr()

    def datavisual(self, df):
        sns.barplot(data=df, x="Domestic Sales (in $)", y="Title")
        plt.title("The top 4 best highest grossing movies of all time")
        print("******")
        chart = df.boxplot()
        chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
        plt.ylabel('Count', fontsize=12)
        plt.show()


do = DataOperations()
df = do.check_format('HolywoodMovies.csv')
# do.check_set(df)
des=do.des(df)
print(des)
nulValues=do.null_values(df)
print(nulValues)
corr=do.corr(df)
print(corr)
# do.datavisual(df)












































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



