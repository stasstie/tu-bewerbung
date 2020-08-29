import pandas as pd
import zipfile as zf
import os
class Dslcc_to_pytorch:
    def __init__(self):
        self.__df = pd.DataFrame
        self.__dict_df = {}

    def open_data(self, dir: str)-> dict:
        df1 = pd.DataFrame
        list_files = os.listdir(dir)
        for item in list_files:
            if item == "DSL-TEST-GOLD.txt" or item == "DSL-TRAIN.txt":
                with open(os.path.join(dir, item), "r", encoding='utf-8') as myfile:
                    self.__dict_df[item] = pd.read_csv(myfile,sep='\t', header=None)
                    self.__dict_df[item].set_index(1)
        return self.__dict_df

    def transform_data(self, dict_df: dict) -> dict:
        for key in dict_df:
            df = dict_df[key]
            df1 = df.loc[(df[1] == 'fr-CA') | (df[1] == 'fr-FR')].copy()
            df1.loc[(df1[1] == 'fr-CA').values, 1] = "1"
            df1.loc[(df1[1] == 'fr-FR').values, 1] = "2"
            df1 = df1[[1,0]]
            dict_df[key] = df1
        return dict_df

    def write_data(self, dict_df):
        dir_name = './.data/dslcc4_csv/'
        try:
            # Create target Directory
            os.mkdir(dir_name)
            print("Directory ", dir_name, " Created ")
        except FileExistsError:
            print("Directory ", dir_name, " already exists")

        for key in dict_df:
            dict_df[key].to_csv(os.path.join(dir_name, key), header=None, index=None)











