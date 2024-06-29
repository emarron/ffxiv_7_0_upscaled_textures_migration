import csv
import shutil
from pathlib import Path

def process_csv_and_copy_files(csv_file, new_directory):
    new_directory = Path(new_directory)
    new_directory.mkdir(parents=True, exist_ok=True)

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        groups = {}

        for row in reader:
            group_id = int(row['Group ID'])
            filename = row['Filename']
            folder = row['Folder']
            file_path = Path(folder) / filename

            if group_id not in groups:
                groups[group_id] = []

            groups[group_id].append(file_path)

        for group_id, files in groups.items():
            if len(files) > 1:
                source_file = files[0]

                for target_file in files[1:]:
                    target_file_path = new_directory / target_file.relative_to(Path(target_file).anchor)
                    target_file_path.parent.mkdir(parents=True, exist_ok=True)

                    # Copy and rename the file
                    try:
                        shutil.copy2(source_file, target_file_path)
                        print(f"Copied {source_file} to {target_file_path}")
                    except Exception as e:
                        print(f"Failed to copy {source_file} to {target_file_path}: {e}")

if __name__ == "__main__":
    csv_file = 'documentation/csv_comparisons/similarity_check_on_PNGS/goodnews_converted_further.csv'
    new_directory = 'new_directory'

    process_csv_and_copy_files(csv_file, new_directory)

    print("Processing completed.")
