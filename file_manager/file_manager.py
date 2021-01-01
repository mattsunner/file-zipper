import os
from zipfile import ZipFile
           
            
 class Zipper:
 	def __init__(self, file_path, destination_path=None, file_status=None, zip_path_name=None, file__paths_to_zip=None):
 		self.file_path = file_path
 		self.destination_path = destination_path
 		self.file_status = file_status
 		self.zip_path_name = zip_path_name
 		self.file_paths_to_zip = file__paths_to_zip
 		
 	def zip_viewer(self):
    with ZipFile(self.file_name, 'r') as zip:
        zip.printdir()
        
 	def file_unzipper(self.file_path, self.file_status, self.destination_path):
    with ZipFile(self.file_path, self.file_status) as zip:
        zip.extractall(path=self.destination_path)
        
  def file_zipper(self.file_path, self.zip_path_name):
    file_paths_to_zip = []

    for root, directories, files in os.walk(file_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths_to_zip.append(filepath)
            
    with ZipFile(zip_path_name, 'w') as zip:
        for file in file_paths_to_zip:
            zip.write(file)
            
 
 def main():
 	pass 
 	
 	
 if __name__ == "__main__":
 	main()
