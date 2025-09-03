import cv2
import os

from ultralytics import YOLO

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
    
    
    
def load_model():
    current_path = os.getcwd()
    model_path = os.path.join(current_path, "model", "best.pt")
    if os.path.exists(model_path):
        model = YOLO(model=model_path)
        return "okk"
    else:
        print("model not found")
        
        
        
    