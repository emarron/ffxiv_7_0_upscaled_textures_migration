import os
import json
import shutil
from pathlib import Path

def load_materials(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def normalize_path(path):
    return path.replace('\\', '/').replace('.tga', '.tex')

def find_material_entry(materials, texture_path):
    normalized_texture_path = normalize_path(texture_path)
    for entry in materials:
        if any(normalize_path(tex) == normalized_texture_path for tex in entry['textures']):
            return entry
    return None

def process_textures(bc7_output_dir, materials_json, output_dir):
    materials = load_materials(materials_json)
    
    for root, _, files in os.walk(bc7_output_dir):
        for file in files:
            if file.endswith('.tga'):
                tga_path = os.path.join(root, file)
                relative_path = os.path.relpath(tga_path, bc7_output_dir)
                
                material_entry = find_material_entry(materials, relative_path)
                
                if material_entry:
                    shpk = material_entry['shpk']
                    output_path = os.path.join(output_dir, shpk, relative_path)
                    
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    shutil.copy2(tga_path, output_path)
                    print(f"Copied {tga_path} to {output_path}")
                else:
                    print(f"No material entry found for {relative_path}")
                    
if __name__ == "__main__":
    bc7_output_dir = "bc7_output"
    materials_json = "materials.json"
    output_dir = "output"
    
    process_textures(bc7_output_dir, materials_json, output_dir)