import os
from collections import defaultdict
import django
root_dir = r'C:\code\PythonBasics\venv\Lib\site-packages\django'
sizes = [100, 1000, 10000, 100000]
django_files = defaultdict(int)
for root, dirs, files in os.walk(root_dir):

    for file in files:
        a = 0
        for i in sizes:
            if a <= os.stat(os.path.join(root, file)).st_size <= i:
                django_files[i] += 1
                a = i

print(sorted(django_files.items()))

