# import pandas as pd
# import random
# from datetime import datetime, timedelta

# # Create an empty DataFrame
# data = pd.DataFrame(columns=['sensor_id', 'timestamp', 'waste_type', 'inductive_property', 'capacitive_property', 'moisture_property', 'infrared_property'])

# # Generate 1000 data points
# for i in range(1000):
#     sensor_id = random.randint(1, 4)
#     timestamp = (datetime(2023, 9, 1, 12, 0) + timedelta(minutes=i * 15)).strftime('%Y-%m-%d %H:%M:%S')
#     waste_type = random.choice(['recyclable', 'organic', 'non_recyclable'])
#     inductive_property = round(random.uniform(0.6, 1.4), 2)
#     capacitive_property = round(random.uniform(0.0, 1.0), 2)
#     moisture_property = round(random.uniform(0.0, 1.0), 2)
#     infrared_property = round(random.uniform(0.0, 100.0), 2)
    
#     data = data._append({'sensor_id': sensor_id,
#                         'timestamp': timestamp,
#                         'waste_type': waste_type,
#                         'inductive_property': inductive_property,
#                         'capacitive_property': capacitive_property,
#                         'moisture_property': moisture_property,
#                         'infrared_property': infrared_property}, ignore_index=True)

# # Save the DataFrame to a CSV file
# data.to_csv('sensor_data.csv', index=False)
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Load the dataset
sensor_data = pd.read_csv('sensor_data.csv')

# Handling Missing Values
# Replace missing values with the mean for numerical features
imputer = SimpleImputer(strategy='mean')
numerical_features = ['inductive_property', 'capacitive_property', 'moisture_property', 'infrared_property']
sensor_data[numerical_features] = imputer.fit_transform(sensor_data[numerical_features])

# Encoding Categorical Data
# Encode the 'waste_type' column using label encoding
label_encoder = LabelEncoder()
sensor_data['waste_type'] = label_encoder.fit_transform(sensor_data['waste_type'])

# Scaling Numerical Features
# Standardize numerical features to have mean=0 and std=1
scaler = StandardScaler()
sensor_data[numerical_features] = scaler.fit_transform(sensor_data[numerical_features])

# Now, your sensor_data DataFrame contains cleaned and preprocessed data.

# You can save the cleaned data to a new CSV file if needed
sensor_data.to_csv('cleaned_sensor_data.csv', index=False)
