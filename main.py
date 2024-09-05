import pandas as pd
import logging
import os

from ComputerGraphics.functions import log_student_count
from functions import generate_email
from constraints import handle_special_characters

#logging
logging.basicConfig(filename='process.log', level=logging.INFO, format='%(asctime)s - %(message)s')



#load the Excel file
file_a_df =pd.read_excel('/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/data/TestFiles.xlsx',sheet_name='File_A')
file_b_df =pd.read_excel('/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/data/TestFiles.xlsx',sheet_name='File_B')

# generate file containing each name and their corresponding email
def process_file(df):
     #Apply the special character handler if needed
     df['Clean_Student_Name']=df['Student Name'].apply(handle_special_characters)

     #generate email address
     df['Email Address'] = df['Student Name'].apply(generate_email)

     return  print(df[['Student Name','Email Address']])

#print file A
print("Processing file_A")
process_file(file_a_df)

#print file B
print("Processing file_B")
process_file(file_b_df)

#Log the count of male and female students based on the Gender column
male_count=file_a_df[file_a_df['Gender'] == 'Male'].shape[0]+ file_b_df[file_b_df['Gender'] == 'Male'].shape[0]
female_count=file_a_df[file_a_df['Gender'] == 'Female'].shape[0]+file_b_df[file_b_df['Gender'] == 'Female'].shape[0]

#pass both the male count and female count as parameters on the logging function
log_student_count(male_count,female_count)

#save processed DataFrame as CSV,TSV, and JSON
def save_processed_data(df, filename_prefix):
     output_folder = '/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/'

     try:
          # Save as CSV
          csv_file = os.path.join(output_folder, f'{filename_prefix}.csv')
          df.to_csv(csv_file, index=False)
          print(f"CSV file saved: {csv_file}")
     except Exception as e:
          print(f"Failed to save CSV: {e}")

     try:
          # Save as TSV
          tsv_file = os.path.join(output_folder, f'{filename_prefix}.tsv')
          df.to_csv(tsv_file, sep='\t', index=False)
          print(f"TSV file saved: {tsv_file}")
     except Exception as e:
          print(f"Failed to save TSV: {e}")

     try:
          # Save as JSON
          json_file = os.path.join(output_folder, f'{filename_prefix}.json')
          df.to_json(json_file, orient='records')
          print(f"JSON file saved: {json_file}")
     except Exception as e:
          print(f"Failed to save JSON: {e}")


# Saving processed data for File A and File B
save_processed_data(file_a_df, 'Processed_File_A')
save_processed_data(file_b_df, 'Processed_File_B')