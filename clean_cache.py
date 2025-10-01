import os, shutil

for root, dirs, files in os.walk("."):
    if "__pycache__" in dirs:
        print("Cleaning", os.path.join(root, "__pycache__"))
        shutil.rmtree(os.path.join(root, "__pycache__"))