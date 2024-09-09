import os
import pandas as pd
from openpyxl import load_workbook


# Define the folders
UPLOAD_FOLDER = 'uploads'
EXPORT_FOLDER = 'exports'


# Function to calculate all the values in the Excel file and export as CSV
def process_excel_file(filename):
    # Define the file paths
    input_file_path = os.path.join(UPLOAD_FOLDER, filename)
    output_file_path = os.path.join(EXPORT_FOLDER, f'{os.path.splitext(filename)[0]}.csv')

    # Step 1: Load the workbook using openpyxl
    workbook = load_workbook(input_file_path, data_only=True)  # data_only=True reads the calculated values
    sheet = workbook.active  # You can specify the sheet by name if needed

    # Step 2: Extract all the data from the sheet
    data = sheet.values  # This generator gives each row as a tuple of values

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame as CSV
    df.to_csv(output_file_path, index=False, header=False)

    return output_file_path  # Return the path of the exported CSV

