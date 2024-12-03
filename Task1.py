# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define settings
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.width', 80)  # Set line wrapping width
plt.style.use('seaborn-darkgrid')  # Aesthetic visualizations

# Load dataset
data = pd.read_csv('QVI_purchase_behaviour.csv')

# Data Summary
print("Data Overview:")
print(data.info())

# Data Cleaning
print("\nChecking for missing values:")
print(data.isnull().sum())

# Handle missing data (example: drop rows with missing values)
data = data.dropna()

# Handle outliers (example: IQR method)
Q1 = data['spend'].quantile(0.25)
Q3 = data['spend'].quantile(0.75)
IQR = Q3 - Q1
data = data[~((data['spend'] < (Q1 - 1.5 * IQR)) | (data['spend'] > (Q3 + 1.5 * IQR)))]

# Feature Engineering
data['pack_size'] = data['product_name'].str.extract(r'(\d+)g').astype(float)
data['brand'] = data['product_name'].str.split().str[0]

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x='brand', y='spend', data=data, ci=None)
plt.title('Brand Spend Analysis')
plt.xlabel('Brand')
plt.ylabel('Total Spend')
plt.xticks(rotation=45)
plt.show()

# Save processed data
data.to_csv('processed_data.csv', index=False)
