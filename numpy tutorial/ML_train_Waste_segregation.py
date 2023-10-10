import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
sensor_data = pd.read_csv('test_data.csv')
selected_column = ['Waste Type','Conductivity (S/m)','Moisture Content (%)','Inductive Property (H/m)','Infrared Property (µm)']
data =sensor_data[selected_column]
x = data[['Conductivity (S/m)','Moisture Content (%)','Inductive Property (H/m)','Infrared Property (µm)']]
y = data[['Waste Type']]
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2,random_state=42)
# print(X_train.count())
Y_train = Y_train.values.ravel()
Y_test = Y_test.values.ravel()
rf_algorithm = RandomForestClassifier(n_estimators=100,max_depth=10,random_state=42)
rf_algorithm.fit(X_train,Y_train)
y_pred = rf_algorithm.predict(X_test)
accuracy = accuracy_score(Y_test,y_pred)
print(accuracy)
joblib.dump(rf_algorithm,'waste_segregation.pkl')