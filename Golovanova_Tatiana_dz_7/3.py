import shutil
import os.path


PROJECT_DIR = 'my_project'
TEMPLATE_DIR = 'templates'
TEMPLATE_PATH = os.path.join(PROJECT_DIR, TEMPLATE_DIR)
HTML_EXTENSION = '.html'

os.makedirs(TEMPLATE_PATH, exist_ok=True)
for root, dirs, files in os.walk(PROJECT_DIR):
    if TEMPLATE_DIR in root and TEMPLATE_PATH not in root:
        basename = os.path.basename(root)
        for file in files:
            if HTML_EXTENSION in file:
                dst_dir = os.path.join(TEMPLATE_PATH, basename)
                os.makedirs(dst_dir, exist_ok=True)
                shutil.copy2(
                    os.path.join(root, file),
                    dst_dir
                )
