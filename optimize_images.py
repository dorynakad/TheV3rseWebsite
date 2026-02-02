from PIL import Image
import os
import shutil

source_dir = "glitchcut_000"
backup_dir = "glitchcut_000_backup"

# Create backup
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    print(f"Created backup directory: {backup_dir}")

files = [f for f in os.listdir(source_dir) if f.lower().endswith('.jpg')]
print(f"Found {len(files)} images.")

for filename in files:
    src_path = os.path.join(source_dir, filename)
    backup_path = os.path.join(backup_dir, filename)
    
    # Backup if not exists
    if not os.path.exists(backup_path):
        shutil.copy2(src_path, backup_path)
    
    # Process
    try:
        with Image.open(src_path) as img:
            # Calculate new height to maintain aspect ratio
            target_width = 960
            w_percent = (target_width / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            
            # Resize
            img_resized = img.resize((target_width, h_size), Image.Resampling.LANCZOS)
            
            # Save overwrite
            img_resized.save(src_path, "JPEG", quality=60, optimize=True)
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("Optimization complete.")
