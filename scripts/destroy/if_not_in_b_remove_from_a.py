import os
from pathlib import Path

def remove_non_matching_files(output_dir, source_dir):
    output_dir = Path(output_dir)
    source_dir = Path(source_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            source_file = Path(root) / file
            relative_path = source_file.relative_to(source_dir)
            output_file = output_dir / relative_path

            if not output_file.exists():
                try:
                    source_file.unlink()
                    print(f"Removed: {source_file}")
                except Exception as e:
                    print(f"Error removing {source_file}: {e}")

if __name__ == "__main__":
    output_directory = "7-0_id_G"
    source_directory = "7-0_id_R"

    remove_non_matching_files(output_directory, source_directory)
    print("Process completed.")
