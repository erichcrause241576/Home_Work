import os

standart = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in standart.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)
