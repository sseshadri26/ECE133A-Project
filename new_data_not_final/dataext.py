import pandas as pd
import time

# Replace 'filename.csv' with the name of your file
df = pd.read_csv('to_mod.csv')

# Convert start and end times to Unix time
df.iloc[:, 1] = pd.to_datetime(df.iloc[:, 1], format='%Y-%m-%d %H:%M:%S').dt.tz_localize('UTC').dt.tz_convert('America/Los_Angeles').apply(lambda x: int(time.mktime(x.timetuple())))

df.iloc[:, 2] = pd.to_datetime(df.iloc[:, 2], format='%Y-%m-%d %H:%M:%S').dt.tz_localize('UTC').dt.tz_convert('America/Los_Angeles').apply(lambda x: int(time.mktime(x.timetuple())))

df.insert(4, 'duration', df.iloc[:, 2] - df.iloc[:, 1])


# Add column for start time of the day in seconds after midnight
df.insert(2, 'Seconds Since Start Of Day', df.iloc[:, 1] % 86400)

# Add column for number of days since January 1st, 1970
day_num = pd.to_datetime(df.iloc[:, 1], unit='s').dt.dayofyear - 1

# Insert day number as a new column
df.insert(1, 'Day Number', day_num)



# Save the updated file
# Replace 'new_filename.csv' with the name you want to give to the updated file
df.to_csv('modded.csv', index=False)