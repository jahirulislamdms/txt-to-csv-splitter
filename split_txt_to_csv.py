import os
import csv

def split_txt_to_csv(file_path, max_lines):
    if not os.path.exists(file_path):
        print("File not found!")
        return
    
    folder = os.path.dirname(file_path)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    total_files = (len(lines) + max_lines - 1) // max_lines  # Calculate number of CSVs needed
    
    for i in range(total_files):
        start = i * max_lines
        end = start + max_lines
        chunk = lines[start:end]
        
        csv_file_path = os.path.join(folder, f"{base_name}_part{i+1}.csv")
        
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            for line in chunk:
                writer.writerow([line.strip()])
        
        print(f"Created: {csv_file_path}")

if __name__ == "__main__":
    txt_file = input("Enter the path of the .txt file: ")
    max_lines = int(input("Enter max lines per CSV file: "))
    split_txt_to_csv(txt_file, max_lines)
