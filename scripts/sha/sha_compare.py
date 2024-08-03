import csv
from pathlib import Path

def load_hashes_from_csv(csv_file):
    hashes = {}
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            file_path, file_hash = row
            hashes[file_path] = file_hash
    return hashes

def compare_hashes(current_csv, previous_csv):
    current_hashes = load_hashes_from_csv(current_csv)
    previous_hashes = load_hashes_from_csv(previous_csv)
    
    updated_files = []
    new_files = []
    unchanged_files = []
    
    for file_path, current_hash in current_hashes.items():
        if file_path in previous_hashes:
            if current_hash != previous_hashes[file_path]:
                updated_files.append(file_path)
            else:
                unchanged_files.append(file_path)
        else:
            new_files.append(file_path)
    
    return updated_files, new_files, unchanged_files

# Example usage
current_csv = 'file_hashes_current.csv'
previous_csv = 'file_hashes_previous.csv'

updated_files, new_files, unchanged_files = compare_hashes(current_csv, previous_csv)

# Output results
print("Updated Files:", updated_files)
print("New Files:", new_files)
print("Unchanged Files:", unchanged_files)
