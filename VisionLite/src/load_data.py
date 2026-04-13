import os 
import cv2
import numpy as np
from utils import preprocess_image

def load_data(data_path):
    x=[]
    y=[]

    categories = ['hand','no_hand']

    for category in categories:
        path = os.path.join(data_path,category)
        print(f"Checking folder : {path}")
        label = category.index(category)

        for img_name in os.listdir(path):
            try:
                img_path = os.path.join(path,img_name)
                img = preprocess_image(img_path)

                if img is None:
                    print(f"Failed to load image : {img_name}")
                    continue

                x.append(img)
                y.append(label)

            except Exception as e:
                print(f"Error loading images : {img_name}")

    return np.array(x),np.array(y)

if __name__ == "__main__":
    x,y = load_data("./data")
    print(x.shape)
    print(y.shape)