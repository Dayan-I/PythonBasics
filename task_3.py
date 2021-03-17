import os
import shutil
root_dir = r'C:\code\PythonBasics\my_project'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if '.html' in file:
            path = os.path.join(root, file).split(os.sep)

            try:
                path = os.path.join(root_dir, 'templates', path[4])
                os.makedirs(path)
            except FileExistsError:
                print('Something wrong')
            finally:
                shutil.copy(os.path.join(root, file), path)








