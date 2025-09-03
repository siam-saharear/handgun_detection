import cv2
import os

def read_files():
    current_path = os.getcwd()
    path = os.path.join(current_path, "test_images")
    
    all_images = []
    
    if os.path.exists(path=path):
        for file in os.listdir(path=path):
            if file.split('.')[-1]=="png" or file.split('.')[-1]=="jpg":
                all_images.append(os.path.join(path,file))
            else:
                print(f"{file} not image")
    else:
        print("path not valid")
    
    return all_images
    
    
    
    
