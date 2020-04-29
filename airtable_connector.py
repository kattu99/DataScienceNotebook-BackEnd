from airtable import Airtable
import pandas as pd
import numpy as np
import json
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def connect_to_db(key, tablename, api_key, columns, row_conditions): 
    airtable = Airtable(key, tablename, api_key = api_key)
    record_list = airtable.get_all(fields=columns, maxRecords=500)
    df = pd.DataFrame([record['fields'] for record in record_list])
    for row in row_conditions:
        df = df.loc[df[row] == row_conditions[row]]
    df = df[columns]
    return df

selected_columns = ['longitude', 'latitude', 'housing_median_age','total_rooms', 'median_house_value' ]
table = connect_to_db('appwenHop5nM0Kr57', 'HousingDataset', api_key = 'keyqXIq4dGINpcj0h',columns=selected_columns, row_conditions={})
processed = process_data(table, 'group_by','housing_median_age', None)
regressor = train_regression(table, selected_columns[:4], selected_columns[4])
vals = np.array([-117.13, 32.74, 50.0, 1527.0]).reshape(1, -1)
print(predict_values(regressor, vals)[0])