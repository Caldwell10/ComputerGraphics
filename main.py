import pandas as pd

#load the Excel file
file_a_df =pd.read_excel('/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/data/TestFiles.xlsx',sheet_name='File_A')
file_b_df =pd.read_excel('/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/data/TestFiles.xlsx',sheet_name='File_B')

# generate email
def process_file(df):
     return  print(df[['Student Name','Email Address']])

print("Processing file_A")
process_file(file_a_df)

print("Processing file_B")
process_file(file_b_df)


