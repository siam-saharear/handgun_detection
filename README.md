# Handgun Detection  

## About  
This project is built on the **Ultralytics YOLOv8n** model.  
- Training dataset: ~300 images for handguns and ~100 images for bullets.  
- You can either:  
  - Train the model from scratch, or  
  - Fine-tune it on top of the pre-trained weights included in this repo.  

---

## Testing  
1. Place all test images inside the `test_images/` folder.  
2. Run `manage.py`.  
3. From the menu, select **Detect Images**.  

---

## Training  
1. Use **LabelImg** to annotate your images.  
2. Split the dataset into an **80:20 ratio**:  
   - Training images → `train/images/`  
   - Validation images → `val/images/`  
3. Place corresponding labels in:  
   - `train/labels/`  
   - `val/labels/`  
4. Keep everything unchanged in data.yaml 
5. Run `manage.py`.  
6. From the menu, select **Train Model**.  

---

## Detection Results  
Here are some sample detection outputs from the model:  

![Detection Example 1](examples/Screenshot%20from%202025-09-06%2014-46-24.png)  
![Detection Example 2](examples/Screenshot%20from%202025-09-06%2014-46-58.png)  
![Detection Example 3](examples/Screenshot%20from%202025-09-06%2014-47-09.png)  
![Detection Example 4](examples/Screenshot%20from%202025-09-06%2014-47-39.png)  
![Detection Example 5](examples/Screenshot%20from%202025-09-06%2014-47-53.png)  
