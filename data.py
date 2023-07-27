import os
import zipfile

zip_filename = os.path.join(os.getcwd(),'data', 'archive.zip')
print(zip_filename)
file_storage= os.path.join(os.getcwd(),'data')
print(file_storage)

def extract_data(source, destination):
    with zipfile.ZipFile(source, 'r') as zip_ref:
        zip_ref.extractall(path=destination)

extract_data(zip_filename,file_storage)