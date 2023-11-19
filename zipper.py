import os
import zipfile

paths = os.listdir(".")


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))


for path in paths:
    if path.startswith("Assignment") and not path.endswith(".zip"):
        with zipfile.ZipFile("zips/" + path + ".zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipdir(path, zipf)
