import cv2

def preprocess_image(img_path):
    img = cv2.imread(img_path)

    if img is None:
        raise ValueError("Image not found")
    
    img = cv2.resize(img,(100,100))
    img = img/255.0
    img = img.flatten()

    return img