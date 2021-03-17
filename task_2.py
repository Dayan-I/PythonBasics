import os

with open('config.yaml') as f:
    dirs = [line.replace('\n', '').replace(':', '') for line in f]
    for line in dirs:
        if line[0].isalpha():
            os.mkdir(str(line))
        elif line.startswith(' ') and line[2].isalpha():
            if '.py' in line: pass
            else:
                path = os.path.join(str(dirs[0]), str(line[2:]))
                os.makedirs(path)
                a = line[2:]
        elif line.startswith(' ') and line[4] == '-':
            if '.py' in line:
                save_path = os.getcwd() + '//' + str(path)
                py_file = os.path.join(save_path, str(line[5:]))
                file_1 = open(py_file, 'w')
                file_1.close()
            else:
                path = os.path.join(str(dirs[0]), str(a), str(line[5:]))
                os.makedirs(path)
                b = line[5:]
        elif line.startswith(' ') and line[8] == '-':
            path = os.path.join(str(dirs[0]), str(a), str(b), str(line[9:]))
            os.makedirs(path)
        elif line.startswith(' ') and line[12] == '-':
            save_path = os.getcwd() + '//' + str(path)
            py_file = os.path.join(save_path, str(line[13:]))
            file_1 = open(py_file, 'w')
            file_1.close()

