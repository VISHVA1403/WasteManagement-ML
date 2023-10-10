import matplotlib.pyplot as plt
import pandas as pd

# Sample data (you can replace this with your actual dataset)
data = pd.read_csv('test_data.csv')

# Group data by waste type and calculate mean values
grouped_data = data.groupby('Waste Type').mean().reset_index()

# Extract properties and values
waste_types = grouped_data['Waste Type']
moisture_content = grouped_data['Moisture Content (%)'] % 100
conductivity = grouped_data['Conductivity (S/m)']
inductivity = grouped_data['Inductive Property (H/m)']
infrared = grouped_data['Infrared Property (µm)']

plt.style.use('_mpl-gallery')
# Create a stacked plot
plt.figure(figsize=(10, 6))

# Plot stacked areas for each property
plt.stackplot(waste_types, moisture_content, conductivity, inductivity, infrared, labels=['Moisture Content (%)', 'Conductivity (S/m)', 'Inductive Property (H/m)', 'Infrared Property (µm)'],alpha=0.7)

# Add labels and title
plt.xlabel('Waste Type')
plt.ylabel('Property Level')
plt.title('Waste Properties by Type')
plt.xticks(rotation=45)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
