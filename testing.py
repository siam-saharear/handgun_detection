import cv2
import os

from ultralytics import YOLO

from training import most_recent_model


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
    model_path = most_recent_model()
    if os.path.exists(model_path):
        model = YOLO(model=model_path)
        return model
    else:
        print("model not found")
        
        
def detect(model, image):
    image = cv2.imread(image)
    results = model(image)    
    annotated = results[0].plot()
    cv2.imshow("detection", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
all_files = read_files()
model = load_model()
for image in all_files:
    detect(model=model, image=image)
    
