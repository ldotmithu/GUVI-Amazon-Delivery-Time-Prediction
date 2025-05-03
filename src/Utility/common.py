import os 
import yaml

def Create_Folder(path):
    try:
        os.makedirs(path,exist_ok=True)
        print(f"{path} Created")
    except Exception as e:
        raise e     
    
def Read_yaml(path):
    with open(path ,'r') as f:
        file = yaml.safe_load(f)
        print(f"{path} Read the yaml successfully")
        return file