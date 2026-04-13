from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

from load_data import load_data

#Load data
x,y = load_data("./data")

#split data
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#train model 
model = RandomForestClassifier(n_estimators=100)
model.fit(x_train,y_train)

#prediction
y_pred = model.predict(x_test)

#Accuracy
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy : ",accuracy)

#Save model

with open("model/model.pkl","wb") as f:
    pickle.dump(model,f)

print("Model saved successfully")