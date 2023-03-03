import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('final_data_crashes_final.csv')

# Replace the values in column 32
# df['Sunrise_Sunset'] = df['Sunrise_Sunset'].replace({'Night': 0, 'Day': 1})
# df['Civil_Twilight'] = df['Civil_Twilight'].replace({'Night': 0, 'Day': 1})
# df['Nautical_Twilight'] = df['Nautical_Twilight'].replace({'Night': 0, 'Day': 1})
# df['Astronomical_Twilight'] = df['Astronomical_Twilight'].replace({'Night': 0, 'Day': 1})

# ss=['Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop']
# for s in ss:
#     df[s] = df[s].replace({False: 0, True: 1})

df['Side'] = df['Side'].replace({'L': 0, 'R': 1})

# dir_dict = {'N': [0, 1],
#             'North': [0, 1],
#             'NNE': [0.38, 0.92],
#             'NE': [0.71, 0.71],
#             'ENE': [0.92, 0.38],
#             'E': [1, 0],
#             'East': [1, 0],
#             'ESE': [0.92, -0.38],
#             'SE': [0.71, -0.71],
#             'SSE': [0.38, -0.92],
#             'S': [0, -1],
#             'South': [0, -1],
#             'SSW': [-0.38, -0.92],
#             'SW': [-0.71, -0.71],
#             'WSW': [-0.92, -0.38],
#             'W': [-1, 0],
#             'West': [-1, 0],
#             'WNW': [-0.92, 0.38],
#             'NW': [-0.71, 0.71],
#             'NNW': [-0.38, 0.92],
#             'Calm': [0, 0],
#             'CALM': [0, 0],
#             'VAR': '',
#             'Variable': ''}


# df['Wind_Direction'] = df['Wind_Direction'].replace({'False': 0, 'True': 1})
# df[['Wind x', 'Wind y']] = df['Wind_Direction'].apply(lambda x: pd.Series(dir_dict[x]))
# df.dropna(inplace=True)

# df[['Wind x', 'Wind y']] = df[['Wind x', 'Wind y']].mul(df['Wind_Speed(mph)'].astype(float), axis=0)

# df['Weather Condition'] = df['Weather_Condition']



# unique_values = df[:, 32].unique()

for col in df.iloc[:, 8:9]:
    unique_values = df[col].unique()
    print(f"Unique values in {col}:")
    for value in unique_values:
        count = df[col].value_counts()[value]
        print(f"{value} ({count} times)")



# col_18_counts = df['Weather_Condition'].value_counts()
# valid_col_18 = col_18_counts[col_18_counts >= 250].index
# df = df[df['Weather_Condition'].isin(valid_col_18)]


# Print the unique values
# print(unique_values)
# print(unique_values18)

# Write the updated DataFrame back to the CSV file

# one-hot encode the "Category" column
# one_hot = pd.get_dummies(df['State'])

# # add the one-hot encoded columns to the original DataFrame
# df = pd.concat([df, one_hot], axis=1)

# # drop the original "Category" column
# df = df.drop('State', axis=1)


df.to_csv('final_data_crashes_final_final.csv', index=False)