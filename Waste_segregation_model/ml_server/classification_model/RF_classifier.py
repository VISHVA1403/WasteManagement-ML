import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
df = pd.read_csv('test_data.csv')
# seperating properties and lables inot x and y
x, y= df[['Conductivity (S/m)','Moisture Content (%)','Inductive Property (H/m)','Infrared Property (µm)']],df[['Waste Type']]

# spliting the data sheet into training and testing 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# initializing random forest classifier
rfclassifier = RandomForestClassifier(n_estimators=100,max_depth=10,random_state=42)

# fitting 1D array as ravel()
y_train =y_train.values.ravel()
y_test =y_test.values.ravel()
# train the model based on training data
Train_model = rfclassifier.fit(x_train,y_train)

# predicting based on train data to test data
prediction = Train_model.predict(x_test)

# checking accuracy test output and prediction
print("Accuracy score: ",accuracy_score(y_true= y_test , y_pred= prediction))


#dumping into pkl file
joblib.dump(rfclassifier,'rf_segregation_model.pkl')