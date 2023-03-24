import csv
import random

# Open the original CSV file
with open('modded111.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Initialize empty lists for each label
    label1_rows = []
    label2_rows = []
    label3_rows = []
    label4_rows = []
    
    # Read the header row from the original CSV file
    header_row = next(csv_reader)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        
        # Check the label of the row
        label = int(row[0])
        
        # Add the row to the appropriate label list
        if label == 1:
            label1_rows.append(row)
        elif label == 2:
            label2_rows.append(row)
        elif label == 3:
            label3_rows.append(row)
        elif label == 4:
            label4_rows.append(row)
    
    # Randomly select 250 rows from each label
    label1_sample = random.sample(label1_rows, 12500)
    label2_sample = random.sample(label2_rows, 12500)
    label3_sample = random.sample(label3_rows, 12500)
    label4_sample = random.sample(label4_rows, 12500)
    
    # Combine the samples into one list
    final_sample = label1_sample + label2_sample + label3_sample + label4_sample
    
    # Shuffle the final sample
    random.shuffle(final_sample)
    
    # Open a new CSV file to write the final sample to
    with open('final_data_crashes_medium_even.csv', 'w', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        
        # Write the header row
        csv_writer.writerow(header_row)
        
        # Write each row from the final sample to the new CSV file
        for row in final_sample:
            csv_writer.writerow(row)