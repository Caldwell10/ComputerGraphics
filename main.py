import pandas as pd
from functions import generate_email

#load the Excel file
file_a_df =pd.read_excel('/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/data/TestFiles.xlsx',sheet_name='File_A')
file_b_df =pd.read_excel('/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/data/TestFiles.xlsx',sheet_name='File_B')

# generate file containing each name and their corresponding email
def process_file(df):
     df['Email Address'] = df['Student Name'].apply(generate_email)
     return  print(df[['Student Name','Email Address']])

#print file A
print("Processing file_A")
process_file(file_a_df)

#print file B
print("Processing file_B")
process_file(file_b_df)


