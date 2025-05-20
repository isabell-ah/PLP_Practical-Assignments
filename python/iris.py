import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

# Set seaborn style for better visuals
sns.set_style("whitegrid")

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean dataset (fill missing values if any
    if df.isnull().any().any():
        df = df.fillna(df.mean(numeric_only=True))
        print("\nMissing values filled with column means.")
    else:
        print("\nNo missing values found.")

except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"Error occurred: {str(e)}")

# Task 2: Basic Data Analysis
try:
    # Basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

    # Group by species and compute mean for numerical columns
    grouped_means = df.groupby('species').mean()
    print("\nMean values by species:")
    print(grouped_means)

    # Observations
    print("\nFindings:")
    print("- The dataset contains three species: setosa, versicolor, and virginica.")
    print("- Each species has distinct measurements, with virginica generally having larger features.")

except Exception as e:
    print(f"Error during analysis: {str(e)}")

# Task 3: Data Visualization
try:
    # Visualization 1: Line Chart (Sepal Length over Index, per Species)
    plt.figure(figsize=(10, 6))
    for species in df['species'].unique():
        species_data = df[df['species'] == species]
        plt.plot(species_data.index, species_data['sepal length (cm)'], label=species)
    plt.title('Sepal Length Trend Across Observations by Species')
    plt.xlabel('Observation Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    plt.savefig('sepal_length_line.png')
    plt.close()

    # Visualization 2: Bar Chart (Average Petal Length by Species)
    plt.figure(figsize=(8, 6))
    sns.barplot(x='species', y='petal length (cm)', data=df)
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.savefig('petal_length_bar.png')
    plt.close()

    # Visualization 3: Histogram (Sepal Width Distribution)
    plt.figure(figsize=(8, 6))
    plt.hist(df['sepal width (cm)'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.savefig('sepal_width_histogram.png')
    plt.close()

    # Visualization 4: Scatter Plot (Sepal Length vs Petal Length)
    plt.figure(figsize=(8, 6))
    for species in df['species'].unique():
        species_data = df[df['species'] == species]
        plt.scatter(species_data['sepal length (cm)'], species_data['petal length (cm)'], 
                    label=species, alpha=0.7)
    plt.title('Sepal Length vs Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    plt.savefig('sepal_vs_petal_scatter.png')
    plt.close()

    print("\nVisualizations saved as PNG files:")
    print("- sepal_length_line.png")
    print("- petal_length_bar.png")
    print("- sepal_width_histogram.png")
    print("- sepal_vs_petal_scatter.png")

except Exception as e:
    print(f"Error during visualization: {str(e)}")