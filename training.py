from ultralytics import YOLO
import os
import cv2
  
      
def most_recent_model():
    current_path = os.getcwd()
    model_folder_path = os.path.join(current_path, "model")
    max_run = 0
    if len(os.listdir(model_folder_path)) != 0:
        for run in os.listdir(model_folder_path):
            if run[:3] == "run":
                run_no = int(run[-1])
            else:
                run_no = 1
            if run_no > max_run:
                max_run = run_no
            else:
                pass
            
        max_run_train_path = os.path.join(current_path, model_folder_path, f"runs_{max_run}", "detect")

        max_train = 1
        for train in os.listdir(max_run_train_path):
            if train[-1]!= "n" and train[:5]=="train":
                train_no = int(train[-1])
            else:
                train_no = 1
            if train_no > max_train:
                max_train = train_no
        if max_train == 1:
            final_train = "train"
        else:
            final_train = f"train{max_train}"
        
        most_recent_model_path = os.path.join( 
                                            model_folder_path, 
                                            f"runs_{max_run}", 
                                            "detect", 
                                            final_train, 
                                            "weights", 
                                            "best.pt")
    else:
        most_recent_model_path = None
    
    return most_recent_model_path


def next_run_folder():
    current_path = os.getcwd()
    model_folder_path = os.path.join(current_path, "model")
    if len(os.listdir(model_folder_path)) != 0:
        max_run = 1
        for run in os.listdir(model_folder_path):
            if run[:3] == "run":
                run_no = int(run[-1])
                if run_no > max_run:
                    max_run = run_no
        new_run_path = os.path.join(model_folder_path, f"runs_{max_run+1}")
    else:
        new_run_path = os.path.join(model_folder_path, "runs_1")
    os.makedirs(new_run_path, exist_ok = True)
    
    return new_run_path


def train_model():
    if most_recent_model() != None:
        model = YOLO(most_recent_model())
    else:
        model = YOLO("yolov8n.pt")
    model.train(data="training_images/data.yaml",
                project=next_run_folder(),
                name = "detect/train",
                epochs=50,
                imgsz=640, 
                )
    print("Check for new model")

print(most_recent_model())