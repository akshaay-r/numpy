from utils import preprocess_image
import pickle

#load model
with open("model/model.pkl","rb") as f:
    model = pickle.load(f)

#load image
img = preprocess_image("test.jpg").reshape(1,-1)

#predict
prediction = model.predict(img)

#output
if prediction[0] == 0:
    print("Hand detected")
else:
    print("No hand detected")