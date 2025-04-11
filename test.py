import pandas as pd
from datetime import datetime


def get_age(birthday):
    today = datetime.now()
    if today.month <= birthday.month and today.day < birthday.day:
        return today.year - birthday.year - 1
    else:
        return today.year - birthday.year


df = pd.read_csv("data/raw/test.csv")

df["age"] = df.apply(lambda x: get_age(pd.to_datetime(x['col_c'])), axis=1)

df.to_csv("data/processed/est_01.csv")
