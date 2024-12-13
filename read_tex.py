import os
from core import run


folder_path = "./input"
# txt 파일만 필터링
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

for file_name in txt_files:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        name = file_name.split('.')[0]
        texts = {'KR':content}
        run(texts, name)


