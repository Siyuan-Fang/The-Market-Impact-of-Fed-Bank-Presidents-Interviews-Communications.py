import os
import pandas as pd

def merge_xlsx_files(folder_path, output_file):
    # Create a Pandas Excel writer using openpyxl as the engine
    writer = pd.ExcelWriter(output_file, engine='openpyxl')

    for filename in os.listdir(folder_path):
        if filename.endswith(".xlsx"):
            print(filename)

    # Save the writer and close

# Example usage
folder_path = 'D:/AA econ/research track/data/Youtube CNBC Fed1'
output_file = 'D:/AA econ/research track/data/Youtube CNBC Fed.xlsx'
merge_xlsx_files(folder_path, output_file)