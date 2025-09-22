import pandas as pd
import numpy as np
import random
import string
import datetime
import csv

int_col = np.random.randint(0, 10000, 10000)

# generate a list of random string

def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

string_col = [random_string(10) for i in range(100000)]

# generate a list of random dates
start = datetime.datetime.strptime("01-01-2000", "%d-%m-%Y")
end =  datetime.datetime.strptime("01-01-2023", "%d-%m-%Y")
date_col = [start + datetime.timedelta(days=random.randint(0, (end-start).days))for i in range(100000)]

# generate a dateframe from the list of data
df = pd.DataFrame({'integer_coliumn': int_col, 'string_column': string_col, 'date_column': date_col})
df.to_csv('dataframe.csv', index=False)
df.to_parquet('dataframe.parquet', index=False)
df.to_csv('dataframe.tsv', sep='\t', index=False)