import pandas as pd

# Replace 'filename.csv' with the name of your file
df = pd.read_csv('US_Accidents_Dec21_updated.csv')

df.iloc[:, 17:19] = df.iloc[:, 17:19].fillna(0)
df['Wind_Chill(F)'] = df['Wind_Chill(F)'].fillna(df['Temperature(F)'])

# Drop any rows that have missing data in any column
df.dropna(inplace=True)




# Save the new file with the cleaned data
# Replace 'new_filename.csv' with the name you want to give to the cleaned file
df.to_csv('new_filename.csv', index=False)

