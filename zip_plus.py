#! python3
# zip_plus.py

import sys
import zipfile

def unzip(filename):
    zip_name = zipfile.ZipFile(filename)
    zip_name.extractall()

unzip(sys.argv[1])