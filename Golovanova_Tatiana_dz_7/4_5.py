import os.path


PATH = '/tmp'
SIZES = {}


def upper_bound(size):
    rank = 1
    while True:
        size //= 10
        if size == 0:
            break
        rank += 1

    return 10 ** rank


for root, dirs, files in os.walk(PATH):
    for file in files:
        file_path = os.path.join(root, file)
        _, ext = os.path.splitext(file)
        bound = upper_bound(os.stat(file_path, follow_symlinks=False).st_size)

        count, exts = SIZES.setdefault(bound, (0, []))
        if ext and ext not in exts:
            exts.append(ext)
        SIZES[bound] = (count + 1, exts)

print(SIZES)
