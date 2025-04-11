import pandas, datetime
dataframe =pandas.read_csv("test.csv")
dataframe["age"]=dataframe.apply(lambda x: datetime.datetime.now().year - pandas.to_datetime(x['col_c']).year - 1 if datetime.datetime.now().month <= pandas.to_datetime(x['col_c']).month and datetime.datetime.now().day < pandas.to_datetime(x['col_c']).day else datetime.datetime.now().year - pandas.to_datetime(x['col_c']).year, axis=1)  
dataframe.to_csv("testfinal.csv")