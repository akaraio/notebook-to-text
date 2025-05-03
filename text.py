import json
import os
import glob

dirx = []

for root, dirs, files in os.walk("data"):
        for file in files:
            if '.venv' not in root:
                if file.endswith(".ipynb"):
                    dirx.append(root + '\\' + file)

print(len(dirx))

for dir in dirx:
    with open(dir, 'r', encoding="utf8") as file:
        doc = json.load(file)

        for i in range(len(doc['cells'])):
            with open('data' + '_'.join(dir.split('\\')[2:]).replace('.ipynb', '') + '.txt', 'a', encoding="utf8") as f:
                for line in doc['cells'][i]['source']:
                    f.write(line)

print(len(glob.glob('data')))