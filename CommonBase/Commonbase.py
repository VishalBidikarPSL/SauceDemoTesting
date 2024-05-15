import configparser

import pandas as pd


class Commonbase:

    def __init__(self):
        self.driver = None
        self.filepath = None
        self.sheet_name = None

    def read_excel(self):
        df = None
        config = configparser.ConfigParser()
        config.read('..\\CommonBase\\config.properties')
        self.filepath = config.get('TEST', 'excel')
        self.sheet_name = config.get('TEST', 'sheet')

        try:
            df = pd.read_excel('..\\CommonBase\\' + self.filepath, self.sheet_name)
            df = df.fillna("")
        except Exception as e:
            print(e)

        return df

