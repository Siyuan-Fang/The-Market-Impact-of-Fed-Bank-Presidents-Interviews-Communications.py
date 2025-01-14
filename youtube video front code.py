import os
import pandas as pd

def merge_xlsx_files(folder_path, output_file):
    # Create a Pandas Excel writer using openpyxl as the engine
    writer = pd.ExcelWriter(output_file, engine='openpyxl')

    for filename in os.listdir(folder_path):
        if filename.endswith(".xlsx"):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)

            # Load the Excel file into a DataFrame
            df = pd.read_excel(file_path)

            # Use the filename without extension as sheet name
            sheet_name = os.path.splitext(filename)[0]

            # Write the DataFrame to a new sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Save the writer and close
    writer.save()

# Example usage
folder_path = 'D:/AA econ/research track/data/Youtube CNBC Fed1'
output_file = 'D:/AA econ/research track/data/Youtube CNBC Fed.xlsx'
merge_xlsx_files(folder_path, output_file)