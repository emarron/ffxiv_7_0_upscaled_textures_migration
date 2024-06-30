import os
from pathlib import Path

def remove_matching_files(output_dir, source_dir):
    output_dir = Path(output_dir)
    source_dir = Path(source_dir)

    for root, _, files in os.walk(output_dir):
        for file in files:
            output_file = Path(root) / file
            relative_path = output_file.relative_to(output_dir)
            source_file = source_dir / relative_path

            if source_file.exists():
                try:
                    source_file.unlink()
                    print(f"Removed: {source_file}")
                except Exception as e:
                    print(f"Error removing {source_file}: {e}")

if __name__ == "__main__":
    output_directory = "7-0_output"
    source_directory = "minor_changes"

    remove_matching_files(output_directory, source_directory)
    print("Process completed.")