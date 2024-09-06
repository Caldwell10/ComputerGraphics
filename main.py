import pandas as pd
import logging
import os
from functions import generate_email, log_student_count
from constraints import handle_special_characters

log_file_path = '/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/process.log'

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

# Load the Excel files
file_a_df = pd.read_excel('/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/data/TestFiles.xlsx', sheet_name='File_A')
file_b_df = pd.read_excel('/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/data/TestFiles.xlsx', sheet_name='File_B')

# Normalize gender values to lowercase
file_a_df['Gender'] = file_a_df['Gender'].str.lower()
file_b_df['Gender'] = file_b_df['Gender'].str.lower()

#Mapping abbreviations
gender_mapping = {
    'm': 'male',
    'f': 'female',
    'male': 'male',
    'female': 'female'
}
file_a_df['Gender'] = file_a_df['Gender'].map(gender_mapping)
file_b_df['Gender'] = file_b_df['Gender'].map(gender_mapping)

# Process files and generate emails
def process_file(df):
    # Detect special characters and log names with special characters
    special_character_count = 0
    df['Contains Special Characters'] = df['Student Name'].apply(handle_special_characters)
    for index, row in df.iterrows():
        if row['Contains Special Characters']:
            logging.warning(f"Name contains special characters: {row['Student Name']}")
            special_character_count += 1

        # Log the total number of students with special characters
    logging.info(f"Total students with special characters: {special_character_count}")

    special_char_names = df[df['Contains Special Characters'] == True]['Student Name'].tolist()
    for name in special_char_names:
        logging.warning(f"Name contains special characters: {name}")

    # Generate email addresses
    df['Email Address'] = df['Student Name'].apply(generate_email)
    return df[['Student Name', 'Email Address','Gender']]

# Processing File A
logging.info("Processing file_A")
file_a_df_processed = process_file(file_a_df)
logging.info("Finished processing file_A")

# Processing File B
logging.info("Processing file_B")
file_b_df_processed = process_file(file_b_df)
logging.info("Finished processing file_B")

# Count male and female students after normalizing the Gender column
if 'Gender' in file_a_df.columns and 'Gender' in file_b_df.columns:
    male_count = file_a_df[file_a_df['Gender'] == 'male'].shape[0] + file_b_df[file_b_df['Gender'] == 'male'].shape[0]
    female_count = file_a_df[file_a_df['Gender'] == 'female'].shape[0] + file_b_df[file_b_df['Gender'] == 'female'].shape[0]
    log_student_count(male_count, female_count)

# Save processed data as CSV, TSV, and JSON
def save_processed_data(df, filename_prefix):
    output_folder = '/Users/caldwellwachira/PycharmProjects/codeLabs_1/ComputerGraphics/'

    try:
        csv_file = os.path.join(output_folder, f'{filename_prefix}.csv')
        df.to_csv(csv_file, index=False)
        logging.info(f"CSV file saved: {csv_file}")
    except Exception as e:
        logging.error(f"Failed to save CSV: {e}")

    try:
        tsv_file = os.path.join(output_folder, f'{filename_prefix}.tsv')
        df.to_csv(tsv_file, sep='\t', index=False)
        logging.info(f"TSV file saved: {tsv_file}")
    except Exception as e:
        logging.error(f"Failed to save TSV: {e}")

    try:
        json_file = os.path.join(output_folder, f'{filename_prefix}.json')
        df.to_json(json_file, orient='records')
        logging.info(f"JSON file saved: {json_file}")
    except Exception as e:
        logging.error(f"Failed to save JSON: {e}")

# Function to save gender-based lists of students


# Save data for File A and File B
save_processed_data(file_a_df_processed, 'Processed_File_A')
save_processed_data(file_b_df_processed, 'Processed_File_B')

def save_gender_based_lists(df, filename_prefix):
    # Filter male students
    male_students = df[df['Gender'] == 'male']
    if not male_students.empty:
        logging.info(f"Saving male students list: {filename_prefix}_Male_Students")
        save_processed_data(male_students, f"{filename_prefix}_Male_Students")
    else:
        logging.info("No male students found.")

    # Filter female students
    female_students = df[df['Gender'] == 'female']
    if not female_students.empty:
        logging.info(f"Saving female students list: {filename_prefix}_Female_Students")
        save_processed_data(female_students, f"{filename_prefix}_Female_Students")
    else:
        logging.info("No female students found.")

# Save separate lists for male and female students
save_gender_based_lists(file_a_df_processed, 'Processed_File_A')
save_gender_based_lists(file_b_df_processed, 'Processed_File_B')