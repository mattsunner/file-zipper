import os
from zipfile import ZipFile


def zip_viewer(file_path):
    with ZipFile(file_name, 'r') as zip:
        zip.printdir()


def file_unzipper(file_path, file_status, destination_path):
    with ZipFile(file_path, file_status) as zip:
        zip.extractall(path=destination_path)


def file_zipper(file_path, zip_path_name):
    file_paths_to_zip = []

    for root, directories, files in os.walk(file_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths_to_zip.append(filepath)

    with ZipFile(zip_path_name, 'w') as zip:
        for file in file_paths_to_zip:
            zip.write(file)
