import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('final_data_crashes.csv')


# Add a new column 'hour' to the dataframe, which is the hour of the day
df['Hour'] = (df['Seconds Since Start Of Day'] // 3600).astype(int)

# One-hot encode the 'hour' column and add it to the dataframe as 24 new columns
hour_one_hot = pd.get_dummies(df['Hour'], prefix='Hour')
df = pd.concat([df, hour_one_hot], axis=1)

# Add a new column 'amount of light' to the dataframe
def map_amount_of_light(hour):
    if hour <= 11:
        return hour
    elif hour == 12:
        return 12
    else:
        return 24 - hour

df['Amount of Light'] = df['Hour'].apply(map_amount_of_light)

# Write the updated dataframe back to a CSV file

df.to_csv('final_data_crashes_final_final.csv', index=False)