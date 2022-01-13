import os

path = r"C:\Users\sshanmu2\Desktop\shan"

os.chdir(path)
  
  
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
  
  
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        read_text_file(file_path)
