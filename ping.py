import re
import pandas as pd

def process_ping_data(input_txt_path, output_excel_path):
    with open(input_txt_path, 'r') as f:
        data = f.read()
        
    time_values = re.findall(r'time=(\d+)ms', data)
    time_values = list(map(int, time_values))
    
    df = pd.DataFrame({'Time(ms)': time_values})
    df.to_excel(output_excel_path, index=False)

input_file = input('Input file name: ')
input_txt_path = f"{input_file}.txt"

output_file = input('Output file name: ')
output_excel_path = f"{output_file}.xlsx"

# Process the data and save to Excel
process_ping_data(input_txt_path, output_excel_path)
