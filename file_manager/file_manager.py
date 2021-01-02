import os
from zipfile import ZipFile


class Zipper:
    def __init__(self, file_path=None, destination_path=None, file_status=None, zip_path_name=None, file_paths_to_zip=None):
        self.file_path = file_path
        self.destination_path = destination_path
        self.file_status = file_status
        self.zip_path_name = zip_path_name
        self.file_paths_to_zip = file_paths_to_zip

    def zip_viewer(self, file_path):
        """zip_viewer: Method to view contents of a zipped directory.

        Args:
            file_path (str): File path string; Desired file path to view contents. 

        Returns:
            obj: printdir() contents of file path.
        """
        try:
            with ZipFile(self.file_path, 'r') as zip:
                return zip.printdir()
        except FileNotFoundError:
            print('File Path Not Found')


def main():
    test = Zipper(file_path='../input/zip_1.zip')
    print(test.zip_viewer())


if __name__ == "__main__":
    main()
