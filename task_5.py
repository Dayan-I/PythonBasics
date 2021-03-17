import os
from collections import defaultdict
import django
root_dir = r'C:\code\PythonBasics\venv\Lib\site-packages\django'
sizes = [100, 1000, 10000, 100000]
django_files = defaultdict(tuple)
new_list = []

for root, dirs, files in os.walk(root_dir):
    for i in sizes:

        a = 0
        b = 0
        for file in files:

            if a <= os.stat(os.path.join(root, file)).st_size <= i:
                b += 1
                print(b)
                for symb in file:
                    if symb == '.':
                        c = file.index(symb)

                if file[c:] not in new_list:
                    new_list.append(file[c:])
                value = (b, new_list)
                django_files[i] = value
                a = i
print(sorted(django_files.items()))