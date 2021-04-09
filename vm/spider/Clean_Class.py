import pandas as pd
import csv
import os 

class Cleaner():
    def __init__(self):
        # Get the current directory  and the 'media' folder path
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.media_dir = os.path.join(self.current_dir,'media')

        
    def convert_to_csv(self, src):
        # Get the path of the current excel file 
        file_path = os.path.join(self.media_dir,src)
        print(file_name)
        
        # Get the name of the current excel file without extension
        file_name = src.split(".")
        
        # Create a var  with  [filename.csv] 
        cast_in_csv = file_name[0] + ".csv"
        
        # Create a new imaginary path to the csv file "that doesn't exist yet "
        new_full_path = os.path.join(self.media_dir, o)
        
        # Create a new .csv file with the name that we caste
        with open(new_full_path ,mode="w") as f:
            f.write("")
            
        # Load the excel 
        df = pd.read_excel(file_name)

        # Rewrite the empty .csv file with the loaded dataframe 
        df.to_csv(new_full_path, index = False)
            
            

if __name__ == "__main__":
    c = Cleaner()
    c.convert_to_csv("testfilejojo.xlsx")