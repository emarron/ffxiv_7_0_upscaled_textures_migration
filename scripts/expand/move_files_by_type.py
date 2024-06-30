import os
import shutil
from pathlib import Path

def move_files_by_type(source_dir):
    source_dir = Path(source_dir)
    d_dir = source_dir.parent / (source_dir.name + '_d')
    n_dir = source_dir.parent / (source_dir.name + '_n')

    # Create destination directories if they don't exist
    d_dir.mkdir(exist_ok=True)
    n_dir.mkdir(exist_ok=True)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith('d.dds'):
                move_file(root, file, d_dir)
            elif file.lower().endswith('n.dds'):
                move_file(root, file, n_dir)

def move_file(root, file, dest_dir):
    source_path = Path(root) / file
    relative_path = source_path.relative_to(source_dir)
    dest_path = dest_dir / relative_path

    # Create subdirectories in the destination if they don't exist
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Move the file
    shutil.move(str(source_path), str(dest_path))
    print(f"Moved: {relative_path} to {dest_path}")

if __name__ == "__main__":
    source_dir = "minor_change_format"
    move_files_by_type(source_dir)
    print("Process completed.")