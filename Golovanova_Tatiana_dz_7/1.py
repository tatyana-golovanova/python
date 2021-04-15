import os.path


DIR_TREE = {
    'my_project': ['settings', 'mainapp', 'adminapp', 'authapp'],
}


for rootdir, subdirs in DIR_TREE.items():
    if not os.path.exists(rootdir):
        os.mkdir(rootdir)
    for subdir in subdirs:
        subdir_path = os.path.join(rootdir, subdir)
        try:
            os.mkdir(subdir_path)
        except FileExistsError:
            print(f'{subdir_path} уже существует')
