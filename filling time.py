# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Simulated data for training the model (replace this with actual sensor data)
# Features: Distance measured by ultrasonic sensor
# Target: Time taken for dustbin to fill
np.random.seed(42)
distance = np.random.uniform(5, 30, 100)
time_to_fill = 10 * distance + np.random.normal(0, 5, 100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(distance.reshape(-1, 1), time_to_fill, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Plot the results
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Distance (cm)')
plt.ylabel('Time to Fill (minutes)')
plt.title('Ultrasonic Sensor Prediction Model')
plt.show()

# Use the model to predict the time for a given distance
new_distance = np.array([[15]])  # Replace 15 with the actual distance measured
predicted_time_minutes = model.predict(new_distance.reshape(-1, 1))[0]
predicted_time_hours = predicted_time_minutes / 60
print(f"Predicted Time to Fill: {predicted_time_hours:.2f} hours")
