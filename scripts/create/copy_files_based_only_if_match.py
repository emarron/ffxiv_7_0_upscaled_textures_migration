from pathlib import Path
import shutil

def sort_files(source_dir):
    source_dir = Path(source_dir)
    
    # Create destination directories if they don't exist
    for folder in ['stuff-mask', 'stuff-norm', 'stuff-base']:
        (source_dir / folder).mkdir(parents=True, exist_ok=True)

    for file_path in source_dir.rglob('*'):
        if file_path.suffix.lower() in ('.dds', '.tga'):
            if '_mask' in file_path.stem:
                dest_folder = 'stuff-mask'
            elif '_norm' in file_path.stem:
                dest_folder = 'stuff-norm'
            elif '_base' in file_path.stem:
                dest_folder = 'stuff-base'
            else:
                continue  # Skip files that don't match any criteria
            
            relative_path = file_path.relative_to(source_dir)
            dest_path = source_dir / dest_folder / relative_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            shutil.copy2(file_path, dest_path)
            print(f"Copied {file_path} to {dest_path}")

# Usage
source_directory = Path('stuff')
sort_files(source_directory)