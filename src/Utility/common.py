import os 


def Create_Folder(path):
    try:
        os.makedirs(path,exist_ok=True)
        print(f"{path} Created")
    except Exception as e:
        raise e     