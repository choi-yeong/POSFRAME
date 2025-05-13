import os
import shutil

source_root = 'KolektorSDD'         # 50개 폴더가 있는 상위 폴더
target_folder = 'surfaceDataset'         # 합쳐진 이미지 폴더

os.makedirs(target_folder, exist_ok=True)
existing_names = set()

count = 1
for root, dirs, files in os.walk(source_root):
    for file in files:
        if file.lower().endswith(('.jpg', '.bmp')):
            original_path = os.path.join(root, file)
            
            # 중복 방지용 이름 재조정
            name, ext = os.path.splitext(file)
            folder_name = os.path.basename(root)
            new_name = f"{folder_name}_{name}{ext}"
            while new_name in existing_names:
                new_name = f"{name}_{count:03d}{ext}"
                count += 1

            existing_names.add(new_name)
            target_path = os.path.join(target_folder, new_name)
            shutil.copy2(original_path, target_path)

print("모든 이미지가 중복 없이 병합되었습니다.")
